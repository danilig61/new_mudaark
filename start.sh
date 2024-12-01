#!/bin/sh

# Запуск Django сервера в фоновом режиме
python manage.py runserver 0.0.0.0:8000 &

# Запуск Celery рабочего процесса
celery -A config worker --loglevel=info -P eventlet
