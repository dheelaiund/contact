from django.urls import re_path, include
from . import views

app_name = 'contact'

urlpatterns = [
    re_path(r'^index/$', views.Index.as_view(), name='index'),
    re_path(r"display/$", views.UserAllContacts.as_view(),
            name="displaycontacts"),
    re_path(r"^details/(?P<username>[-\w]+)/(?P<pk>\d+)/$",
            views.ContactDetails.as_view(), name="contactdetails"),
    re_path(r"create/$", views.CreateContact.as_view(), name="create"),

]
