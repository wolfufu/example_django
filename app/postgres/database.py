import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import urllib.parse

load_dotenv()

def get_database_url():
    DB_NAME = os.getenv('DB_NAME', 'myproject_db')
    DB_USER = os.getenv('DB_USER', 'myproject_user')
    DB_PASSWORD = os.getenv('DB_PASSWORD', 'myproject_password')
    DB_HOST = os.getenv('DB_HOST', 'localhost')
    DB_PORT = os.getenv('DB_PORT', '5432')
    
    # Кодируем пароль на случай спецсимволов
    encoded_password = urllib.parse.quote_plus(DB_PASSWORD)
    
    return f"postgresql://{DB_USER}:{encoded_password}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

DATABASE_URL = get_database_url()

try:
    engine = create_engine(
        DATABASE_URL,
        pool_pre_ping=True,
        echo=False,  # Поставьте True для отладки SQL запросов
        connect_args={'options': '-c client_encoding=utf8'}
    )
    
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base = declarative_base()
    
except Exception as e:
    print(f"Ошибка подключения к базе данных: {e}")
    # Создаем заглушки для случаев, когда БД недоступна
    engine = None
    SessionLocal = None
    Base = declarative_base()

def get_db():
    if SessionLocal is None:
        raise Exception("База данных не настроена")
    
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()