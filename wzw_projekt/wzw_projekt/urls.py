"""wzw_projekt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

from wzw.views import *

urlpatterns = [
    url(r'^group/([0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4})/$', GroupIndex.as_view()),
    url(r'^group/([0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4})/editGroup/$', GroupView.as_view()),

    # Group VIEWS
    url(r'^group/([0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4})/group/$', GroupView.as_view()),
    url(r'^group/([0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4})/group/new$', NewGroupView.as_view()),
    url(r'^group/([0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4})/group/edit$',
        EditGroupView.as_view()),
    url(r'^group/([0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4})/group/delete$',
        DeleteGroupView.as_view()),

    # PERSONEN VIEW
    url(r'^group/([0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4})/person/$', PersonView.as_view()),
    url(r'^group/([0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4})/person/new$',
        NewPersonView.as_view()),
    url(r'^group/([0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4})/person/edit$',
        EditPersonView.as_view()),
    url(r'^group/([0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4})/person/delete$',
        DeletePersonView.as_view()),

    # AUSGABEN SEITEN
    url(r'^group/([0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4})/expense/$', ExpenseView.as_view()),
    url(r'^group/([0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4})/expense/new$',
        NewExpenseView.as_view()),
    url(r'^group/([0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4})/expense/edit$',
        EditExpenseView.as_view()),
    url(r'^group/([0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4})/expense/delete$',
        DeleteExpenseView.as_view()),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', Index.as_view()),
]