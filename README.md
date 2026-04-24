# Проект с услугами для людей


1. Клонируем репозиторий с проектом удобным способом (например по https)
  ```
  git clone https://github.com/nikita201ss/env.git
  ```

2. Переходим в директорию
  ```
  cd env
  ```

3. Создаем виртуальное окружение и активируем его
  ```
  python -m venv venv

  venv\Scripts\activate
  ```

4. Устанавливаем зависимости (проект работает на СУБД MySQL)
  ```
  pip install django mysqlclient python-dotenv Pillow
  ```

5. Создаём БД в MySQL
  ```
  CREATE DATABASE myprojectdb CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
  ```

6. Создаём файл .env в корне проекта с данными
  ```
  SECRET_KEY=63f4945d921d599f27ae4fdf5bada3f1
  MYSQL_DB=myprojectdb
  MYSQL_USER=root
  MYSQL_PASSWORD=root
  MYSQL_HOST=localhost
  MYSQL_PORT=3306
  ```

7. Создаём миграции
  ```
  python manage.py migrate
  ```

8. Создаём суперпользователя
  ```
  python manage.py createsuperuser
  ```
    
10. Запуск проекта
  ```
  python manage.py runserver
  ```
