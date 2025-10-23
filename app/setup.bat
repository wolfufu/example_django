@echo off
echo Установка зависимостей для Windows...
set PG_HOME=C:\Program Files\PostgreSQL\17
set PATH=%PG_HOME%\bin;%PATH%
pip install --no-cache-dir psycopg2