# django
from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required

from logtoday.views import (
    IndexView, ListGoalsView, GoalsCreate, GoalsUpdate, GoalsDelete,
    ListActivitiesView, ActivityCreate, ActivityDelete,
    login_view, logout_view, change_password
)

activity_urls = [
    url(r'^list/$', login_required(ListActivitiesView.as_view(), login_url="/"), name="activities-list"),
    url(r'^add/$', login_required(ActivityCreate.as_view(), login_url="/"), name="activity-add"),
    url(r'^(?P<pk>[-\w]+)/remove/$', login_required(ActivityDelete.as_view(), login_url="/"), name="activity-remove"),
]

goals_urls = [
    url(r'^add/$', login_required(GoalsCreate.as_view(), login_url="/"), name="goal-create"),
    url(r'^(?P<pk>[-\w]+)/update/$', login_required(GoalsUpdate.as_view(), login_url="/"), name="goal-update"),
    url(r'^(?P<pk>[-\w]+)/remove/$', login_required(GoalsDelete.as_view(), login_url="/"), name="goal-remove"),
]

dashboard_urls = [
    url(r'^$', login_required(ListGoalsView.as_view(), login_url="/"), name="goals-list"),
    url(r'^change-password$', login_required(change_password, login_url="/"), name="change-pwd"),
    url(r'^goal/', include(goals_urls)),
    url(r'^activity/', include(activity_urls)),
]

urlpatterns = [
    url(r'^$', IndexView.as_view(), name="index"),
    url(r'^login/$', login_view, name="login"),
    url(r'^logout/$', logout_view, name="logout"),
    url(r'^dashboard/', include(dashboard_urls)),
]
