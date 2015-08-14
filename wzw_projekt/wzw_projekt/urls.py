# -*- coding: utf-8 -*-

from django.conf.urls import include, url
from django.contrib import admin

from wzw.views import GroupView, GroupIndexView, NewGroupView, EditGroupView, \
    PersonView, NewPersonView, DeletePersonView, EditPersonView, \
    ExpenseView, NewExpenseView, IndexView, ImpressumView, AboutView, ReportView, ExpenseViewDetails, ExpenseViewEdit, ExpenseViewDelete

urlpatterns = [

    # STARTSEITE, IMPRESSUM UND UEBER UNS  VIEW
    url(r'^$', IndexView.as_view()),
    url(r'^impressum/',
        ImpressumView.as_view()),
    url(r'^about/',
        AboutView.as_view()),

    # Group VIEWS
    url(r'^group/([0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4})/$',
        GroupIndexView.as_view(),
        name='startseite',),
    url(r'^group/([0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4})/group/$',
        GroupView.as_view(),
        name='group-details',),
    url(r'^group/([0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4})/group/new$',
        NewGroupView.as_view(),
        name='group-new',),
    url(r'^group/([0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4})/group/edit$',
        EditGroupView.as_view(),
        name='group-edit',),
    # url(r'^group/([0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4})/group/delete$',
    #     DeleteGroupView.as_view(),
    #     name='group-delete',),

    # PERSONEN VIEW
    url(r'^group/([0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4})/person/$',
        PersonView.as_view(),
        name='person-details',),
    url(r'^group/([0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4})/person/new$',
        NewPersonView.as_view(),
        name='group-details',),
    url(r'^group/([0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4})/person/edit$',
        EditPersonView.as_view(),
        name='person-edit',),
    url(r'^group/([0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4})/person/delete$',
        DeletePersonView.as_view(),
        name='person-delete',),

    # AUSGABEN VIEW
    url(r'^group/([0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4})/expense/$',
        ExpenseView.as_view(),
        name='expense-details',),
    url(r'^group/([0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4})/expense/new$',
        NewExpenseView.as_view(),
        name='expense-new',),

    url(r'^group/([0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4})/expense/([0-9]+)/$',
        ExpenseViewDetails.as_view(),
        name='expense-details-id',),

    url(r'^group/([0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4})/expense/([0-9]+)/edit/$',
        ExpenseViewEdit.as_view(),
        name='expense-details-id',),

    url(r'^group/([0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4})/expense/([0-9]+)/delete/$',
        ExpenseViewDelete.as_view(),
        name='expense-details-id',),

    # REPORT VIEW
    url(r'^group/([0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4})/report/$',
        ReportView.as_view()),

    # BACKEND VIEW
    url(r'^admin/', include(admin.site.urls)),
]
