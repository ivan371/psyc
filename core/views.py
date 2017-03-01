from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from core.models import User


def home(request):
    return render(request, 'core/index.html')

class Registration(CreateView):
    template_name = 'core/registration.html'
    model = User
    fields = ['username', 'password', 'first_name', 'email', 'last_name', 'avatar']
    def get_success_url(self):
         return reverse('core:home')
