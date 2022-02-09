from audioop import reverse
from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import (
    TemplateView,
    DetailView,
    ListView,
    CreateView,
    UpdateView,
)
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy
from django.http import Http404
from django.views import generic


from . import forms
from . import models

from django.contrib.auth import get_user_model
User = get_user_model()


class Home(TemplateView):
    template_name = 'contact/home.html'


class Index(TemplateView):
    template_name = 'contact/index.html'


class UserAllContacts(LoginRequiredMixin, ListView):
    model = models.UserContactModel
    template_name = "contact/all_contacts.html"
    context_object_name = "contacts"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self):
        return models.UserContactModel.objects.filter(user=self.request.user)
        


class ContactDetails(LoginRequiredMixin,DetailView):
    model = models.UserContactModel
    template_name = "contact/contact_details.html"
    context_object_name = "cd"

    def get_queryset(self):
        return models.UserContactModel.objects.filter(user=self.request.user)


class CreateContact(LoginRequiredMixin,CreateView):
    model = models.UserContactModel
    form_class = forms.UserContactForm
    template_name = "contact/create.html"
    success_url = reverse_lazy('contact:displaycontacts')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

class UpdateContact(LoginRequiredMixin, UpdateView):
    model = models.UserContactModel
    template_name = "contact/update.html"
    form_class = forms.ContactUpdateForm
    # fields = ('firstname', 'lastname', 'nickname', 'gender', 'address', 'phone_number', 'website')
    success_url = reverse_lazy('contact:displaycontacts')
