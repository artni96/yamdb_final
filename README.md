# _api_yamdb_
*Данный API даёт возможность собирать ваши отзывы на различные произведения.
Здесь сможете делиться своими идеями, искать единомышленников и дискутировать.
Проект доступен по адресу: http://158.160.42.90/*
Проект реализован при помощи: 
- ![image](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green)Django Web Framework (Python)
- ![image](https://img.shields.io/badge/django%20rest-ff1709?style=for-the-badge&logo=django&logoColor=white) Django REST Framework
- ![image](https://img.shields.io/badge/JWT-000000?style=for-the-badge&logo=JSON%20web%20tokens&logoColor=white) JSON Web Tokens
- ![image](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white) Docker
- ![deploy_badge](https://github.com/artni96/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg?event=push) Статус деплоя

# Для развёртывания проекта:
- Подключитесь к рабочему удаленному серверу через ssh:
```
ssh <user>@<ip_server> # 158.160.42.90
```
- Обновите индекс пакетов APT:
```
sudo apt update
```
- Обновите установленные в системе пакеты и установите обновления безопасности:
```
sudo apt upgrade -y
```
-  Установите менеджер пакетов pip и систему контроля версий git, чтобы клонировать ваш проект:
```
sudo apt install python3-pip git -y
```
- Остановите службу nginx:
```
sudo systemctl stop nginx 
```
- Установите docker (если предварительно не был установлен):
```
sudo apt install docker.io
```
- Установите docker-compose (если предварительно не был установлен):
```
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
docker-compose --version
```
_docker-compose version 1.29.2, build 5becea4c_

- Скопируйте файлы docker-compose.yml и nginx/default.conf с локального комьютера в корневую папку сервера при помощи утилиты scp:
```
scp docker-compose.yml <user>@<ip_server>:/home/<user>/
scp -r nginx <user>@<ip_server>:/home/<user>/
```
- Измените настройки сервера nginx (ip-адрес сервера):
```
sudo nano nginx/default.conf
```
Добавьте необходимые переменные окружения в GitHub Actions:
```
DB_ENGINE # указываем, что работаем с postgresql
DB_NAME # имя базы данных
POSTGRES_USER # логин для подключения к базе данных
POSTGRES_PASSWORD # пароль для подключения к БД (установите свой)
DB_HOST # название сервиса (контейнера)
DB_PORT # порт для подключения к БД
HOST # ip-адрес сервера
USER # имя пользователя для подключения к серверу
PASSPHRASE # фраза-пароль для подключения (если такой был задан при создании ssh-ключа)
SSH_KEY # приватный ключ компьютера, который имеет доступ к серверу
DOCKER_USERNAME # Аккаунт DockerHub, на котором находится образ контейнера web
DOCKER_PASSWORD # Пароль от аккаунта DockerHub
TELEGRAM_TO # ID телеграм-аккаунта
TELEGRAM_TOKEN # токен телеграм-бота, с которого будет отправлено сообщение
```
- Соберите необходимые конейнеры:
```
sudo docker-compose up -d
```
- Выполните миграции:
```
sudo docker-compose exec web python manage.py migrate
```
- Создайте суперпользователя:
```
sudo docker-compose exec web python manage.py createsuperuser
```

# Проект запущен и доступен по ip-адресу сервера (158.160.42.90)

- Redoc доступен по адресу http://158.160.42.90/redoc

### В случае каких-либо изменений в контейнерах необходимо выполнить их пересборку:
```
sudo docker-compose up -d --build 
```
### Не забывайте делать резервную копию БД:
```
sudo docker-compose exec web python manage.py dumpdata > <название_файла>.json
```
### Заполнение БД данными
Необходимо перенести json-файл на сервер:
```
scp <название_файла>.json <user>@<ip_server>:.
```
Затем перенести этот файл в контейнер БД и выполнить:
```
sudo docker cp <название_файла>.json <id_контейнера_web>:app/
sudo docker-compose exec web python manage.py loaddata <название_файла>.json
```
