# Обработчик команд
from aiogram import Router, F, Bot
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

# Получение Списков Админов
import dotenv
import os

# Функция для проверки по БД
from Data_base.data_users.users_db import update_user_db, get_user_db

# Кнопки
from Keyboards.admin_keyboard import correct_status_admin_keyboard, admin_start_keyboard

# Состояния
from States.admin_state import AdminAddDBUser

router = Router()

# Основные Админы
dotenv.load_dotenv()
admin_id = os.getenv('ADMIN1')


@router.message(Command('admin'))
async def admin_cmd(message: Message):
    user_id = str(message.chat.id)
    if user_id == admin_id:
        await message.answer('Добро пожаловать в Админ Панель! ', reply_markup=admin_start_keyboard)

@router.callback_query(F.data.startswith('admin_'))
async def get_admin_db(call_back: CallbackQuery):
    call_data = call_back.data.replace('admin_', '')
    if call_data == 'db':
        data_db = await get_user_db()
        text = ''
        for key, value in data_db.items():
            text += f'\n{key} | tg_id: {value.get('tg_id')} | Дата: {value.get('date')} | Статус: {value.get('status')}'

        await call_back.message.edit_text(text=text)


# Обработчик Разрешения доступа
@router.callback_query(F.data.startswith('add_'))
async def correct_admin_cmd(call_back: CallbackQuery, state: FSMContext, bot: Bot):
    call_data = call_back.data.replace('add_', '')
    if call_data.startswith('no_'):
        # Получение Айди из Call_back_data
        new_user_id = int(call_data.replace('no_', ''))
        await bot.send_message(new_user_id, 'К сожалению вашу заявку отклонили')
        await call_back.message.delete()
        await call_back.message.answer('Отказ зафиксирован')
        await state.clear()
    else:
        # Получение Айди ТГ из Call_back_data
        new_user_id = int(call_back.data.replace('add_', ''))
        # Обновление состояний
        await state.set_state(AdminAddDBUser.user_id)
        await state.update_data(user_id=new_user_id)
        # Переход на новое состояние
        await state.set_state(AdminAddDBUser.status)
        await call_back.message.edit_text('Выбери Статус Пользователю', reply_markup=correct_status_admin_keyboard)


@router.callback_query(F.data.startswith('ad_cor_'))
async def correct_admin_cmd(call_back: CallbackQuery, state: FSMContext, bot: Bot):
    try:
        # Ловим нужный статус
        status = call_back.data.replace('ad_cor_', '')
        await state.update_data(status=status)
        # Получение данных с состояния
        data = await state.get_data()
        user_id = data.get('user_id')

        if status == 'True':
            await update_user_db(user_id, True)
            await call_back.message.delete()
            await call_back.message.answer(f'Пользователь: {user_id}'
                                              f'\nУспешно добавлен')
            await bot.send_message(user_id, 'Вы были успешно добавлены')
        else:
            await call_back.message.delete()
            await bot.send_message(user_id, 'К сожалению вашу заявку отклонили')
            await call_back.message.answer('Отказ зафиксирован')
        await state.clear()
    except Exception as ex:
        await call_back.message.answer(f'Возникла ошибка: {ex}')







