from django.urls import path
from .views import *


urlpatterns = [
    # path('forum/', views.listView, name='listView'),
    path('', ForumListView.as_view(), name='forum-list'),
    path('add/', ForumCreate.as_view(), name='forum-add'),
    path('edit/<int:pk>', ForumUpdateView.as_view(), name='forum-edit'),
	path('delete/<int:pk>', ForumDeleteView.as_view(), name='forum-delete'),

    path('<slug:slug>/', ForumDetailView.as_view(), name='forum-detail'),
    path('add-comment/<int:pk>', CommentCreateView.as_view(), name='add-comment'),

    path('edit-comment/<int:pk>', CommentUpdateView.as_view(), name='edit-comment'),
    path('delete-comment/<int:pk>', CommentDeleteView.as_view(), name='delete-comment'),
]