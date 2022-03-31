# Демо проект

Тут находится пример построения проекта  
Детали реализации не подходят для использования в продакшене (будут проблемы с конкурентными запросами)


### Локальное развертывание
Развернуть виртуальное окружение python  
Установить все python зависимости, для этого нужно в venv создать pip.conf и указать extra-index-url в секции \[global\],
```ini
[global]
extra-index-url=https://<YOUR_TFS_TOKEN>@tfs.msk.evraz.com/tfs/%D0%9F%D1%80%D0%BE%D0%B4%D0%B2%D0%B8%D0%BD%D1%83%D1%82%D0%B0%D1%8F%20%D0%B0%D0%BD%D0%B0%D0%BB%D0%B8%D1%82%D0%B8%D0%BA%D0%B0/_packaging/test%40Local/pypi/simple/
```
TFS_TOKEN генерится в Azure, права запросите у вашего РП  

Накатить миграции на чистую базу (для простоты тут используется SQLite)  
Особенности запуска см. ниже

- HTTP API
  - **\<your venv\>/gunicorn simple_shop.composites.shop_api:app \<other args\>** - запуск
  - Переменные окружения
    - **DB_URL** - URL подключения к файлу БД SqLite
    - **LOGGING_LEVEL [default=INFO]** - уровень логгирования
    - **LOGGING_JSON [default=True]** - нужны ли логи в формате JSON
    - **SA_LOGS [default=False]** - нужны ли логи SqlAlchemy
    - **ALLOW_ORIGINS [default=()]** - CORS домены
    - **IS_DEV_MODE [default=False]** - пропускает запросы со всех доменов, так же подкидывает заглушечную стратегию для аутентификатора
- HTTP API version with rabbitmq
  - **\<your venv\>/gunicorn simple_shop.composites.shop_api_with_rabbitmq:app \<other args\>** - запуск
  - Переменные окружения
    - **DB_URL** - URL подключения к файлу БД SqLite
    - **BROKER_URL** - URL подключения к брокеру сообщений RabbitMQ
    - **LOGGING_LEVEL [default=INFO]** - уровень логгирования
    - **LOGGING_JSON [default=True]** - нужны ли логи в формате JSON
    - **SA_LOGS [default=False]** - нужны ли логи SqlAlchemy
    - **ALLOW_ORIGINS [default=()]** - CORS домены
    - **IS_DEV_MODE [default=False]** - пропускает запросы со всех доменов, так же подкидывает заглушечную стратегию для аутентификатора
- Consumer
  - **python -m simple_shop.composites.consumer** - запуск консьюмера сообщений
  - Переменные окружения
    - **DB_URL** - URL подключения к файлу БД SqLite
    - **BROKER_URL** - URL подключения к брокеру сообщений RabbitMQ
    - **LOGGING_LEVEL** [default=INFO] - уровень логгирования
    - **LOGGING_JSON [default=True]** - нужны ли логи в формате JSON
    - **SA_LOGS** [default=False] - нужны ли логи SqlAlchemy
- Migrations
  - **python -m simple_shop.composites.alembic_runner \<other args\>** - запуск
  - Переменные окружения
    - **DB_URL** - URL подключения к файлу БД SqLite
    - **LOGGING_LEVEL** [default=INFO] - уровень логгирования
    - **LOGGING_JSON [default=True]** - нужны ли логи в формате JSON
    - **SA_LOGS** [default=False] - нужны ли логи SqlAlchemy
  - Запускалка миграций это обертка, аргументы просто проксируются в cli alembic  


Если приложение установить как python пакет, то запускать компоненты можно через cli, посмотреть команды:  
**simple_shop --help**

### Развертывание в контейнере
Изучить Dockerfile в каталоге развертывания, собрать контейнер с необходимой командой запуска (выбрать нужный entrypoint.sh)  
Единицы запуска смотрите выше

### Логирование
По дефолту уровень логирования - INFO, формат - JSON

### Тесты
Тут частичное покрытие тестами для демонстрации  
Запуск unit тестов **pytest ./tests/unit**  
Запуск integration тестов **pytest ./tests/integration**
