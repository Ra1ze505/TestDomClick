from django.db import models
from django.contrib.auth.models import User, Group, Permission


class StatusChoise(models.Model):
    """Статусы заявки"""
    title = models.CharField(max_length=100, verbose_name='Название')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статусы'
        verbose_name_plural = 'Статусы'


class TypeRequest(models.Model):
    """Типы заявок"""
    type = models.CharField(max_length=100, verbose_name='Тип')

    def __str__(self):
        return self.type

    class Meta:
        verbose_name = 'Виды заявок'
        verbose_name_plural = 'Виды заявок'


class Requests(models.Model):
    """Заявки"""
    name = models.CharField(max_length=100, verbose_name='Имя')
    type = models.ForeignKey(TypeRequest, on_delete=models.CASCADE, verbose_name='Тип заявки')
    request = models.TextField(verbose_name='Заявка')
    email = models.EmailField()
    manager = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE, verbose_name='Менеджер')
    status = models.ForeignKey(StatusChoise, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Статус')
    bot_id = models.CharField(max_length=100, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated = models.DateTimeField(auto_now=True, verbose_name='Изменено')
    TOKEN = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Заявки'
        verbose_name_plural = 'Заявки'


class UserRequest(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Пользователи оформившие заявку'
        verbose_name_plural = 'Пользователи оформившие заявку'
