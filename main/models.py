from django.db import models
from django.contrib.auth.models import User, Group, Permission




class StatusChoise(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статусы'
        verbose_name_plural = 'Статусы'



class TypeRequest(models.Model):
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.type

    class Meta:
        verbose_name = 'Виды заявок'
        verbose_name_plural = 'Виды заявок'


class Requests(models.Model):
    name = models.CharField(max_length=100)
    type = models.ForeignKey(TypeRequest, on_delete=models.CASCADE)
    request = models.TextField()
    email = models.EmailField()
    manager = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    status = models.ForeignKey(StatusChoise, on_delete=models.CASCADE, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Заявки'
        verbose_name_plural = 'Заявки'

