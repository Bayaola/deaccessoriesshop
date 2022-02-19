from ast import arg
from urllib import request
from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponseForbidden
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.urls import reverse
from .forms import CommentForm
from .models import Forum, Comment


# Create your views here.

# @method_decorator(login_required, name='dispatch')
class ForumListView(ListView):
    model = Forum
    queryset = Forum.objects.order_by('-created_at')
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.all()
        return context

class ForumDetailView(DetailView):
    model = Forum
    template_name = 'Forums/forum_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_comment'] = CommentForm()
        return context


class OwnerProtectMixin(object):
    def dispatch(self, request, *args, **kwargs):
        objectUser = self.get_object()
        if objectUser.user != self.request.user:
            return HttpResponseForbidden()
        return super(OwnerProtectMixin, self).dispatch(request, *args, **kwargs)


@method_decorator(login_required, name='dispatch')
class ForumUpdateView(OwnerProtectMixin, UpdateView):
	model = Forum
	fields = ['title','desc']
	template_name = 'Forums/forum_update_form.html'

	def get_success_url(self, **kwargs):
		return reverse_lazy('forum-detail', kwargs={'slug' : self.object.slug})


@method_decorator(login_required, name='dispatch')
class ForumDeleteView(SuccessMessageMixin, OwnerProtectMixin, DeleteView):
	model = Forum
	success_url = '/forums'
	success_message = 'Forum was successfully deleted'


@method_decorator(login_required, name='dispatch')
class ForumCreate(SuccessMessageMixin, CreateView):
	model = Forum
	fields = ['title','desc']

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super().form_valid(form)    


@method_decorator(login_required, name='dispatch')
class CommentCreateView(CreateView):
    model = Comment
    fields = ['desc']
    success_message = 'Forum was successfully created'
    # success_url = reverse_lazy('forum-detail')

    def form_valid(self, form):
        self._forum = get_object_or_404(Forum, id=self.kwargs['pk'])
        form.instance.user = self.request.user
        form.instance.forum = self._forum
        return super().form_valid(form)

    def get_success_url(self, **kwargs):
        return reverse_lazy('forum-detail', kwargs={'slug' : self._forum.slug})


@method_decorator(login_required, name='dispatch')
class CommentUpdateView(OwnerProtectMixin, UpdateView):
    model = Comment
    fields = ['desc']
    template_name = 'Forums/forum_update_comment.html'

    def get_success_url(self):
        self.forum = self.object.forum
        return reverse_lazy('forum-detail', kwargs={'slug': self.forum.slug})


@method_decorator(login_required, name='dispatch')
class CommentDeleteView(OwnerProtectMixin, DeleteView):
    model = Comment

    def get_success_url(self):
        self.forum = self.object.forum
        return reverse_lazy('forum-detail', kwargs={'slug': self.forum.slug})