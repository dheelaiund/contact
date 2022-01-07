from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class Home(TemplateView):
    template_name = 'contact/home.html'

class Index(TemplateView):
    template_name = 'contact/index.html'

class Display(TemplateView):
    template_name = 'contact/display_contacts.html'