```markdown
<div align="center">

# 🐱 Kittygram: Сезонные события и рейтинг котов

![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-5.2-092E20?style=for-the-badge&logo=django&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-ready-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![REST API](https://img.shields.io/badge/REST-API-FF6C37?style=for-the-badge&logo=postman&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)

**Kittygram** — социальная платформа для котов и их владельцев с уникальной системой **сезонных событий** и **рейтинга**

✨ Участвуйте в событиях • 🏆 Получайте достижения • ⭐ Повышайте рейтинг своего кота

</div>

---

## 🌟 Новые возможности

| Функция | Описание |
|:---:|:---|
| 🎪 **Сезонные события** | Зимние, весенние, летние и осенние мероприятия с бонусными очками |
| ⭐ **Система рейтинга** | Начисление очков за участие в событиях и лайки от пользователей |
| 🏆 **Достижения** | 15+ уникальных достижений для котов, автоматическое создание |
| ❤️ **Лайки** | Только авторизованные пользователи, нельзя лайкать своего кота, +5 очков |

---

## 🛠 Установка и запуск

### Системные требования
- Git
- Docker Desktop (рекомендуется) или Python 3.11+

### Клонирование проекта
```bash
git clone https://github.com/BBBounc/Kittygram_Byzaev_Dmitry.git
cd Kittygram_Byzaev_Dmitry
```

### Запуск через Docker (рекомендуется)
```bash
# Создайте файл .env
echo "SECRET_KEY=dev-secret-key-123456789" > .env
echo "DEBUG=True" >> .env
echo "DB_NAME=kittygram" >> .env
echo "DB_USER=root" >> .env
echo "DB_PASSWORD=123" >> .env
echo "DB_HOST=db" >> .env
echo "DB_PORT=5432" >> .env

# Запустите контейнеры
docker-compose up -d --build

# Примените миграции
docker-compose exec web python manage.py migrate

# Создайте суперпользователя
docker-compose exec web python manage.py createsuperuser
```

### Локальный запуск (без Docker)
```bash
# Создайте виртуальное окружение
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Установите зависимости
pip install -r requirements.txt

# Примените миграции
python manage.py migrate

# Запустите сервер
python manage.py runserver
```

### Доступ к приложению
| Сервис | URL |
|:---|:---|
| Главная страница | `http://localhost:8000` |
| Админ-панель | `http://localhost:8000/admin` |
| API Endpoint | `http://localhost:8000/api/` |

---

## 📡 API Endpoints

### Коты
| Метод | URL | Описание | Доступ |
|:---:|:---|:---|:---:|
| GET | `/api/cats/` | Список всех котов | Все |
| POST | `/api/cats/` | Добавить кота | Auth |
| GET | `/api/cats/{id}/` | Получить кота | Все |
| PATCH | `/api/cats/{id}/` | Обновить кота | Владелец |
| DELETE | `/api/cats/{id}/` | Удалить кота | Владелец |

### События
| Метод | URL | Описание | Доступ |
|:---:|:---|:---|:---:|
| GET | `/api/events/` | Список событий | Все |
| POST | `/api/events/` | Создать событие | Admin |
| GET | `/api/events/{id}/` | Получить событие | Все |

### Достижения
| Метод | URL | Описание | Доступ |
|:---:|:---|:---|:---:|
| GET | `/api/achievements/` | Список достижений | Все |
| POST | `/api/achievements/` | Создать достижение | Admin |

### Участие в событиях
| Метод | URL | Описание | Доступ |
|:---:|:---|:---|:---:|
| POST | `/api/participations/join_event/` | Участвовать в событии | Auth |

### Аутентификация
| Метод | URL | Описание | Доступ |
|:---:|:---|:---|:---:|
| POST | `/api/token/` | Получить JWT токен | Все |
| POST | `/api/token/refresh/` | Обновить токен | Auth |

---

## 🧪 Примеры запросов

### Получение JWT токена
```json
POST /api/token/
{
    "username": "admin",
    "password": "admin123"
}
```

