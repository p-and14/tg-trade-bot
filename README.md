# Telegram Trade Bot

Бот telegram для обмена токенов в сети ethereum на Uniswap UR.

## Release Notes
### v1.1
 - Добавлена возможность добавления своего кошелька
 - Добавлен паттерн DAO для взаимодействия с БД

Доступные команды: /start и /menu.

В будущем:
- Создание нового кошелька, удаление существующего кошелька
- Покупка/продажа токенов
- Апрув токенов

## Stack
- python 3.13.2
- postgresql
- aiogram 3.18.0

## Project launch:
1. Создать виртуальное окружение.
2. Установить зависимости: 
> pip install -r requirements.txt
3. Создать ".env" файл на примере ".env_example".
4. Создать БД (Выбрать один вариант):
   - Установить к себе на компьютер по инструкции из [официальной документации](https://www.postgresql.org/download/). 
   - Установить docker-контейнер с уже готовой и настроенной СУБД. 
    > docker run --name postgres -e POSTGRES_PASSWORD=postgres -e TZ=Europe/Moscow -d postgres
5. Запустить run_tg_bot.py
> python run_tg_bot.py
