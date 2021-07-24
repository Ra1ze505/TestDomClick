from django.contrib import admin
from django import forms

from .models import *


class ManagerChoiseField(forms.ModelChoiceField):
    pass


class RequestAdmin(admin.ModelAdmin):
    """Настройка дисплея заявок"""
    list_display = ('name', 'type', 'manager', 'status', 'created', 'updated')
    list_filter = ('type', 'status', 'created', 'updated')
    list_editable = ['status', 'manager']

    def save_model(self, request, obj, form, change):
        """Отслеживаем изменение статуса для уведомления пользователя"""
        update_fields = []
        if change:
            if form.initial['status'] != form.cleaned_data['status']:
                update_fields.append('status')

        obj.save(update_fields=update_fields)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        """Ограничиние выбора менеджера для заявки"""
        if db_field.name == 'manager':
            if request.user.is_superuser:
                return ManagerChoiseField(User.objects.filter(groups__name='Manager'))
            else:
                return ManagerChoiseField(User.objects.filter(username=request.user))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        """Ограничение отображения заявок для менеджера"""
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(manager=request.user)


class UserRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')


admin.site.register(StatusChoise)
admin.site.register(TypeRequest)
admin.site.register(Requests, RequestAdmin)
admin.site.register(UserRequest, UserRequestAdmin)
