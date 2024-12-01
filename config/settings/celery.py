from config.settings.env import env
import environ

# Инициализация environ
env = environ.Env()

# Чтение переменных из .env файла
environ.Env.read_env()

CELERY_BROKER_URL = env.str('CELERY_BROKER_URL')
CELERY_RESULT_BACKEND = env.str('CELERY_RESULT_BACKEND')
CELERY_ACCEPT_CONTENT = env.list('CELERY_ACCEPT_CONTENT', default=['json'])
CELERY_TASK_SERIALIZER = env.str('CELERY_ACCEPT_CONTENT')
CELERY_RESULT_SERIALIZER = env.str('CELERY_ACCEPT_CONTENT')
CELERY_TIMEZONE = env.str('CELERY_ACCEPT_CONTENT')
CELERY_WORKER_CONCURRENCY = env.int('CELERY_ACCEPT_CONTENT')
CELERY_WORKER_POOL = env.str('CELERY_ACCEPT_CONTENT')
