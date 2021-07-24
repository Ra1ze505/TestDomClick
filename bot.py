import telebot
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

from main.models import Requests


bot = telebot.TeleBot(settings.API)


# def my_handler(sender, **kwargs):
#     print('hi')
#     chat_id = str(sender.bot_id)
#     status = str(sender.status)
#     bot.send_message(chat_id, 'Ваша заявка '+ status)
#
#
# post_save.connect(my_handler, sender=Requests)

@bot.message_handler(func=lambda message: True)
def activate(message):
    qusetion = message.text
    qs = qusetion.split()
    if qs[0] == '/start':
        token = str(qs[1])
        try:
            obj = Requests.objects.filter(TOKEN=token)
        except Requests.DoesNotExist:
            obj = None
            bot.reply_to(message, 'Не удалось привязать бота')
        if obj:
            obj.update(bot_id=message.chat.id)
            bot.reply_to(message, 'Вы привязали бота, теперь вы будете получать уведомления о сотоянии вашей заявки')


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'hi')


def main():
    bot.polling()

if __name__ == '__main__':
    main()
