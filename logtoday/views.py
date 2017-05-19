import os
import json
import pytz

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import (
    authenticate, login, logout, update_session_auth_hash
)
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, Template
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import (
    CreateView, UpdateView, DeleteView
)
from django.urls import reverse_lazy

from logtoday.forms import GoalsCreateForm, ActivityCreateForm
from logtoday.models import GoalsCategory, ShortTermGoals, DailyActivity


class IndexView(TemplateView):

    template_name = "login.html"


class ListGoalsView(ListView):

    template_name = "dashboard/goals_list.html"
    model = ShortTermGoals
    context_object_name = "goals"


class GoalsCreate(CreateView):

    model = ShortTermGoals
    template_name = "dashboard/goal_create_update.html"
    form_class = GoalsCreateForm


class GoalsUpdate(UpdateView):

    model = ShortTermGoals
    template_name = "dashboard/goal_create_update.html"

    fields = ['goal_desc', 'goal_target', 'goal_notes', 'goal_status']


class GoalsDelete(DeleteView):

    model = ShortTermGoals
    template_name = "dashboard/goal_remove.html"
    success_url = reverse_lazy('goals-list')


class ListActivitiesView(ListView):

    model = DailyActivity
    template_name = "dashboard/activities_list.html"
    context_object_name = "activities"
    paginate_by = 15


class ActivityCreate(CreateView):

    model = DailyActivity
    template_name = "dashboard/activity_create.html"
    form_class = ActivityCreateForm

    def form_valid(self, form):
        form.instance.activity_user = self.request.user
        return super(ActivityCreate, self).form_valid(form)


class ActivityDelete(DeleteView):

    model = DailyActivity
    template_name = "dashboard/activity_remove.html"
    success_url = reverse_lazy('activities-list')


class GoalsCategoryView(ListView):

    model = GoalsCategory
    template_name = "dashboard/goal_categories.html"
    context_object_name = "categories"


class GoalsCategoryCreate(CreateView):

    model = GoalsCategory
    template_name = "dashboard/category_create_update.html"

    fields = ['category_value', 'category_name']


class GoalsCategoryUpdate(UpdateView):

    model = GoalsCategory
    template_name = "dashboard/category_create_update.html"

    fields = ['category_value', 'category_name']


class GoalsCategoryDelete(DeleteView):

    model = GoalsCategory
    template_name = "dashboard/category_remove.html"
    success_url = reverse_lazy('goal-category')


class ReportMonthlyStatus(TemplateView):
    """
    Monthly Status teport View
    """
    template_name = "dashboard/report_status.html"
    context_object_name = "activities"


def login_view(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    redirect_url = "index"
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        redirect_url = "goals-list"
        try:
            with open(os.path.join('makegoalsdaily', 'app-config.json')) as data_file:
                data = json.load(data_file)
            if data.get('timezone') and data.get('timezone') in pytz.common_timezones:
                request.session['django_timezone'] = data['timezone']
        except:
            # log error
            pass
    else:
        messages.add_message(request, messages.ERROR, "Invalid Credentials")
    return HttpResponseRedirect(reverse_lazy(redirect_url))


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse_lazy("index"))


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('index')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/change_password.html', {
        'form': form
    })


def monthly_activities(request):
    """
    Monthly Activities AJAX View
    """
    if request.is_ajax():
        post_params = request.POST.dict()
        if post_params.get('month_year'):
            context = Context(
                {'META': request.META,
                 'month_year': post_params['month_year']}
            )
            template_string = """
                {% load monthly_activities from custom_tags %}
                {% monthly_activities month_year %}
            """
            return HttpResponse(Template(template_string).render(context))
    return HttpResponse(status=500)
