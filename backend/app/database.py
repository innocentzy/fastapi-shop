from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings

engine = create_engine(                                                             # Создание движка  для работы с базой данных
    settings.database_url,                                                          # Получаем URL через файл настроек
    connect_args={"check_same_thread": False},                                      # Настройки
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)         # Создание сессии для работы с базой данных
Base = declarative_base()                                                           # Базовый класс для для работы с базой данных

def get_db():                                                                       # Функция для открытия сессии для работы с БД
    db = SessionLocal()                                                              
    try:
        yield db                                                                    # Пытаемся вернуть базу данных
    finally:
        db.close()                                                                  # В конце закрываем сессию

def init_db():                                                                      # Функция инициализации базы данных
    Base.metadata.create_all(bind=engine)                                           # Создаем все таблицы