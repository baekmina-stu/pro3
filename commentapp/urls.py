from django.urls import path

from commentapp.views import CommentCreateView, CommentDeleteView

# Create your models here.
app_name = 'commentapp'

urlpatterns = [
    path('create/', CommentCreateView.as_view(), name='create'),
    path('delete/<int:pk>', CommentDeleteView.as_view(), name='delete'),
]