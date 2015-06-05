from django.conf.urls import include, url, patterns
from django.contrib import admin

from wzw.views import GroupView, GroupIndexView, NewGroupView, EditGroupView, DeleteGroupView, \
    PersonView, NewPersonView, DeletePersonView, EditPersonView, \
    ExpenseView, NewExpenseView, DeleteExpenseView, EditExpenseView, \
    IndexView, impressum, about, ImpressumView, AboutView

urlpatterns = [

    # STARTSEITE, IMPRESSUM UND UEBER UNS  VIEW

    url(r'^$', IndexView.as_view()),
    url(r'^group/([0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4})/impressum/',
        ImpressumView.as_view()),
    url(r'^group//impressum/',
        impressum, name='impressum'),
    url(r'^group/([0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4})/about/',
        AboutView.as_view()),
    url(r'^group//about/',
        about, name='about'),

    # Group VIEWS
    url(r'^group/([0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4})/$',
        GroupIndexView.as_view()),
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

    # AUSGABEN VIEW
    url(r'^group/([0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4})/expense/$',
        ExpenseView.as_view()),
    url(r'^group/([0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4})/expense/new$',
        NewExpenseView.as_view()),
    url(r'^group/([0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4})/expense/edit$',
        EditExpenseView.as_view()),
    url(r'^group/([0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4}[-][0-9a-zA-Z]{4})/expense/delete$',
        DeleteExpenseView.as_view()),

    # BACKEND VIEW
    url(r'^admin/', include(admin.site.urls)),
]
