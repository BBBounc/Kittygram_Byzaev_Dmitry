# Используем образ 3.11 на базе Bookworm (самый актуальный и полный)
FROM python:3.11-bookworm

WORKDIR /app

# Устанавливаем системные пакеты для компиляции всего подряд
RUN apt-get update && apt-get install -y \
    build-essential \
    libssl-dev \
    libffi-dev \
    python3-dev \
    cargo \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# Обновляем инструменты установки до последних версий
RUN pip install --no-cache-dir --upgrade pip setuptools wheel

# Копируем твой неизменный requirements.txt
COPY requirements.txt .

# Пытаемся установить зависимости. 
# Если какая-то библиотека дает сбой, мы пробуем ставить их по одной, 
# чтобы увидеть, на чем именно ломается сборка.
RUN pip install --no-cache-dir -r requirements.txt || \
    (while read -r line; do pip install --no-cache-dir "$line" || echo "Failed to install $line"; done < requirements.txt)

# Копируем проект
COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]