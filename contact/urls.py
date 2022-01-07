from django.urls import re_path,include
from . import views

app_name = 'contact'

urlpatterns = [
    re_path(r'^index/$', views.Index.as_view(), name = 'index'),
    re_path(r'^display/$', views.Display.as_view(), name = 'display'),
]
