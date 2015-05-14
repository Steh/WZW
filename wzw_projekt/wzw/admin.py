from django.contrib import admin

from .models import Group, Expenses, Person

admin.site.register(Group)
admin.site.register(Person)
admin.site.register(Expenses)