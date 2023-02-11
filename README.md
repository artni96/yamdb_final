# _api_yamdb_
*Данный API даёт возможность собирать ваши отзывы на различные произведения.
Здесь сможете делиться своими идеями, искать единомышленников и дискутировать.*
Проект реализован при помощи: 
- ![image](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green)Django Web Framework (Python)
- ![image](https://img.shields.io/badge/django%20rest-ff1709?style=for-the-badge&logo=django&logoColor=white) Django REST Framework
- ![image](https://img.shields.io/badge/JWT-000000?style=for-the-badge&logo=JSON%20web%20tokens&logoColor=white) JSON Web Tokens
- ![image](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white) Docker
- ![deploy_badge](https://github.com/artni96/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg?event=push) Статус деплоя

# Для развёртывания проекта:
- Необходимо перейти в директорию infra_sp2 и создать .env-файл:
Необходимые переменные окружения:
```
DB_ENGINE=django.db.backends.postgresql # указываем, что работаем с postgresql
DB_NAME=postgres # имя базы данных
POSTGRES_USER=username # логин для подключения к базе данных
POSTGRES_PASSWORD=password # пароль для подключения к БД (установите свой)
DB_HOST=db # название сервиса (контейнера)
DB_PORT=5432 # порт для подключения к БД
```
- Соберите необходимые конейнеры:
```
docker-compose up
```
- Выполните миграции:
```
docker-compose exec web python manage.py migrate
```
- Создайте суперпользователя:
```
docker-compose exec web python manage.py createsuperuser
```
- Соберите статику:
```
docker-compose exec web python manage.py collectstatic --no-input
```
# Проект запущен и полностью готов к работе по адресу: http://localhost/

### В случае каких-либо изменений в контейнерах необходимо выполнить их пересборку:
```
docker-compose up -d --build 
```
### Не забывайте делать резервную копию БД:
```
docker-compose exec web python manage.py dumpdata > <название_файла>.json
```
### Для заполнения БД данными необходимо перенести json-файл в необходимый контейнер и выполнить:
```
docker cp <название_файла_на_локальном_комьютере>.json <id_контейнера>:app/
docker-compose exec web python manage.py loaddata <название_файла>.json
```
