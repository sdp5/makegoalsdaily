from django.shortcuts import render

# Create your views here.
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.urls import reverse


class IndexView(TemplateView):

    template_name = "login.html"


class DashboardView(TemplateView):

    template_name = "dashboard/home.html"

    def get_context_data(self, **kwargs):
        """
        Build context data
        """
        context_data = super(DashboardView, self).get_context_data(**kwargs)
        context_data["user"] = self.request.user
        return context_data


def login_view(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    redirect_url = "index"
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        redirect_url = "dashboard"
    else:
        messages.add_message(request, messages.ERROR, "Invalid Credentials")
    return HttpResponseRedirect(reverse(redirect_url))


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))
