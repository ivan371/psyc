from django.shortcuts import render
from django.views.generic import ListView
from article.models import Entry

class Last_article(ListView):
    template_name = 'article/last_article.html'
    model = Entry

    def dispatch(self, request, pk=None, *args, **kwargs):
         self.post = Entry.objects.order_by('-id')
         return super(Last_article, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
         context = super(Last_article, self).get_context_data(**kwargs)
         context['post'] = self.post
         return context
