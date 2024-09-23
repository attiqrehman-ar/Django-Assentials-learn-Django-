from django.shortcuts import render
# from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class LogoutInterfaceView(LogoutView):
    template_name="home/logout_home.html"
    

class LoginInterfaceView(LoginView):
    template_name="home/login.html"


class HomeView(TemplateView):
    template_name="home/welcome.html"
    extra_content= {'today': datetime.today()}


class AuthorizedView(LoginRequiredMixin, TemplateView):
    template_name= "home/authorized.html"
    login_url="/admin"
