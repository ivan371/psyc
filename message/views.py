#coding=utf8
from django.shortcuts import render, get_object_or_404, HttpResponse, render_to_response
from core.models import User, Psycologist
from message.models import Message, Chat
from django.views.generic import ListView, CreateView, DetailView, UpdateView, View
from django.db.models import Q
from message.forms import MessageForm
from django.template import RequestContext

class Showchat(ListView):
    model = Message
    template_name = "message/showchat.html"

    def dispatch(self, request, pk=None, *args, **kwargs):
        self.chat = []
        self.messages = []
        if self.request.user.is_psycologist == True:
            self.ps = self.request.user
            self.cl = get_object_or_404(User, id=pk)
        else:
            self.cl = self.request.user
            self.ps = get_object_or_404(User, id=pk)
        if self.ps.is_psycologist() == True and self.cl.is_psycologist() == False:
            try:
                self.chat = Chat.objects.get(
                psycologist=self.ps.psycologist,
                client=self.cl.client)
            except Chat.DoesNotExist:
                self.chat = Chat(
                    psycologist=self.ps.psycologist,
                    client=self.cl.client)
                self.chat.save()

            self.messages = Message.objects.filter(char=self.chat)
            #.filter(Q(user = self.request.user) | Q(user = self.psycologist))
        return super(Showchat, self).dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('message:detail')

    def get_context_data(self, **kwargs):
         context = super(Showchat, self).get_context_data(**kwargs)
         context['chat'] = self.chat
         context['messages'] = self.messages
         return context

def create_message(request, pk):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            m = Message(
                user = request.user,
                char = Chat.objects.get(id=pk),
                content = data['text']
            )
            m.save()
            text = "Сообщение отправлено"
        else:
            text = "Ошибка при обработке данных"
    else:
        text = "Ошибка при отправке сообщения"
    id = pk
    return render_to_response('message/textform.html', {'text': text, 'id': id})
    #return HttpResponse("Все ок")
