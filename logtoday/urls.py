# django
from django.conf.urls import url, include
from logtoday.views import IndexView, DashboardView, login_view, logout_view
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^$', IndexView.as_view(), name="index"),
    url(r'^login/$', login_view, name="login"),
    url(r'^logout/$', logout_view, name="logout"),
    url(r'^dashboard/$', login_required(
        DashboardView.as_view(), login_url="/"
    ), name="dashboard"),
]
