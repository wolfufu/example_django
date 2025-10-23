# db/init_db.py
from .database import engine, Base
from .models import Test

def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    init_db()
    print("Таблицы созданы успешно!")