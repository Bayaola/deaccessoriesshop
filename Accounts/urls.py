from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import RegistrationView, ProfileView, MembershipView, UpdateAccountMembershipView

app_name = 'Accounts'

urlpatterns = [
    path('register/', RegistrationView.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    path('memberships/', MembershipView.as_view(), name='select'),
    path('memberships/<int:pk>', views.UpdateAccountMembershipView, name='select-update'),

    # Wish List
    path("wishlist", views.wishlist, name="wishlist"),
    path("wishlist/add_to_wishlist/<int:id>", views.add_to_wishlist, name="user_wishlist"),
]