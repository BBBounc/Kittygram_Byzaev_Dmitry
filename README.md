<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
</head>
<body>

<div align="center">
  
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:10b981,100:059669&height=200&section=header&text=Kittygram&fontSize=70&fontColor=white&animation=fadeIn" width="100%"/>

  <h1>
    <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Animals/Cat.png" alt="Cat" width="50" />
    Сезонные события и рейтинг котов
    <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Animals/Cat.png" alt="Cat" width="50" />
  </h1>

  <p>
    <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=24&duration=3000&pause=500&color=10B981&center=true&vCenter=true&width=600&lines=Добро+пожаловать+в+Kittygram!;Участвуйте+в+событиях;Повышайте+рейтинг;Получайте+достижения" alt="Typing SVG" />
  </p>

  <p>
    <img src="https://img.shields.io/badge/Python-3.11-3776AB?style=flat-square&logo=python&logoColor=white&labelColor=2c3e50"/>
    <img src="https://img.shields.io/badge/Django-5.2-092E20?style=flat-square&logo=django&logoColor=white&labelColor=2c3e50"/>
    <img src="https://img.shields.io/badge/Docker-Ready-2496ED?style=flat-square&logo=docker&logoColor=white&labelColor=2c3e50"/>
    <img src="https://img.shields.io/badge/REST_API-FF6C37?style=flat-square&logo=postman&logoColor=white&labelColor=2c3e50"/>
    <img src="https://img.shields.io/badge/PostgreSQL-15-4169E1?style=flat-square&logo=postgresql&logoColor=white&labelColor=2c3e50"/>
  </p>

</div>

<br>

<div align="center">
  <table>
    <tr>
      <td align="center">
        <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Activities/Sparkles.png" width="40"><br>
        <b>15+</b><br>
        Достижений
      </td>
      <td align="center">
        <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Activities/Party%20Popper.png" width="40"><br>
        <b>4 сезона</b><br>
        Событий
      </td>
      <td align="center">
        <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Symbols/Star.png" width="40"><br>
        <b>∞</b><br>
        Рейтинг
      </td>
      <td align="center">
        <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Symbols/Heart%20Decoration.png" width="40"><br>
        <b>❤️</b><br>
        Лайки
      </td>
    </tr>
  </table>
</div>

---

## <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Activities/Confetti%20Ball.png" width="30"> **О проекте**

**Kittygram** — это современная социальная платформа для котов и их владельцев.

> ✨ **Уникальная система сезонных событий**  
> 🏆 **Рейтинг котов с возможностью лайкать**  
> 🎪 **Четыре сезонных мероприятия в год**  
> ⭐ **Бонусные очки за активность**

---

## <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Fire.png" width="30"> **Ключевые возможности**

| | | |
|:---:|:---:|:---:|
| 🎪 **Сезонные события**<br>Зимние, весенние, летние<br>и осенние мероприятия | ⭐ **Система рейтинга**<br>Очки за события и лайки<br>Топ котов на главной | 🏆 **Достижения**<br>15+ уникальных наград<br>Автоматическое создание |
| ❤️ **Лайки**<br>+5 очков за лайк<br>Нельзя лайкать себя | 📡 **REST API**<br>Полный CRUD<br>JWT аутентификация | 🐳 **Docker**<br>Готов к развёртыванию<br>PostgreSQL в контейнере |

---

## <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Hand%20gestures/Backhand%20Index%20Pointing%20Right%20Dark%20Skin%20Tone.png" width="30"> **Быстрый старт**

### 📦 Клонирование

