Быстрые советы: 

Запуск сервера: python manage.py runserver

Создание нового приложения python manage.py startapp имя
* В каждом приложении должны быть папки: static и templates/имя_приложения


# Активируйте виртуальное окружение
python -m venv venv

# Установите зависимости
pip install -r requirements.txt

# Инициализируйте таблицы
python -c "from postgres.init_db import init_db; init_db()"

# Запустите сервер
python manage.py runserver
