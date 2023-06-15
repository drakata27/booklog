from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect
from typing import Any

class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'home/signup.html'
    success_url = '/workouts'

    def get(self, request: HttpRequest, *args: str, **kwargs: Any):
        if self.request.user.is_authenticated:
            return redirect('workouts_list')
        return super().get(request, *args, **kwargs)

class LogoutInterfaceView(LogoutView):
    template_name = 'home/logout.html'

class LoginInterfaceView(LoginView):
    template_name = 'home/login.html'

class HomeView(TemplateView):
    template_name = 'home/welcome.html'