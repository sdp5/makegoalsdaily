from django.shortcuts import render

# Create your views here.
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import (
    CreateView, UpdateView, DeleteView
)
from django.urls import reverse_lazy

from logtoday.models import ShortTermGoals


class IndexView(TemplateView):

    template_name = "login.html"


class ListGoalsView(ListView):

    template_name = "dashboard/goals_list.html"
    model = ShortTermGoals

    def get_context_data(self, **kwargs):
        """
        Build context data
        """
        context_data = super(ListGoalsView, self).get_context_data(**kwargs)
        context_data["user"] = self.request.user
        return context_data


class GoalsCreate(CreateView):

    model = ShortTermGoals
    template_name = "dashboard/goal_create_update.html"

    fields = ['goal_slug', 'goal_desc', 'goal_target', 'goal_category']


class GoalsUpdate(UpdateView):

    model = ShortTermGoals
    template_name = "dashboard/goal_create_update.html"

    fields = ['goal_desc', 'goal_target', 'goal_notes', 'goal_status']


class GoalsDelete(DeleteView):

    model = ShortTermGoals
    template_name = "dashboard/goal_remove.html"
    success_url = reverse_lazy('goals-list')


def login_view(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    redirect_url = "index"
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        redirect_url = "goals-list"
    else:
        messages.add_message(request, messages.ERROR, "Invalid Credentials")
    return HttpResponseRedirect(reverse_lazy(redirect_url))


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse_lazy("index"))
