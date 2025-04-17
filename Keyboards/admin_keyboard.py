# Кнопки пользователей
import asyncio

from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardButton, InlineKeyboardMarkup)

from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder


from treid_bot_tg.Keyboards.Keyboards_all import inline_keyboard_button, inline_keyboard_buttons

# Стартовая клавиатура Админа
admin_start_keyboard = asyncio.run(
    inline_keyboard_buttons(
    buttons_dct={'Данные из Базы Данных': 'db'},
    starts='admin_',
    adjust=1,
    )
)



# Клавиатура для подтверждения или отклонения
async def correct_user_keyboard(tg_id: int) -> InlineKeyboardMarkup:
    res = await inline_keyboard_buttons(
    buttons_dct={'Подтвердить': tg_id, 'Отклонить': f'no_{tg_id}'},
    starts='add_',
    adjust=3,
    )
    return res

# Клавиатура внесения нужного статуса
correct_status_admin_keyboard = asyncio.run(inline_keyboard_buttons(
    buttons_dct={'Активен': 'True', 'Не активен': 'False'},
    starts='ad_cor_',
    adjust=3,
))