from os import stat
from django.forms.forms import Form
from django.shortcuts import render, redirect
from . import forms
from django.contrib import messages
from .models import Quiz
from django.views.generic.edit import (
    CreateView, UpdateView, DeleteView,
)
from django.views.generic.list import ListView
from pure_pagination.mixins import PaginationMixin
from django.urls import reverse_lazy

class QuizFormView(ListView):
    template_name = 'home.html'
    model = Quiz
    def get_queryset(self):
        return Quiz.objects.order_by('?')[:1]

class QuizCreateView(CreateView):
    template_name = 'create_quiz.html'
    form_class = forms.CreateQuizForm
    model = Quiz

    def get_initial(self, **kwargs):
        initial = super(QuizCreateView, self).get_initial(**kwargs)
        initial['category'] = 'その他'
        return initial



class QuizListView(PaginationMixin, ListView):
    model = Quiz
    template_name = 'quiz_list.html'
    paginate_by = 10

    def get_queryset(self):
        qs = super(QuizListView, self).get_queryset()
        qs = qs.order_by('id')
        return qs

class QuizUpdateView(UpdateView):
    model = Quiz
    template_name = 'update_quiz.html'
    form_class = forms.QuizUpdateForm


class QuizDeleteView(DeleteView):
    model = Quiz
    template_name = 'delete_quiz.html'
    success_url = reverse_lazy('app:quiz_list')

# エラーハンドリング
def show_error_page(request, exception):
    return render(
        request, '404.html', status=404
    )








