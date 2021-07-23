# TestDomClick
## Установка
Создайте clone:
`` ''
git clone https://github.com/Ra1ze505/TestDomClick.git
`` ''
Перейдите в корневой каталог проекта:
`` ''
cd TestDomClick
`` ''
Вы можете протестировать возможности проекта на предоставленной тестовой базе данных(Суперюзер: [Логин:admin Пароль:1234]) или удалить файл db.sqlite3 и подключить свою базу данных в settings.py
Для теста функционала с тестовой базой данных:
`` ''
python manage.py runserver
`` ''
После подключения своей или новой базы данных:
`` ''
python manage.py migrate
`` ''
В случае ошибки удалите файл main/migrations/0001_inital.py:
`` ''
python manage.py makemigrations
python manage.py migrate
`` ''
## Функционал
Данный проект позволяет принимать заявки на главной странице и в последствии в панели администрации суперюзер может назначить менеджера на эту заявку. Менеджер в своей панели администрации будет иметь доступ только к назначенным ему заявкам.
Для данного функционала необходимо создать группу с названием 'Manager' и дать группе доступ (main | Заявки | Can view Заявки, main | Заявки | Can change Заявки)
Далее добавить пользователя со статусом персонала и добавить ему группу 'Manager'
