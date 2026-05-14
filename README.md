Вот обновлённый README.md под ваш проект Kittygram с событиями и рейтингом:

```markdown
# 🐱 Kittygram: Сезонные события и рейтинг котов

![Python](https://img.shields.io/badge/python-3.11-blue.svg)
![Django](https://img.shields.io/badge/django-5.2-green.svg)
![Docker](https://img.shields.io/badge/docker-ready-blue.svg)
![REST API](https://img.shields.io/badge/REST-API-red.svg)

**Kittygram** — это социальная платформа для котов и их владельцев с уникальной системой сезонных событий и рейтинга. Участвуйте в событиях, получайте достижения, повышайте рейтинг своего кота и становитесь лучшим в сообществе!

---

## ✨ Новые возможности

### 🎪 **Сезонные события**
- Зимние, весенние, летние и осенние мероприятия
- Бонусные очки рейтинга за участие
- Автоматическое начисление наград

### ⭐ **Система рейтинга**
- Начисление очков за участие в событиях
- Лайки от других пользователей (+5 очков)
- Отображение топа котов на главной странице

### 🏆 **Достижения**
- 15+ уникальных достижений для котов
- Автоматическое создание при миграции
- Визуальное отображение в профиле

### ❤️ **Лайки**
- Только авторизованные пользователи
- Нельзя лайкать своего кота
- Обновление рейтинга в реальном времени

---

## 🛠 1. Подготовка и установка

### Системные требования
- **Git** (для клонирования репозитория)
- **Docker Desktop** (рекомендуется для быстрого развертывания)
- **Python 3.11+** (для локальной разработки)

### Клонирование проекта
```bash
git clone https://github.com/BBBounc/Kittygram_Byzaev_Dmitry.git
cd Kittygram_Byzaev_Dmitry
```

---

## 🚀 2. Быстрый запуск через Docker (Рекомендуется)

Самый простой способ запустить проект вместе с базой данных PostgreSQL.

1. **Запустите Docker Desktop.**

2. **Создайте файл `.env` в корне проекта:**
```env
SECRET_KEY=dev-secret-key-123456789
DEBUG=True
DB_NAME=kittygram
DB_USER=root
DB_PASSWORD=123
DB_HOST=db
DB_PORT=5432
```

3. **Соберите и запустите контейнеры:**
```bash
docker-compose up -d --build
```

4. **Примените миграции и создайте администратора:**
```bash
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
```

5. **Проект доступен по адресу:** `http://localhost:8000`

---

## 💻 3. Локальный запуск (без Docker)

Если нужно запустить проект в виртуальном окружении:

1. **Создайте и активируйте venv:**
```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate
```

2. **Установите зависимости:**
```bash
pip install -r requirements.txt
```

3. **Настройте `.env`:** Создайте файл в корне:
```env
SECRET_KEY=your-secret-key-here
DEBUG=True
```

4. **Запустите сервер:**
```bash
python manage.py migrate
python manage.py runserver
```

---

## 📑 4. API Эндпоинты

### 🐱 Коты
| Метод | URL | Описание | Доступ |
| :--- | :--- | :--- | :--- |
| **GET** | `/api/cats/` | Список всех котов | Any |
| **POST** | `/api/cats/` | Добавить кота | Auth |
| **GET** | `/api/cats/{id}/` | Получить кота | Any |
| **PATCH** | `/api/cats/{id}/` | Обновить кота | Owner |
| **DELETE** | `/api/cats/{id}/` | Удалить кота | Owner |

### 🎪 События
| Метод | URL | Описание | Доступ |
| :--- | :--- | :--- | :--- |
| **GET** | `/api/events/` | Список событий | Any |
| **POST** | `/api/events/` | Создать событие | Admin |
| **GET** | `/api/events/{id}/` | Получить событие | Any |

### 🏆 Достижения
| Метод | URL | Описание | Доступ |
| :--- | :--- | :--- | :--- |
| **GET** | `/api/achievements/` | Список достижений | Any |
| **POST** | `/api/achievements/` | Создать достижение | Admin |

### 🔐 Аутентификация
| Метод | URL | Описание | Доступ |
| :--- | :--- | :--- | :--- |
| **POST** | `/api/token/` | Получить JWT токен | Any |
| **POST** | `/api/token/refresh/` | Обновить токен | Auth |

