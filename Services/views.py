from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic.edit import FormMixin
from .models import Service, MessageService
from .forms import MessageForm
from django.urls import reverse_lazy

from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.

class ServicesList(generic.ListView):
    queryset = Service.objects.all()
    template_name = 'services/index.html'


class ServiceDetail(generic.DetailView):
    model = Service
    template_name = 'services/service_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = MessageForm()
        return context

 

class SendMessage(SuccessMessageMixin, generic.CreateView):
    model = MessageService
    fields = ['name', 'email', 'subject', 'message']
    success_message = 'message was successfully created'
    # success_url = reverse_lazy('Services:service_detail')

    def form_valid(self, form):
        self._message = get_object_or_404(Service, id=self.kwargs['pk'])
        form.instance.service = self._message
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        subject = form.cleaned_data['subject']
        message = form.cleaned_data['message']
        return super().form_valid(form)

    def get_success_url(self, **kwargs):
        return reverse_lazy('Services:service_detail', kwargs={'slug' : self._message.slug})