from django.shortcuts import render,redirect
from django.views.generic import TemplateView,View,FormView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse

# Create your views here.


class RegisterUser(FormView):

    model = User
    template_name = 'accounts/registeruser.html'
    
   

    def get(self, request, *args, **kwargs):
        # return super().get(request, *args, **kwargs)
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        
        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(
                    request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('contact:displaycontacts')
            except IntegrityError:
                return render(request, self.template_name, {'error': 'Username already taken'})

        else:
            return render(request, self.template_name, {'error':'Passwords do not match'})
            
             


class LoginUser(TemplateView):
    template_name = 'accounts/loginuser.html'

    def get(self, request, *args, **kwargs):
        # return super().get(request, *args, **kwargs)
        return render(request, self.template_name, {})

    def post(self, request, *args, **kwargs):
        user = authenticate(
            request, username=request.POST["username"], password=request.POST["password"])
        if user:
            login(request, user)
            return redirect('contact:displaycontacts')
        else:
            
            return render(request, self.template_name, {'error': 'Incorrect Username or Password'})


class LogoutUser(View):
    def get(self, request):
        logout(request)
        return redirect('accounts:loginuser')