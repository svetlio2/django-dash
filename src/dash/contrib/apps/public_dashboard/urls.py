from django.conf.urls import url

from dash.contrib.apps.public_dashboard import views

urlpatterns = [
    # View public dashboard workspace.
    url(r'^(?P<username>[\w_\-]+)/(?P<workspace>[\w_\-]+)/$', views.public_dashboard, name='dash.public_dashboard'),

    # View public dashboard (no workspace selected == default workspace used).
    url(r'^(?P<username>[\w_\-]+)/$', views.public_dashboard, name='dash.public_dashboard'),
]