---

## 🧪 5. Примеры запросов (JSON)

### Получение JWT токена
**POST** `/api/token/`
```json
{
    "username": "admin",
    "password": "admin123"
}
```

### Создание кота
**POST** `/api/cats/`
```json
{
    "name": "Барсик",
    "color": "Ginger",
    "birth_year": 2022,
    "achievements": [1, 2]
}
```

### Создание сезонного события
**POST** `/api/events/`
```json
{
    "name": "Новогодний карнавал",
    "season": "winter",
    "start_date": "2026-12-20",
    "end_date": "2027-01-15",
    "description": "Праздничное мероприятие с бонусами",
    "bonus_points": 100
}
```

### Участие кота в событии
**POST** `/api/participations/join_event/`
```json
{
    "cat_id": 1,
    "event_id": 1
}
```

### Лайк кота (HTML эндпоинт)
**POST** `/cats/{id}/like/`

---

## 🔍 6. Фильтрация, поиск и сортировка

### Фильтрация
```
GET /api/cats/?color=Ginger          # Рыжие коты
GET /api/events/?season=winter       # Зимние события
```

### Поиск
```
GET /api/cats/?search=Барс           # Поиск по имени
GET /api/events/?search=Новогодний   # Поиск событий
```

### Сортировка
```
GET /api/cats/?ordering=-rating_points    # Топ по рейтингу
GET /api/cats/?ordering=-likes_count      # По лайкам
GET /api/cats/?ordering=-birth_year       # Молодые сначала
GET /api/events/?ordering=start_date      # По дате начала
```

### Комбинированные запросы
```
GET /api/cats/?color=Ginger&ordering=-rating_points&search=Барс
```

---

## 🛡 7. Безопасность и логика

### Аутентификация
- **JWT Bearer Token** для API запросов
- Только авторизованные пользователи могут:
  - Добавлять котов
  - Ставить лайки
  - Участвовать в событиях

### Права доступа
- **IsOwnerOrReadOnly**: Редактирование только владельцем кота
- **IsAuthenticatedOrReadOnly**: Чтение для всех, запись для авторизованных

### Бизнес-логика
- ✅ Нельзя лайкать своего кота
- ✅ +5 очков рейтинга за каждый лайк
- ✅ +бонусные очки за участие в событиях
- ✅ Автоматическое создание достижений
- ✅ Валидация дат событий

---

## 📁 8. Структура проекта

```
Kittygram_Byzaev_Dmitry/
├── cats/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   └── views.py
├── kittygram2/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── cats/
│   ├── events/
│   └── registration/
├── static/
├── media/
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

---

## 🐳 9. Docker команды

```bash
# Запуск в фоновом режиме
docker-compose up -d

# Просмотр логов
docker-compose logs -f

# Остановка контейнеров
docker-compose down

# Полная перезагрузка (с очисткой БД)
docker-compose down -v
docker-compose up --build

# Выполнение команд в контейнере
docker-compose exec web python manage.py createsuperuser
docker-compose exec web bash
```

---

## 🧪 10. Тестирование

### Создание тестовых данных
```bash
# Добавить достижения
docker-compose exec web python manage.py shell -c "
from cats.models import Achievement
achievements = ['Любитель рыбки', 'Мастер охоты', 'Король сна']
for name in achievements: Achievement.objects.get_or_create(name=name)
"
```

### Проверка API через браузер
```
http://localhost:8000/api/cats/
http://localhost:8000/api/events/
http://localhost:8000/api/achievements/
```

---

## 👨‍💻 Разработчик

**Дмитрий Byzaev**  
GitHub: [@BBBounc](https://github.com/BBBounc)

---

## 📄 Лицензия

MIT License

---

**Проект:** Проектирование и реализация серверной части проекта Kittygram для поддержки пользовательского сценария "Сезонные события и рейтинг"  
**Год:** 2026
```

Этот README.md:
- ✅ Обновлён под ваш проект Kittygram
- ✅ Добавлена информация о сезонных событиях
- ✅ Описана система рейтинга
- ✅ Добавлены примеры API запросов
- ✅ Красивое оформление с бейджами
- ✅ Понятная структура и инструкции
- ✅ Включены все новые функции (лайки, достижения, события)