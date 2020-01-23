# django
from django.conf.urls import url, include
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
    url(r'^$', login_required(ReportMonthlyStatus.as_view(), login_url="/"), name="reports-home"),
    url(r'^ajax/monthly-activities$', monthly_activities, name="monthly_activities"),
    url(r'^progress$', login_required(ReportGoalsProgress.as_view(), login_url="/"), name="reports-progress"),
]

settings_url = [
    url(r'^goal-categories/$', login_required(GoalsCategoryView.as_view(), login_url="/"), name="goal-category"),
    url(r'^goal-category/add/$', login_required(GoalsCategoryCreate.as_view(), login_url="/"),
        name="goal-category-add"),
    url(r'^goal-category/(?P<pk>[-\w]+)/update/$', login_required(GoalsCategoryUpdate.as_view(), login_url="/"),
        name="goal-category-update"),
    url(r'^goal-category/(?P<pk>[-\w]+)/remove/$', login_required(GoalsCategoryDelete.as_view(), login_url="/"),
        name="goal-category-remove"),
    url(r'^change-password/$', login_required(change_password, login_url="/"), name="change-pwd"),
]

activity_urls = [
    url(r'^list/$', login_required(ListActivitiesView.as_view(), login_url="/"), name="activities-list"),
    url(r'^add/$', login_required(ActivityCreate.as_view(), login_url="/"), name="activity-add"),
    url(r'^(?P<pk>[-\w]+)/remove/$', login_required(ActivityDelete.as_view(), login_url="/"), name="activity-remove"),
]

goals_urls = [
    url(r'^$', login_required(ListGoalsView.as_view(), login_url="/"), name="goals-list"),
    url(r'^add/$', login_required(GoalsCreate.as_view(), login_url="/"), name="goal-create"),
    url(r'^(?P<pk>[-\w]+)/update/$', login_required(GoalsUpdate.as_view(), login_url="/"), name="goal-update"),
    url(r'^(?P<pk>[-\w]+)/remove/$', login_required(GoalsDelete.as_view(), login_url="/"), name="goal-remove"),
    url(r'^(?P<pk>[-\w]+)/tasks/$', login_required(ListTasks.as_view(), login_url="/"), name="tasks-list"),
    url(r'^(?P<pk>[-\w]+)/tasks/create$', login_required(CreateTasks.as_view(), login_url="/"), name="tasks-create"),
    url(r'^(?P<pk>[-\w]+)/task/(?P<task_id>[-\w]+)/update$', login_required(TaskEdit.as_view(), login_url="/"), name="task-edit"),
    url(r'^(?P<pk>[-\w]+)/task/(?P<task_id>[-\w]+)/remove$', login_required(TaskDelete.as_view(), login_url="/"), name="task-delete"),
]

dashboard_urls = [
    url(r'^$', login_required(DashboardView.as_view(), login_url="/"), name="dashboard"),
    url(r'^settings/', include(settings_url)),
    url(r'^goals/', include(goals_urls)),
    url(r'^activity/', include(activity_urls)),
    url(r'^reports/', include(reports_url)),
]

urlpatterns = [
    url(r'^$', IndexView.as_view(), name="index"),
    url(r'^login/$', login_view, name="login"),
    url(r'^logout/$', logout_view, name="logout"),
    url(r'^dashboard/', include(dashboard_urls)),
]
