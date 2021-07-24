from django.conf import settings
from django.shortcuts import render, redirect
from django.db import IntegrityError
from uuid import uuid4
from django.db.models.signals import post_save
import requests

from .forms import *


def main(request):
    if request.method == 'POST':
        form = Request(request.POST)
        if form.is_valid():
            TOKEN = str(uuid4())
            cd = form.cleaned_data
            r = Requests(name=cd['name'],
                         type=cd['type'],
                         request=cd['request'],
                         email=cd['email'],
                         TOKEN=TOKEN)
            r.save()
            Requests.objects.update()
            try:
                UserRequest.objects.create(name=cd['name'], email=cd['email'])
            except IntegrityError:
                pass
            return redirect(f'https://t.me/Test_my_telegram_simple_bot?start={TOKEN}')

    else:
        form = Request()
    return render(request, 'main/main.html', {'form': form})


"""Уведомляем пользователя о статусе заявки"""
def my_handler(sender, update_fields, instance, **kwargs):
    sta = 'status'
    print(instance.status)
    if sta in update_fields:
        status = instance.status
        api_key = settings.API
        chat_id = str(instance.bot_id)
        text = 'Статус вашей заявки изменился: ' + str(status)
        url = f'https://api.telegram.org/bot{api_key}/sendMessage'
        params = {
            'chat_id': chat_id,
            'text': text,
        }
        return requests.get(url, params=params).json()

post_save.connect(my_handler, sender=Requests)
