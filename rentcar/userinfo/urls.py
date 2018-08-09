from django.conf.urls import url
from django.contrib import admin
from userinfo import views

urlpatterns = [
    url(r'^login/', views.signin, name='login'),
    url(r'^register/',views.register_in, name='register'),
    url(r'^reigsterin/',views.register_, name='register_in'),
    url(r'^loginin/', views.login_, name='login_in'),
    url(r'^loginout/', views.login_out, name='login_out'),
]