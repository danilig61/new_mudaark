from pathlib import Path
import os

import environ

# Инициализация environ
env = environ.Env()

# Определение базовой директории
BASE_DIR = Path(__file__).resolve()

# Загрузка переменных окружения
env_file = BASE_DIR / (".env.local" if os.getenv("READ_ENV_LOCAL") else ".env")
print(f"Загружаем файл окружения: {env_file}")  # Отладочный вывод

if env_file.exists():
    environ.Env.read_env(str(env_file))
else:
    raise FileNotFoundError(f"Файл {env_file} не найден. Убедитесь, что он существует.")
