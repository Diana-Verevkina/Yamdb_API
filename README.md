# REST API для проекта YaMDb

Проект даёт возможность управлять данными методом API запросов

# Установка

Клонировать репозиторий и перейти в него в командной строке:

Cоздать и активировать виртуальное окружение:

python3 -m venv venv source 
venv/bin/activate 

Установить зависимости из файла requirements.txt:

python3 -m pip install --upgrade pip 
pip install -r requirements.txt 

Выполнить миграции:

python3 manage.py migrate 

Запустить проект:

python3 manage.py runserver

Загрузить тестовые данные в базу данных: 

python3 manage.py data_loading

