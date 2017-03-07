#coding: utf8
from django.shortcuts import render, reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, View
from core.models import User, Psycologist
from core.forms import RegistrationForm, CkEditorForm
from article.models import Entry
from django.views import generic
from django.db.models import Q
from message.models import Chat

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

    def dispatch(self, request, pk=None, *args, **kwargs):
        if self.request.user.is_psycologist == True:
            self.chats = Chat.objects.filter(psycologist=self.request.user.psycologist)
        else:
            self.chats = Chat.objects.filter(client=self.request.user.client)
        return super(Self_room, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
         context = super(Self_room, self).get_context_data(**kwargs)
         context['chats'] = self.chats
         return context


class Self_update(UpdateView):
    template_name = 'core/self_update.html'
    model = User
    fields = ('username', 'first_name', 'last_name', 'avatar', 'first_name', 'city')

    def get_success_url(self):
        return reverse('core:self_room')

    def get_object(self, queryset=None):
        return self.request.user

class List_article(ListView):
    template_name = 'core/list_article.html'
    model = Entry

    def dispatch(self, request, pk=None, *args, **kwargs):
         self.post = Entry.objects.filter(user=self.request.user).order_by('-id')
         return super(List_article, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
         context = super(List_article, self).get_context_data(**kwargs)
         context['post'] = self.post
         return context

class Create_article(CreateView):
    template_name = 'core/create_article.html'
    model = Entry
    fields = ['title', 'content',]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(Create_article, self).form_valid(form)

    def get_success_url(self):
        return reverse('core:self_room')

class Show_user(DetailView):
    template_name = 'core/user.html'
    context_object_name = 'us'
    model = User

class Show_users(ListView):
    template_name = 'core/psyc.html'
    context_object_name = 'u'
    model = Psycologist
