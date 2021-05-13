from django.urls import path
from .views import (
    QuizFormView, QuizListView, QuizCreateView, QuizUpdateView, QuizDeleteView,
)
from . import views

app_name = 'app'

urlpatterns = [
    path('',QuizFormView.as_view(), name='home'),
    path('create_quiz/', QuizCreateView.as_view(), name='create_quiz'),
    path('quiz_list/', QuizListView.as_view(), name='quiz_list'),
    path('update_quiz/<int:pk>', QuizUpdateView.as_view(), name='update_quiz'),
    path('delete_quiz/<int:pk>', QuizDeleteView.as_view(), name='delete_quiz'),
]
