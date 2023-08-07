# django
from django.urls import re_path
from django.conf.urls import include
from django.contrib.auth.decorators import login_required

from logtoday.views import (
    IndexView, ListGoalsView, GoalsCreate, GoalsUpdate, GoalsDelete,
    ListActivitiesView, ActivityCreate, ActivityDelete, GoalsCategoryView,
    GoalsCategoryCreate, GoalsCategoryUpdate, GoalsCategoryDelete,
    ReportMonthlyStatus, ReportGoalsProgress, ListTasks, CreateTasks,
    monthly_activities, login_view, logout_view, change_password,
    DashboardView, TaskEdit, TaskDelete
)


reports_url = [
    re_path(r'^$', login_required(ReportGoalsProgress.as_view(), login_url="/"), name="reports-home"),
    re_path(r'^monthly$', login_required(ReportMonthlyStatus.as_view(), login_url="/"), name="reports-monthly"),
    re_path(r'^ajax/monthly-activities$', monthly_activities, name="monthly_activities"),
]

settings_url = [
    re_path(r'^goal-categories/$', login_required(GoalsCategoryView.as_view(), login_url="/"), name="goal-category"),
    re_path(r'^goal-category/add/$', login_required(GoalsCategoryCreate.as_view(), login_url="/"),
        name="goal-category-add"),
    re_path(r'^goal-category/(?P<pk>[-\w]+)/update/$', login_required(GoalsCategoryUpdate.as_view(), login_url="/"),
        name="goal-category-update"),
    re_path(r'^goal-category/(?P<pk>[-\w]+)/remove/$', login_required(GoalsCategoryDelete.as_view(), login_url="/"),
        name="goal-category-remove"),
    re_path(r'^change-password/$', login_required(change_password, login_url="/"), name="change-pwd"),
]

activity_urls = [
    re_path(r'^list/$', login_required(ListActivitiesView.as_view(), login_url="/"), name="activities-list"),
    re_path(r'^add/$', login_required(ActivityCreate.as_view(), login_url="/"), name="activity-add"),
    re_path(r'^(?P<pk>[-\w]+)/remove/$', login_required(ActivityDelete.as_view(), login_url="/"), name="activity-remove"),
]

goals_urls = [
    re_path(r'^$', login_required(ListGoalsView.as_view(), login_url="/"), name="goals-list"),
    re_path(r'^add/$', login_required(GoalsCreate.as_view(), login_url="/"), name="goal-create"),
    re_path(r'^(?P<pk>[-\w]+)/update/$', login_required(GoalsUpdate.as_view(), login_url="/"), name="goal-update"),
    re_path(r'^(?P<pk>[-\w]+)/remove/$', login_required(GoalsDelete.as_view(), login_url="/"), name="goal-remove"),
    re_path(r'^(?P<pk>[-\w]+)/tasks/$', login_required(ListTasks.as_view(), login_url="/"), name="tasks-list"),
    re_path(r'^(?P<pk>[-\w]+)/tasks/create$', login_required(CreateTasks.as_view(), login_url="/"), name="tasks-create"),
    re_path(r'^(?P<pk>[-\w]+)/task/(?P<task_id>[-\w]+)/update$', login_required(TaskEdit.as_view(), login_url="/"), name="task-edit"),
    re_path(r'^(?P<pk>[-\w]+)/task/(?P<task_id>[-\w]+)/remove$', login_required(TaskDelete.as_view(), login_url="/"), name="task-delete"),
]

dashboard_urls = [
    re_path(r'^$', login_required(DashboardView.as_view(), login_url="/"), name="dashboard"),
    re_path(r'^settings/', include(settings_url)),
    re_path(r'^goals/', include(goals_urls)),
    re_path(r'^activity/', include(activity_urls)),
    re_path(r'^reports/', include(reports_url)),
]

urlpatterns = [
    re_path(r'^$', IndexView.as_view(), name="index"),
    re_path(r'^login/$', login_view, name="login"),
    re_path(r'^logout/$', logout_view, name="logout"),
    re_path(r'^dashboard/', include(dashboard_urls)),
]
