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

## **О проекте**

**Kittygram** — это современная социальная платформа для котов и их владельцев.

> ✨ **Уникальная система сезонных событий**
> 🏆 **Рейтинг котов с возможностью лайкать**
> 🎪 **Четыре сезонных мероприятия в год**
> ⭐ **Бонусные очки за активность**

---

## **Ключевые возможности**

|                                                                                                                                                |                                                                                                                                            |                                                                                                                                    |
| :---------------------------------------------------------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------: | :--------------------------------------------------------------------------------------------------------------------------------: |
| 🎪**Сезонные события**`<br>`Зимние, весенние, летние`<br>`и осенние мероприятия | ⭐**Система рейтинга**`<br>`Очки за события и лайки`<br>`Топ котов на главной | 🏆**Достижения**`<br>`15+ уникальных наград`<br>`Автоматическое создание |
|                     ❤️**Лайки**`<br>`+5 очков за лайк`<br>`Нельзя лайкать себя                     |                           📡**REST API**`<br>`Полный CRUD`<br>`JWT аутентификация                           |            🐳**Docker**`<br>`Готов к развёртыванию`<br>`PostgreSQL в контейнере            |

---

## **Быстрый старт**

### Клонирование

```bash
git clone https://github.com/BBBounc/Kittygram_Byzaev_Dmitry.git
cd Kittygram_Byzaev_Dmitry

# Создание .env файла
echo "SECRET_KEY=dev-secret-key-123456789" > .env
echo "DEBUG=True" >> .env
echo "DB_NAME=kittygram" >> .env
echo "DB_USER=root" >> .env
echo "DB_PASSWORD=123" >> .env
echo "DB_HOST=db" >> .env
echo "DB_PORT=5432" >> .env

# Запуск
docker-compose up -d --build
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser


Локальный запуск
bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
Доступ к приложению
Сайт	http://localhost:8000
Админка	http://localhost:8000/admin
API	http://localhost:8000/api/
API Endpoints
Метод	URL	Описание	Доступ
GET	/api/cats/	Список котов	Все
POST	/api/cats/	Создать кота	Auth
GET	/api/cats/{id}/	Просмотр кота	Все
PATCH	/api/cats/{id}/	Обновить кота	Владелец
DELETE	/api/cats/{id}/	Удалить кота	Владелец
GET	/api/events/	Список событий	Все
POST	/api/events/	Создать событие	Admin
GET	/api/events/{id}/	Просмотр события	Все
GET	/api/achievements/	Список достижений	Все
POST	/api/token/	Получить JWT токен	Все
Примеры запросов
Получение токена

json
POST /api/token/
{
    "username": "admin",
    "password": "admin123"
}
Создание кота

json
POST /api/cats/
{
    "name": "Барсик",
    "color": "Ginger",
    "birth_year": 2022,
    "achievements": [1, 2]
}
Создание события

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
Участие в событии

json
POST /api/participations/join_event/
{
    "cat_id": 1,
    "event_id": 1
}
Фильтрация и сортировка
bash
# Фильтрация по цвету
GET /api/cats/?color=Ginger

# Фильтрация по сезону
GET /api/events/?season=winter

# Поиск по имени
GET /api/cats/?search=Барс

# Сортировка по рейтингу (убывание)
GET /api/cats/?ordering=-rating_points

# Сортировка по лайкам
GET /api/cats/?ordering=-likes_count

# Комбинированный запрос
GET /api/cats/?color=Ginger&ordering=-rating_points&search=Барс
Правила и ограничения
Лайкнуть можно только чужого кота

За лайк кот получает +5 очков рейтинга

За участие в событии кот получает бонусные очки

Редактировать кота может только владелец

API требует JWT токен для защищённых эндпоинтов

Docker команды
bash
docker-compose up -d          # Запуск
docker-compose logs -f        # Логи
docker-compose down           # Остановка
docker-compose down -v        # Остановка с очисткой БД
docker-compose exec web bash  # Вход в контейнер
Разработчик
Дмитрий Byzaev

GitHub: BBBounc

Лицензия
MIT License

Проект: Kittygram | Сценарий: Сезонные события и рейтинг | 2026

text

Вот теперь **чисто, минималистично и красиво**:
- Нет лишних эмодзи
- Чёткие заголовки
- Аккуратные таблицы
- Код в одну строку без караоке
- Простые и понятные инструкции
```
