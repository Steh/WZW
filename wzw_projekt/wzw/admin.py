from django.contrib import admin

from .models import Group, Expense, Person


class GroupAdmin(admin.ModelAdmin):
    list_display = ['name', 'token', 'lastLogon']
    ordering = ['name']


admin.site.register(Group, GroupAdmin)
admin.site.register(Person)
admin.site.register(Expense)
