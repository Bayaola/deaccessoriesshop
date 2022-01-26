from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from .forms import CommentForm
from .models import Forum, Comment
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponseForbidden
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

# Create your views here.

@method_decorator(login_required, name='dispatch')
class ForumListView(ListView):
    model = Forum
    queryset = Forum.objects.order_by('-created_at')
    paginate_by = 2

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)

    #     # context['form_comment'] = 
    #     return context

class ForumDetailView(DetailView):
    model = Forum
    template_name = 'Forums/forum_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_comment'] = CommentForm()
        return context


class ForumCreate(CreateView):
    model = Forum
    fields = ['title','desc']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)      


class CommentCreateView(CreateView):
    model = Comment
    fields = ['desc']
    success_message = 'Forum was successfully created'

    def form_valid(self, form):
        _forum = get_object_or_404(Forum, id=self.kwargs['pk'])
        form.instance.user = self.request.user
        form.instance.forum = _forum
        return super().form_valid(form)