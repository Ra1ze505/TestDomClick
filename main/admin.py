from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django import forms
from .models import *


class ManagerChoiseField(forms.ModelChoiceField):
    pass


class RequestAdmin(admin.ModelAdmin):
    list_display = ['name', 'type', 'manager', 'status', 'created', 'updated']
    list_filter = ['type', 'status', 'created', 'updated']
    list_editable = ['status', 'manager']

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'manager':
            return ManagerChoiseField(User.objects.filter(groups__name='Manager'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(manager=request.user)

    def get_fields(self, request, obj=None):
        fields = super(RequestAdmin, self).get_fields(request, obj)
        if request.user.is_superuser:
            fields += ('manager',)

        return fields


admin.site.register(StatusChoise)
admin.site.register(TypeRequest)
admin.site.register(Requests, RequestAdmin)