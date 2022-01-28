from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from Forums.models import Forum, Comment

# Create your views here.

class StoresListView(ListView):
    # model = Forum
    # queryset = Forum.objects.order_by('-created_at')
    # paginate_by = 2
    model = Forum
    queryset = Forum.objects.order_by('-created_at')
    template_name = 'Stores/index.html'
    