### Создание кота
```json
POST /api/cats/
{
    "name": "Барсик",
    "color": "Ginger",
    "birth_year": 2022,
    "achievements": [1, 2]
}
```

### Создание сезонного события
```json
POST /api/events/
{
    "name": "Новогодний карнавал",
    "season": "winter",
    "start_date": "2026-12-20",
    "end_date": "2027-01-15",
    "description": "Праздничное мероприятие",
    "bonus_points": 100
}
```

### Участие кота в событии
```json
POST /api/participations/join_event/
{
    "cat_id": 1,
    "event_id": 1
}
```

### Лайк кота
```http
POST /cats/1/like/
```

---

## 🔍 Фильтрация, поиск и сортировка

| Тип | Пример запроса |
|:---|:---|
| Фильтрация по цвету | `GET /api/cats/?color=Ginger` |
| Фильтрация по сезону | `GET /api/events/?season=winter` |
| Поиск по имени | `GET /api/cats/?search=Барс` |
| Поиск событий | `GET /api/events/?search=Новогодний` |
| Сортировка по рейтингу | `GET /api/cats/?ordering=-rating_points` |
| Сортировка по лайкам | `GET /api/cats/?ordering=-likes_count` |
| Сортировка по году | `GET /api/cats/?ordering=-birth_year` |
| Комбинированный запрос | `GET /api/cats/?color=Ginger&ordering=-rating_points&search=Барс` |

---

## 🛡 Безопасность и права доступа

- **JWT Bearer Token** для API запросов
- **IsOwnerOrReadOnly** — редактирование только владельцем кота
- **IsAuthenticatedOrReadOnly** — чтение для всех, запись для авторизованных

### Бизнес-логика
- ✅ Нельзя лайкать своего кота
- ✅ +5 очков рейтинга за каждый лайк
- ✅ +бонусные очки за участие в событиях
- ✅ Автоматическое создание достижений
- ✅ Валидация дат событий

---

## 🐳 Docker команды

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

## 🧪 Тестирование

### Создание тестовых достижений
```bash
docker-compose exec web python manage.py shell -c "
from cats.models import Achievement
achievements = ['Любитель рыбки', 'Мастер охоты', 'Король сна']
for name in achievements: Achievement.objects.get_or_create(name=name)
"
```

### Проверка API
```
http://localhost:8000/api/cats/
http://localhost:8000/api/events/
http://localhost:8000/api/achievements/
```

---

## 📁 Структура проекта

```
Kittygram_Byzaev_Dmitry/
├── cats/                   # Основное приложение
│   ├── migrations/         # Миграции БД
│   ├── admin.py           # Админ-панель
│   ├── forms.py           # Формы
│   ├── models.py          # Модели данных
│   ├── serializers.py     # API сериализаторы
│   ├── urls.py            # Маршруты
│   └── views.py           # Контроллеры
├── kittygram2/            # Конфигурация проекта
│   ├── settings.py        # Настройки Django
│   └── urls.py            # Главные маршруты
├── templates/             # HTML шаблоны
│   ├── cats/              # Шаблоны котов
│   ├── events/            # Шаблоны событий
│   └── registration/      # Шаблоны регистрации
├── static/                # Статические файлы
├── media/                 # Медиа файлы
├── docker-compose.yml     # Docker Compose
├── Dockerfile             # Docker образ
├── requirements.txt       # Зависимости
├── .env.example          # Пример переменных
├── .gitignore            # Игнорируемые файлы
└── README.md             # Документация
```

---

## 👨‍💻 Разработчик

**Дмитрий Byzaev**

[![GitHub](https://img.shields.io/badge/GitHub-BBBounc-181717?style=flat-square&logo=github)](https://github.com/BBBounc)

---

## 📄 Лицензия

MIT License

---

<div align="center">
  
**Проект:** Проектирование и реализация серверной части проекта Kittygram  
**Сценарий:** Сезонные события и рейтинг  
**Год:** 2026

🐾 *Будьте добрее к котам и они ответят вам тем же* 🐾

</div>
```