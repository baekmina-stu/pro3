from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Question, Answer
from django.http import HttpResponseNotAllowed
from .forms import QuestionForm, AnswerForm
from django.core.paginator import Paginator
from articleapp.models import Article
from django.contrib.auth.decorators import login_required
from django.contrib import messages



def index(request):
    search_subject = request.GET.get('search_subject')  # subject 검색어 가져오기
    search_content = request.GET.get('search_content')  # content 검색어 가져오기

    # 질문 목록 조회
    question_list = Question.objects.order_by('-create_date')

    # 검색어가 제공된 경우, 검색어에 따라 질문 목록 필터링
    if search_subject:
        question_list = question_list.filter(subject__icontains=search_subject)
    if search_content:
        question_list = question_list.filter(content__icontains=search_content)

    paginator = Paginator(question_list, 10)
    page = request.GET.get('page', 1)
    page_obj = paginator.get_page(page)

    context = {
        'question_list': page_obj,
        'search_subject': search_subject,
        'search_content': search_content
    }
    return render(request, 'jjit/question_list.html', context)



def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'jjit/question_detail.html', context)


@login_required(login_url='accountapp:login')
def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.writer = request.user
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('jjit:detail', question_id=question.id)
    else:
        return HttpResponseNotAllowed('Only POST is possible.')
    context = {'question': question, 'form': form}
    return render(request, 'jjit/question_detail.html', context)

@login_required(login_url='accountapp:login')
def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.create_date = timezone.now()
            question.writer = request.user
            question.save()
            return redirect('jjit:index')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'jjit/question_form.html', context)




@login_required(login_url='accountapp:login')
def question_modify(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.writer:
        messages.error(request, '수정권한이 없습니다')
        return redirect('jjit:detail', question_id=question.id)

    if request.method == "POST":
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.modify_date = timezone.now()  # 수정일시 저장
            question.save()
            return redirect('jjit:detail', question_id=question.id)
    else:
        form = QuestionForm(instance=question)

    context = {'form': form, 'question': question}

    return render(request, 'jjit/question_form.html', context)



@login_required(login_url='accountapp:login')
def question_delete(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('jjit:detail', question_id=question.id)
    question.delete()
    return redirect('jjit:index')

@login_required(login_url='accountapp:login')
def answer_modify(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.user != answer.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('jjit:detail', question_id=answer.question.id)
    if request.method == "POST":
        form = AnswerForm(request.POST, instance=answer)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.modify_date = timezone.now()
            answer.save()
            return redirect('jjit:detail', question_id=answer.question.id)
    else:
        form = AnswerForm(instance=answer)
    context = {'answer': answer, 'form': form}
    return render(request, 'jjit/answer_form.html', context)
