from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View

from .forms import LoginForm, RegistrationForm
from .models import CustomUser


class LoginView(View):
    def get(self, request, *args, **kwargs):
        form = LoginForm(request.POST or None)
        context = {'form': form}
        return render(request, 'account/login.html', context)

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST or None)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse('all_news'))
        context = {'form': form}
        return render(request, 'account/login.html', context)


class RegistrationView(View):
    def get(self, request, *args, **kwargs):
        form = RegistrationForm(request.POST or None)
        context = {'form': form}
        return render(request, 'account/registration.html', context)

    def post(self, request, *args, **kwargs):
        form = RegistrationForm(request.POST or None)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.email = form.cleaned_data['email']
            new_user.password = form.cleaned_data['password']
            new_user.confirm_password = form.cleaned_data['confirm_password']
            # new_user.save()
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            # CustomUser.objects.create(
            #     email=new_user.email,
            #     password=new_user.password)
            user = authenticate(email=form.cleaned_data['email'],
                                password=form.cleaned_data['password'])
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse('all_news'))
        context = {'form': form}
        return render(request, 'account/registration.html', context)


@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html', {'section': 'dashboard'})
