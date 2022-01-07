from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse
# Create your views here.

class Home(TemplateView):
    template_name = 'accounts/home.html'

class RegisterUser(TemplateView):
    template_name = 'accounts/registeruser.html'
    user_creation_form = UserCreationForm


    def get(self, request, *args, **kwargs):
        # return super().get(request, *args, **kwargs)
        form = self.user_creation_form()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.user_creation_form(request.POST)
        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(
                    request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('accounts:home')
            except IntegrityError:
                return render(request, self.template_name, {'form': form})

        else:
            return render(request, self.template_name, {'form': form})
            
            

        return render(request, self.template_name, {'form': form})


class LoginUser(TemplateView):
    template_name = 'accounts/loginuser.html'
    authentication_form = AuthenticationForm

    def get(self, request, *args, **kwargs):
        # return super().get(request, *args, **kwargs)
        form = self.authentication_form()
        return render(request, self.template_name, {'form': self.authentication_form()})

    def post(self, request, *args, **kwargs):
        user = authenticate(
            request, username=request.POST["username"], password=request.POST["password"])
        if user:
            login(request, user)
            return redirect('accounts:home')
        else:
            print('user do no exist')
            return render(request, self.template_name, {'form': self.authentication_form()})


class LogoutUser(TemplateView):
    template_name = 'accounts/logoutuser.html'