# 🐈 Kittygram API

![Python](https://img.shields.io/badge/python-3.9-blue.svg)
![Django](https://img.shields.io/badge/django-3.2-green.svg)
![DRF](https://img.shields.io/badge/DRF-3.12-red.svg)

**Kittygram** — это социальная сеть для любителей котиков. Через наш API пользователи могут регистрировать питомцев, фиксировать их достижения и следить за их возрастом в реальном времени.

---

## 🛠 Технологический стек

* **Язык:** Python 3.9
* **Фреймворк:** Django + Django REST Framework (DRF)
* **Аутентификация:** Djoser (JWT + Bearer Token)
* **База данных:** SQLite (локальная разработка)
* **Документация:** Swagger & ReDoc

---

## 🚀 Как запустить проект (Локально)

### 1. Клонирование и переход в папку
```bash
git clone https://github.com/BBBounc/kittygramMakatrovVD.git
cd kittygramMakatrovVD
```

### 2. Настройка виртуального окружения
Это создаст изолированную среду для проекта, чтобы зависимости не конфликтовали с системными.

**Для Windows:**
```bash
python -m venv venv
source venv/Scripts/activate
```

**Для Linux / macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Установка зависимостей
```bash
pip install --upgrade pip
pip install -r requirements.txt
pip install python-dotenv
```

### 4. Настройка окружения (`.env`)
Создайте файл `.env` в корневом каталоге проекта. Это необходимо для безопасности ваших данных.

**Содержимое `.env`:**
```env
SECRET_KEY=django-insecure-ваша-секретная-строка
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
```

---

## 💾 Работа с базой данных

Чтобы подготовить таблицы в SQLite и запустить сервер:

1.  **Выполнение миграций:**
    ```bash
    python manage.py migrate
    ```
2.  **Создание администратора (по желанию):**
    ```bash
    python manage.py createsuperuser
    ```
3.  **Запуск сервера:**
    ```bash
    python manage.py runserver
    ```
    Проект будет доступен по адресу: `http://127.0.0.1:8000/`

---

## 📡 Основные эндпоинты API

| Метод | Эндпоинт | Описание |
| :--- | :--- | :--- |
| **POST** | `/auth/users/` | Регистрация нового пользователя |
| **POST** | `/auth/jwt/create/` | Получение JWT-токена (Login) |
| **GET** | `/cats/` | Список всех котиков |
| **POST** | `/cats/` | Добавление котика (нужен токен) |
| **PATCH** | `/cats/{id}/` | Частичное обновление данных |
| **DELETE** | `/cats/{id}/` | Удаление котика |
| **GET** | `/achievements/` | Список всех достижений в системе |

---

## 🧪 Примеры запросов (JSON)

**Создание кота с привязкой достижения (ID: 1):**
```json
{
    "name": "Борис",
    "color": "Gray",
    "birth_year": 2021,
    "achievements": [1]
}
```

---

## 🛡 Безопасность и Валидация
* **JWT Auth:** Доступ к созданию и редактированию котиков есть только у авторизованных пользователей.
* **Owner Only:** Редактировать и удалять котика может только тот пользователь, который его добавил.
* **Business Logic:** Реализована проверка года рождения (не старше 40 лет) и уникальности имени кота для одного владельца.


**Разработчик:** [Владислав Макатров](https://github.com/BBBounc)  
**Год:** 2026