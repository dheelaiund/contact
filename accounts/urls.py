from django.urls import re_path,include
from django.contrib.auth.decorators import login_required
from . import views


app_name = 'accounts'

urlpatterns = [
    re_path(r'^register/$',views.RegisterUser.as_view(), name = 'registeruser'),
    re_path(r'^login/$',views.LoginUser.as_view(), name = 'loginuser'),
    re_path(r'^logout/$',views.LogoutUser.as_view(), name = 'logoutuser'),
]
