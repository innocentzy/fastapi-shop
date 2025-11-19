from pydantic import BaseSettings

# Файл с настройками для всего проекта

class Settings(BaseSettings):
    app_name: str = "FastAPI Shop"                  # Название приложения
    debug: bool = True                              # Режим отладки (вывод ошибок)
    database_url: str = "sqlite:///./shop.db"       # URL базы данных
    cors_origins: list = [                          # Список адресов с которых разрешены запросы
        "http://localhost:5173",
        "http://localhost:3000",
        "http://127.0.0.1:5173",
        "http://127.0.0.1:3000"
    ]
    static_dir: str = "static"                      # Директория для статических файлов (фронт)
    images_dir: str = "static/images"               # Директория для изображений

    class Config:                                   # Переменные окружения
        env_file = ".env"

settings = Settings()                               # Инициализируем настройки в переменной