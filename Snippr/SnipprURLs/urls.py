from django.urls import path, re_path
from SnipprURLs import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.shortcuts import redirect
from django.views.generic import RedirectView


urlpatterns = [
    # path('user/', views.user, name='user'),
    # path('snippets/', views.snippets, name='snippets'),
    # path('snippets/<int:snippet_id>/', views.singlesnippet, name='singlesnippet'),
    path("", views.index, name="index"),
    path("login", views.login, name="login"),
    path("logout", views.logout, name="logout"),
    path("callback", views.callback, name="callback"),
]

urlpatterns += staticfiles_urlpatterns()