from django.conf.urls import include, url
from django.contrib import admin

from wzw.views import GroupView, GroupIndexView, NewGroupView, EditGroupView, DeleteGroupView, \
    PersonView, NewPersonView, DeletePersonView, EditPersonView, \
    ExpenseView, NewExpenseView, DeleteExpenseView, EditExpenseView, \
    IndexView

urlpatterns = [
    # Group VIEWS
    url(r'^group/([0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4})/$',
        GroupIndexView.as_view()),

    # url(r'^group/([0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4})/$',
    #    GroupIndex.as_view()),

    # Group VIEWS
    url(r'^group/([0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4})/group/$',
        GroupView.as_view()),
    url(r'^group/([0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4})/group/new$',
        NewGroupView.as_view()),
    url(r'^group/([0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4})/group/edit$',
        EditGroupView.as_view()),
    url(r'^group/([0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4})/group/delete$',
        DeleteGroupView.as_view()),

    # PERSONEN VIEW
    url(r'^group/([0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4})/person/$',
        PersonView.as_view()),
    url(r'^group/([0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4})/person/new$',
        NewPersonView.as_view()),
    url(r'^group/([0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4})/person/edit$',
        EditPersonView.as_view()),
    url(r'^group/([0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4})/person/delete$',
        DeletePersonView.as_view()),

    # AUSGABEN SEITEN
    url(r'^group/([0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4})/expense/$',
        ExpenseView.as_view()),
    url(r'^group/([0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4})/expense/new$',
        NewExpenseView.as_view()),
    url(r'^group/([0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4})/expense/edit$',
        EditExpenseView.as_view()),
    url(r'^group/([0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4})/expense/delete$',
        DeleteExpenseView.as_view()),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', IndexView.as_view()),
]
