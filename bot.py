import telebot
from django.conf import settings

from main.models import Requests

bot = telebot.TeleBot(settings.API)


@bot.message_handler(func=lambda message: True)
def activate(message):
    qusetion = message.text
    qs = qusetion.split()
    if qs[0] == '/start':
        if len(qs) == 2:
            token = str(qs[1])
            try:
                obj = Requests.objects.get(TOKEN=token)
            except Requests.DoesNotExist:
                obj = None
                bot.reply_to(message, 'Не удалось привязать бота')
            if obj:
                obj.update(bot_id=message.chat.id)
                bot.reply_to(message, 'Вы привязали бота, теперь вы будете получать уведомления о сотоянии вашей заявки')


def main():
    bot.polling()


if __name__ == '__main__':
    main()
