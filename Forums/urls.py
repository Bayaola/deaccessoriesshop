from django.urls import path
from .views import *


urlpatterns = [
    # path('forum/', views.listView, name='listView'),
    path('', ForumListView.as_view(), name='forum-list'),
    path('<slug:slug>/', ForumDetailView.as_view(), name='forum-detail'),
    path('add-comment/<int:pk>', CommentCreateView.as_view(), name='add-comment'),

    path('edit-comment/<int:pk>', CommentUpdateView.as_view(), name='edit-comment'),
    path('delete-comment/<int:pk>', CommentDeleteView.as_view(), name='delete-comment'),
]