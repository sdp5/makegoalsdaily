# django
from django.conf.urls import url, include
from logtoday.views import (
    IndexView, ListGoalsView, GoalsCreate, GoalsUpdate, GoalsDelete, login_view, logout_view
)
from django.contrib.auth.decorators import login_required


dashboard_urls = [
    url(r'^$', login_required(ListGoalsView.as_view(), login_url="/"), name="goals-list"),
    url(r'^goal/add/$', login_required(GoalsCreate.as_view(), login_url="/"), name="goal-create"),
    url(r'^goal/(?P<pk>[-\w]+)/update/$', login_required(GoalsUpdate.as_view(), login_url="/"), name="goal-update"),
    url(r'^goal/(?P<pk>[-\w]+)/remove/$', login_required(GoalsDelete.as_view(), login_url="/"), name="goal-remove"),
]

urlpatterns = [
    url(r'^$', IndexView.as_view(), name="index"),
    url(r'^login/$', login_view, name="login"),
    url(r'^logout/$', logout_view, name="logout"),
    url(r'^dashboard/', include(dashboard_urls)),
]
