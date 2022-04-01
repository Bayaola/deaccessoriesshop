from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import Account, Membership, Subscription
from .forms import RegistrationForm
from Stores.models import *


def global_params(request):
    if request.user.is_anonymous:
        subscription_info = None
    else:
        try:
            subscription_info = Subscription.objects.get(user_membership=request.user)
        except Subscription.DoesNotExist:
             subscription_info = None

    # subscription_info = Subscription.objects.get(user_membership=request.user)
    context = {
        "subscription_info": subscription_info,
    }
    return context


@login_required
def wishlist(request):
    products = Product.objects.filter(users_wishlist=request.user)
    return render(request, "dashboard/user_wish_list.html", {"wishlist": products})


@login_required
def add_to_wishlist(request, id):
    product = get_object_or_404(Product, id=id)
    if product.users_wishlist.filter(id=request.user.id).exists():
        product.users_wishlist.remove(request.user)
        messages.success(request, product.title + " has been removed from your WishList")
    else:
        product.users_wishlist.add(request.user)
        messages.success(request, "Added " + product.title + " to your WishList")
    return HttpResponseRedirect(request.META["HTTP_REFERER"])

    
class RegistrationView(CreateView):
    template_name = 'register.html'
    form_class = RegistrationForm

    def get_context_data(self, *args, **kwargs):
        context = super(RegistrationView, self).get_context_data(*args, **kwargs)
        context['next'] = self.request.GET.get('next')
        return context

    def get_success_url(self):
        next_url = self.request.POST.get('next')
        success_url = reverse('Accounts:login')
        if next_url:
            success_url += '?next={}'.format(next_url)

        return success_url


class ProfileView(UpdateView):
    model = Account
    fields = ['name', 'phone', 'date_of_birth', 'picture']
    template_name = 'registration/profile.html'

    def get_success_url(self):
        return reverse('index')

    def get_object(self):
        return self.request.user
        

class MembershipView(ListView):
    model = Membership
    template_name = 'memberships_list.html'

    def get_user_membership(self, *args):
        user_membership_qs = Account.objects.filter(name=self.request.user)
        if user_membership_qs.exists():
            return user_membership_qs.first()
        return None

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        current_membership = self.get_user_membership(self.request)
        context['current_membership'] = str(current_membership.membership)
        return context


def UpdateAccountMembershipView(request, pk):
    if request.method == 'POST':
        membership_type = request.POST.get("membership_type")
        account = Account.objects.get(id=int(request.user.id))
        membership = Membership.objects.get(id=int(pk))
        account.membership = membership
        account.save()
        # next_url = self.request.POST.get('next')

        return redirect('Stores:store_home')

        # print(membership.price, pk, request.user.id)

