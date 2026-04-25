Kittygram API 🐈
Проект «Kittygram» — это REST API сервис для социальной сети любителей кошек. Позволяет регистрировать профили, добавлять питомцев, управлять их достижениями и автоматически рассчитывать их возраст.

Технологии
Python 3.9

Django 3.2

Django REST Framework

Djoser (JWT Authentication)

SQLite (База данных)

Как запустить проект
1. Подготовка
Клонируйте репозиторий и перейдите в папку проекта:

Bash
git clone <ссылка_на_ваш_репозиторий>
cd kittygram2-master
2. Настройка виртуального окружения
Для Windows:

Bash
python -m venv venv
source venv/Scripts/activate
Для Linux / macOS:

Bash
python3 -m venv venv
source venv/bin/activate
3. Установка зависимостей
Bash
pip install --upgrade pip
pip install -r requirements.txt
pip install python-dotenv
4. Настройка окружения
Создайте файл .env в корне проекта (рядом с manage.py):

Bash
# Windows
copy .env.example .env

# Linux/macOS
cp .env.example .env
Заполните .env своими данными (SECRET_KEY, DEBUG=True).

5. Запуск базы данных и сервера
Выполните миграции, чтобы создать таблицы в SQLite, и запустите проект:

Bash
python manage.py migrate
python manage.py runserver
Сервер будет доступен по адресу: http://127.0.0.1:8000/

Как работать с API через Postman
Регистрация: POST /auth/users/ (передать username и password).

Логин: POST /auth/jwt/create/ (получить access токен).

Добавление кота: POST /cats/. В заголовках (Headers) добавьте Authorization: Bearer <ваш_токен>.

Чтобы привязать ачивку, передайте её ID: "achievements": [1].

Редактирование: PATCH /cats/{id}/ — можно изменить имя или список достижений.

Удаление: DELETE /cats/{id}/.

Особенности реализации
Автоматизация: Поле owner (владелец) подставляется автоматически из данных токена при создании кота.

Валидация: Нельзя создать кота с годом рождения из будущего или старше 40 лет.

Уникальность: У одного пользователя не может быть двух котов с одинаковым именем.

Разработчик: Владислав Макатров