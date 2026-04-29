
# 🐾 Котошеринг: Kittygram 2.0

![Python](https://img.shields.io/badge/python-3.9-blue.svg)
![Django](https://img.shields.io/badge/django-4.2-green.svg)
![Docker](https://img.shields.io/badge/docker-ready-blue.svg)

**Котошеринг** — это не просто социальная сеть для котиков, а цифровая экосистема рационального потребления. Пользователи могут вести учет питомцев и обмениваться излишками кормов, медикаментов и аксессуаров через встроенный маркетплейс.

---

## 🛠 1. Подготовка и установка

### Системные требования
* **Git** (для клонирования репозитория)
* **Docker Desktop** (рекомендуется для быстрого развертывания)
* **Python 3.9+** (для локальной разработки)

### Клонирование проекта
```bash
git clone https://github.com/BBBounc/kittygramMakatrovVDv2.git
cd kittygramMakatrovVDv2
```

---

## 🚀 2. Быстрый запуск через Docker (Рекомендуется)

Это самый простой способ запустить проект вместе с базой данных PostgreSQL, не устанавливая ничего лишнего на компьютер.

1.  **Запустите Docker Desktop.**
2.  **Соберите и запустите контейнеры:**
    ```bash
    docker-compose up -d --build
    ```
3.  **Примените миграции и создайте администратора:**
    ```bash
    docker-compose exec web python manage.py migrate
    docker-compose exec web python manage.py createsuperuser
    docker-compose exec web python manage.py collectstatic --no-input
    ```
    Проект доступен по адресу: `http://127.0.0.1:8000/`

---

## 💻 3. Локальный запуск (без Docker)

Если нужно запустить проект в виртуальном окружении:

1.  **Создайте и активируйте venv:**
    ```bash
    python -m venv venv
    source venv/Scripts/activate  # Для Windows: venv\Scripts\activate
    ```
2.  **Установите зависимости:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Настройте `.env`:** Создайте файл в корне и добавьте `SECRET_KEY`, `DEBUG=True`.
4.  **Запустите сервер:**
    ```bash
    python manage.py migrate
    python manage.py runserver
    ```

---

## 📑 4. API-контракт (Эндпоинты)

| Метод | URL | Описание | Доступ |
| :--- | :--- | :--- | :--- |
| **POST** | `/auth/jwt/create/` | Логин (получение токена) | Any |
| **GET** | `/api/items/` | Список вещей в SmartPantry (с пагинацией) | Any |
| **POST** | `/api/items/` | Выставить вещь на обмен (лимит 5 шт) | Auth |
| **POST** | `/api/items/{id}/reserve/` | Забронировать вещь (Custom Action) | Auth |
| **POST** | `/api/items/{id}/confirm/` | Подтвердить передачу (Custom Action) | Owner |
| **POST** | `/api/cats/` | Добавить котика в профиль | Auth |
| **GET** | `/api/categories/` | Список категорий (Корм, Игрушки и т.д.) | Any |

---

## 🧪 5. Примеры запросов (JSON)

### Добавление вещи в SmartPantry (POST /api/items/)
```json
{
    "title": "Корм Gourmet Gold 85г",
    "category": "Корм",
    "description": "Срок до 2027 года, говядина",
    "price": 0,
    "color": "Красный"
}
```

### Фильтрация данных (GET)
* **По категории:** `GET /api/items/?category__name=Корм`
* **Поиск по тексту:** `GET /api/items/?search=Gourmet`

---

## 🛡 6. Безопасность и логика
* **JWT Auth:** Все операции с данными требуют Bearer Token.
* **Permissions:** Редактирование и удаление доступно только автору (IsOwnerOrReadOnly).
* **Бизнес-логика:** Реализована система статусов (`available`, `reserved`, `given`) и ограничение на количество активных объявлений.

---

**Разработчик:** [Владислав Макатров](https://github.com/BBBounc)  
**Проект:** Проектирование и реализация серверной части проекта Kittygram для поддержки пользовательского сценария "Обмен вещами (котошеринг)"  
**Год:** 2026