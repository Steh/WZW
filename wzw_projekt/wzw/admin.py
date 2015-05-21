from django.contrib import admin

from .models import Group, Expenses, Person


class GroupAdmin(admin.ModelAdmin):
    list_display = ['name', 'token', 'lastLogon']
    ordering = ['name']


admin.site.register(Group, GroupAdmin)
admin.site.register(Person)
admin.site.register(Expenses)