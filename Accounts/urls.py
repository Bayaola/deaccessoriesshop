from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import RegistrationView, ProfileView, MembershipView, UpdateAccountMembershipView

urlpatterns = [
    path('register/', RegistrationView.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    path('memberships/', MembershipView.as_view(), name='select'),
    path('memberships/<int:pk>', views.UpdateAccountMembershipView, name='select-update'),
]