from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView, ListView, DetailView

from articleapp.models import Article
from projectapp.forms import ProjectCreationForm
from projectapp.models import Project
from subscribeapp.models import Subscription

import requests
from bs4 import BeautifulSoup

class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectCreationForm
    template_name = 'projectapp/create.html'

    def get_success_url(self):
        return reverse('projectapp:detail', kwargs={'pk': self.object.pk})


class ProjectDetailView(DetailView):
    model = Project
    context_object_name = 'target_project'
    template_name = 'projectapp/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        project = self.object
        if user.is_authenticated:
            subscription = Subscription.objects.filter(user=user, project=project)
        else:
            subscription = None
        context['subscription'] = subscription

        # Get the list of articles related to the project
        article_list = Article.objects.filter(project=project)
        context['article_list'] = article_list

        # Crawl data from external sources
        inflearn_posts, soup_posts = crawl_inflearn_soup(project.title)
        context['inflearn_posts'] = inflearn_posts
        context['soup_posts'] = soup_posts

        return context


class ProjectListView(ListView):
    model = Project
    context_object_name = 'project_list'
    template_name = 'projectapp/list.html'
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Get the list of articles
        article_list = Article.objects.all()
        context['article_list'] = article_list

        return context


def crawl_inflearn_soup(title):
    inflearn_url = f'https://www.inflearn.com/community/studies?status=unrecruited&tag={title}&order=recent'
    soup_url = 'https://soup.pw/projects'

    inflearn_response = requests.get(inflearn_url)
    soup_response = requests.get(soup_url)

    if inflearn_response.status_code == 200 and soup_response.status_code == 200:
        inflearn_soup = BeautifulSoup(inflearn_response.content, 'html.parser')
        soup_soup = BeautifulSoup(soup_response.content, 'html.parser')

        inflearn_posts = []
        e_click_posts = inflearn_soup.find_all(class_='e-click-post')
        for post in e_click_posts[:5]:
            title = post.find(class_='title__text').get_text()
            body = post.find(class_='question__body').get_text()[:30] + "..."
            if "[개발 스터디 모집 내용 예시]" not in title:
                inflearn_posts.append({
                    'title': title,
                    'body': body
                })

        soup_posts = []
        study_items = soup_soup.find_all(class_='css-1089e3a')
        for item in study_items[:5]:
            content = item.get_text()
            soup_posts.append({
                'content': content
            })

        return inflearn_posts, soup_posts