```bash
git clone https://github.com/BBBounc/Kittygram_Byzaev_Dmitry.git
cd Kittygram_Byzaev_Dmitry
🐳 Запуск через Docker (рекомендуется)
bash
# Создаём .env файл
cat > .env << EOF
SECRET_KEY=dev-secret-key-123456789
DEBUG=True
DB_NAME=kittygram
DB_USER=root
DB_PASSWORD=123
DB_HOST=db
DB_PORT=5432
EOF

# Запускаем контейнеры
docker-compose up -d --build

# Применяем миграции
docker-compose exec web python manage.py migrate

# Создаём администратора
docker-compose exec web python manage.py createsuperuser
💻 Локальный запуск
bash
# Создаём виртуальное окружение
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate  # Windows

# Устанавливаем зависимости
pip install -r requirements.txt

# Запускаем
python manage.py migrate
python manage.py runserver
🌐 Доступ
🖥️ Веб-интерфейс	http://localhost:8000
🔧 Админ-панель	http://localhost:8000/admin
📡 API	http://localhost:8000/api/
<img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Laptop.png" width="30"> API Endpoints
🐱 Коты
Метод	URL	Доступ	Описание
GET	/api/cats/	Все	📋 Список всех котов
POST	/api/cats/	Auth	✨ Добавить кота
GET	/api/cats/{id}/	Все	🔍 Просмотр кота
PATCH	/api/cats/{id}/	Владелец	✏️ Обновить кота
DELETE	/api/cats/{id}/	Владелец	🗑️ Удалить кота
🎪 События
Метод	URL	Доступ	Описание
GET	/api/events/	Все	📋 Список событий
POST	/api/events/	Admin	✨ Создать событие
GET	/api/events/{id}/	Все	🔍 Просмотр события
🏆 Достижения
Метод	URL	Доступ	Описание
GET	/api/achievements/	Все	📋 Список достижений
POST	/api/achievements/	Admin	✨ Создать достижение
🔐 Аутентификация
Метод	URL	Описание
POST	/api/token/	🔑 Получить JWT токен
POST	/api/token/refresh/	🔄 Обновить токен
<img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Activities/Video%20Game.png" width="30"> Примеры запросов
<details> <summary><b>📝 Получение токена</b></summary>
json
POST /api/token/
{
    "username": "admin",
    "password": "admin123"
}
</details><details> <summary><b>🐱 Создание кота</b></summary>
json
POST /api/cats/
{
    "name": "Барсик",
    "color": "Ginger",
    "birth_year": 2022,
    "achievements": [1, 2]
}
</details><details> <summary><b>🎪 Создание события</b></summary>
json
POST /api/events/
{
    "name": "Новогодний карнавал",
    "season": "winter",
    "start_date": "2026-12-20",
    "end_date": "2027-01-15",
    "description": "Праздничное мероприятие",
    "bonus_points": 100
}
</details><details> <summary><b>⭐ Участие в событии</b></summary>
json
POST /api/participations/join_event/
{
    "cat_id": 1,
    "event_id": 1
}
</details>
<img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Magnifying%20Glass%20Tilted%20Left.png" width="30"> Фильтрация и поиск
bash
# Фильтрация по цвету
GET /api/cats/?color=Ginger

# Фильтрация по сезону
GET /api/events/?season=winter

# Поиск по имени
GET /api/cats/?search=Барс

# Топ по рейтингу
GET /api/cats/?ordering=-rating_points

# Топ по лайкам
GET /api/cats/?ordering=-likes_count

# Комбинированный запрос
GET /api/cats/?color=Ginger&ordering=-rating_points&search=Барс
<img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Shield.png" width="30"> Безопасность
🔐 JWT аутентификация	Bearer Token для API
🛡️ IsOwnerOrReadOnly	Редактирование только владельцем
👤 IsAuthenticatedOrReadOnly	Чтение для всех, запись для авторизованных
💝 Лайки	Нельзя лайкать своего кота
⭐ Рейтинг	+5 за лайк, +бонус за события
<img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Hand%20gestures/Waving%20Hand%20Light%20Skin%20Tone.png" width="30"> Docker команды
bash
docker-compose up -d          # Запуск в фоне
docker-compose logs -f        # Просмотр логов
docker-compose down           # Остановка
docker-compose down -v        # Полная очистка
docker-compose exec web bash  # Вход в контейнер
<img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/People%20with%20professions/Technologist%20Light%20Skin%20Tone.png" width="30"> Разработчик
<div align="center">
Дмитрий Byzaev

https://img.shields.io/badge/GitHub-BBBounc-181717?style=for-the-badge&logo=github&logoColor=white

</div>
<img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Clipboard.png" width="30"> Лицензия
MIT License

<div align="center"><img src="https://capsule-render.vercel.app/api?type=waving&color=0:10b981,100:059669&height=120&section=footer"/>
Проект: Kittygram | Сценарий: Сезонные события и рейтинг | Год: 2026

<p> <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Animals/Cat.png" width="20"> <i>Будьте добрее к котам и они ответят вам тем же</i> <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Animals/Cat.png" width="20"> </p></div></body> </html> ```