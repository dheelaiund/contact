from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy
from django.http import Http404
from django.views import generic

from braces.views import SelectRelatedMixin

from . import forms
from . import models

from django.contrib.auth import get_user_model
User = get_user_model()


class Home(TemplateView):
    template_name = 'contact/home.html'


class Index(TemplateView):
    template_name = 'contact/index.html'


class UserAllContacts(LoginRequiredMixin, ListView):
    model = models.UserContacts
    template_name = "contact/all_contacts.html"
    context_object_name = "contacts"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contacts'] = context['contacts'].filter(
            user=self.request.user)

        return context


class ContactDetails(DetailView):
    model = models.UserContacts
    template_name = "contact/contact_details.html"
    context_object_name = "cd"
