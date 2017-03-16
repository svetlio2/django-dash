from django.conf.urls import url

from dash import views


urlpatterns = [
    # Paste dashboard entry
    url(r'^entry/paste/(?P<placeholder_uid>[\w_]+)/(?P<workspace>[\w_\-]+)/pos/(?P<position>\d+)/$', \
        views.paste_dashboard_entry, name='dash.paste_dashboard_entry'),
    url(r'^entry/paste/(?P<placeholder_uid>[\w_]+)/pos/(?P<position>\d+)/$', views.paste_dashboard_entry, \
        name='dash.paste_dashboard_entry'),

    # Cut dashboard entry
    url(r'^entry/cut/(?P<entry_id>\d+)/$', views.cut_dashboard_entry, \
        name='dash.cut_dashboard_entry'),

    # Copy dashboard entry
    url(r'^entry/copy/(?P<entry_id>\d+)/$', views.copy_dashboard_entry, \
        name='dash.copy_dashboard_entry'),

    # Add dashboard entry.
    url(r'^entry/add/(?P<placeholder_uid>[\w_]+)/(?P<plugin_uid>[\w_\-]+)/ws/(?P<workspace>[\w_\-]+)/pos/(?P<position>\d+)/$', \
        views.add_dashboard_entry, name='dash.add_dashboard_entry'),
    url(r'^entry/add/(?P<placeholder_uid>[\w_]+)/(?P<plugin_uid>[\w_\-]+)/ws/(?P<workspace>[\w_\-]+)/$', \
        views.add_dashboard_entry, name='dash.add_dashboard_entry'),
    url(r'^entry/add/(?P<placeholder_uid>[\w_]+)/(?P<plugin_uid>[\w_\-]+)/pos/(?P<position>\d+)/$', \
        views.add_dashboard_entry, name='dash.add_dashboard_entry'),
    url(r'^entry/add/(?P<placeholder_uid>[\w_]+)/(?P<plugin_uid>[\w_\-]+)/$', views.add_dashboard_entry, \
        name='dash.add_dashboard_entry'),

    # Edit dashboard entry.
    url(r'^entry/edit/(?P<entry_id>\d+)/$', views.edit_dashboard_entry, \
        name='dash.edit_dashboard_entry'),

    # Delete dashboard entry.
    url(r'^entry/delete/(?P<entry_id>\d+)/$', views.delete_dashboard_entry, \
        name='dash.delete_dashboard_entry'),

    # ********************** Edit dashboard
    # Edit dashboard.
    url(r'^edit/(?P<workspace>[\w_\-]+)/$', views.edit_dashboard, \
        name='dash.edit_dashboard'),
    url(r'^edit/$', views.edit_dashboard, name='dash.edit_dashboard'),

    # ********************** Widgets for dashboard entries
    url(r'^plugin-widgets/(?P<placeholder_uid>[\w_]+)/(?P<workspace>[\w_\-]+)/pos/(?P<position>\d+)/$', \
        views.plugin_widgets, name='dash.plugin_widgets'),
    # Workspace should not be named `pos`. Add check. TODO.
    url(r'^plugin-widgets/(?P<placeholder_uid>[\w_]+)/pos/(?P<position>\d+)/$', \
        views.plugin_widgets, \
        name='dash.plugin_widgets'),
    url(r'^plugin-widgets/(?P<placeholder_uid>[\w_]+)/(?P<workspace>[\w_\-]+)/$', \
        views.plugin_widgets, \
        name='dash.plugin_widgets'),
    url(r'^plugin-widgets/(?P<placeholder_uid>[\w_]+)/$', views.plugin_widgets, \
        name='dash.widgets'),

    # ********************** Dashboard workspace
    # List workspaces.
    url(r'^workspaces/(?P<workspace>[\w_\-]+)/$', views.dashboard_workspaces, \
        name='dash.dashboard_workspaces'),
    url(r'^workspaces/$', views.dashboard_workspaces, \
        name='dash.dashboard_workspaces'),

    # Create dashboard workspace.
    url(r'^workspace/create/$', views.create_dashboard_workspace, \
        name='dash.create_dashboard_workspace'),

    # Edit dashboard workspace.
    url(r'^workspace/edit/(?P<workspace_id>\d+)/$', \
        views.edit_dashboard_workspace, name='dash.edit_dashboard_workspace'),

    # Delete dashboard workspace.
    url(r'^workspace/delete/(?P<workspace_id>\d+)/$',  \
        views.delete_dashboard_workspace, \
        name='dash.delete_dashboard_workspace'),

    # Clone dashboard workspace.
    url(r'^workspace/clone/(?P<workspace_id>\d+)/$', \
        views.clone_dashboard_workspace, \
        name='dash.clone_dashboard_workspace'),

    # View dashboard workspace.
    url(r'^workspace/(?P<workspace>[\w_\-]+)/$', views.dashboard, \
        name='dash.dashboard'),

    # Edit dashboard settings.
    url(r'^settings/edit/$', views.edit_dashboard_settings, \
        name='dash.edit_dashboard_settings'),

    # View default dashboard (no workspace selected == default workspace used).
    url(r'^$', views.dashboard, name='dash.dashboard'),
]
