#coding: utf8
from django.shortcuts import render, reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from core.models import User
from core.forms import RegistrationForm, CkEditorForm
from article.models import Article, Entry
from django.views import generic

def home(request):
    return render(request, 'core/index.html')

class Registration(CreateView):
    template_name = 'core/registration.html'
    model = User
    form_class = RegistrationForm
    def get_success_url(self):
         return reverse('core:home')

class Self_room(ListView):
    template_name = 'core/self_room.html'
    model = User
    fields = ('last_name', 'avatar', 'first_name', 'city')

class Self_update(UpdateView):
    template_name = 'core/self_update.html'
    model = User
    fields = ('last_name', 'avatar', 'first_name', 'city')

    def get_success_url(self):
        return reverse('core:self_room')

    def get_object(self, queryset=None):
        return self.request.user

class List_article(ListView):
    template_name = 'core/list_article.html'
    context_object_name = 'post'
    model = Article

class Create_article(CreateView):
    template_name = 'core/create_article.html'
    model = Entry
    fields = ['title', 'content',]

    def get_success_url(self):
        return reverse('core:self_room')
