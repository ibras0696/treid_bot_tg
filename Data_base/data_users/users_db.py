import asyncio
import sqlite3
from datetime import datetime

# БД
base_user = './Data_base/data_users/data_users.db'


async def check_user_db(tg_id: int, status='None'):
    '''
    Функция для проверки присутствия пользователя в базе, если нет добавляет
    :param tg_id: Телеграм ID
    :param status: Статус По умолчанию Нечего None
    :return: True если пользователь есть иначе False
    '''
    global base_user
    # Сегодняшняя Дата в таком формате 01.12.2025
    date_today = str(datetime.today().strftime("%d.%m.%Y"))
    try:
        with sqlite3.connect(base_user) as conn:
            # Создание и подключение к БД
            cur = conn.cursor()
            # Запрос на получение всех пользователей с таким tg_id
            items = cur.execute(f"SELECT tg_id FROM users WHERE tg_id == '{tg_id}'").fetchone()
            # Проверка наличии такого пользователя в БД
            if items == None or len(items) == 0:
                cur.execute('''
                INSERT INTO users(tg_id, date_con, status) 
                VALUES (?, ?, ?)
                ''', (tg_id, date_today, status))
                conn.commit()
                return False

    except Exception as ex:
        return ex
    else:
        return True


async def status_check_user_db(tg_id: int):
    '''
    Функция для проверки статуса Пользователя
    :param tg_id: Телеграм ID

    :return: Проверяет Статус возвращает True или False
    '''
    global base_user
    try:
        with sqlite3.connect(base_user) as conn:
            # Создание и подключение к БД
            cur = conn.cursor()
            # Запрос на получение всех пользователей с таким tg_id
            items = cur.execute(f"SELECT status FROM users WHERE tg_id == '{tg_id}'").fetchall()

            if len(items) != 0:
                status = items[0][0]
                if status == 'True':
                    return True
                return False
            return False


    except Exception as ex:
        return ex


async def update_user_db(tg_id: int, status: bool=False):
    '''
    Функция для обновления Статуса Пользователя
    :param tg_id: Телеграм ID
    :param status: Статус True или False & NONE
    :return: Возвращает True
    '''
    global base_user
    sts = [True, False]
    if status not in sts:
        status = False
    try:
        with sqlite3.connect(base_user) as conn:
            #  подключение к БД
            cur = conn.cursor()

            cur.execute(f'''
            UPDATE users
            SET status = '{status}'
            WHERE tg_id = '{tg_id}'
            ''')

            conn.commit()
    except Exception as ex:
        return f'Ошибка: {ex}'
    else:
        return True


async def get_user_db():
    '''
        Функция для получение данных с БД Users
        :return: Возвращает Словарь {1: {'tg_id': 1, 'date': '01.01.2001', 'status': 'True'}, 2: {'tg_id': 2, 'date': '01.01.2001', 'status': 'False'}}
        '''
    global base_user
    try:
        with sqlite3.connect(base_user) as conn:
            #  подключение к БД
            cur = conn.cursor()

            items = cur.execute(f'''
                SELECT *
                FROM users
                ''').fetchall()
            # Заключение полученных данных с бд в Словарь
            result = {f'id_{i[0]}':{'tg_id': i[1], 'date': i[2],'status': i[3]} for i in items}
            conn.commit()
    except Exception as ex:
        return f'Ошибка: {ex}'
    else:
        return result


