# TestDomClick
## Установка
Создайте clone:
```
git clone https://github.com/Ra1ze505/TestDomClick.git
```

Перейдите в корневой каталог проекта:
``` 
cd TestDomClick
```

И установите зависимости: 
```
pip install -r requirements.txt
```


Вы можете протестировать возможности проекта на предоставленной **тестовой** базе данных
(**Суперюзер**: Логин:admin Пароль:1234 **Тестовый менеджер**: Логин:ivan Пароль:TestDomClick) или удалить файл **db.sqlite3** и подключить свою базу данных в **TestDomClick/settings.py**.

Для **теста** функционала с тестовой базой данных:
```
python manage.py runserver
```

После подключения **своей или новой** базы данных:
```
python manage.py migrate
python manage.py createsuperuser
```
В случае **ошибки** удалите файл main/migrations/0001_inital.py:
```
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```
Или просто запустите команду
```
docker-compose up
```
Для активации бота необходимо заспустить файл bot.py **глобально** через python Console. Для тестирования был создан бот.
## Функционал
Данный проект позволяет принимать заявки на главной странице и в последствии в панели администрации суперюзер может назначить менеджера на эту заявку. Менеджер в своей панели администрации будет иметь доступ только к назначенным ему заявкам.
Для данного функционала необходимо создать группу с названием 'Manager' и дать группе доступ (main | Заявки | Can view Заявки, main | Заявки | Can change Заявки)
Далее добавить пользователя со статусом персонала и добавить ему группу 'Manager'.

Для выбора статуса заявки и вида заявки их необходимо также добавить через админ панель.

## Что было реализовано
- Оформление заявок
- Доступ админу к заявкам
- Добавление, изменение, удаление заявок администратором
- Список клиентов оставивших заявку
- Возможность администратору назначать менеджера и изменять статус заявки со станици листа заявок
- Доступ менеджера к редактированию заявок назначенных ему
- Ограничение для менеджера переназначить заявку другому менеджеру
- Фильтрация заявок по: статусу, дате, типу
- Привязка заявки к телеграмм боту
- Уведомление клиента о изменении статуса заявки

