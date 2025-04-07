# Кнопки пользователей
import asyncio

from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardButton, InlineKeyboardMarkup)

from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

from Keyboards.Keyboards_all import inline_keyboard_buttons, inline_keyboard_button

# Кнопка возврата назад
back_user_button = asyncio.run(inline_keyboard_button(
    buttons_dct={'❎ Назад ❎': 'back'},
        starts='',
))

# Словарь нужный волют
dct_value_inverting = {
    '💸AUD/CAD💸': '47',
    '💸AUD/CHF💸': '48',
    '💸AUD/GBP💸': '1489',
    '💸AUD/JPY💸': '49',
    '💸AUD/USD💸': '5',
    '💸CAD/CHF💸': '14',
    '💸CAD/JPY💸': '51',
    '💸CHF/JPY💸': '13',
    '💸EUR/AUD💸': '15',
    '💸EUR/CAD💸': '16',
    '💸EUR/CHF💸': '10',
    '💸EUR/GBP💸': '6',
    '💸EUR/JPY💸': '9',
    '💸EUR/USD💸': '1',
    '💸GBP/AUD💸': '53',
    '💸GBP/CAD💸': '54',
    '💸GBP/JPY💸': '11',
    '💸GBP/USD💸': '2',
    '💸USD/CAD💸': '7',
    '💸USD/CHF💸': '4',
    '💸USD/JPY💸': '3'}

reverse_dct_value_inverting = {
    '1': '💸EUR/USD💸',
    '10': '💸EUR/CHF💸',
    '11': '💸GBP/JPY💸',
    '13': '💸CHF/JPY💸',
    '14': '💸CAD/CHF💸',
    '1489': '💸AUD/GBP💸',
    '15': '💸EUR/AUD💸',
    '16': '💸EUR/CAD💸',
    '2': '💸GBP/USD💸',
    '3': '💸USD/JPY💸',
    '4': '💸USD/CHF💸',
    '47': '💸AUD/CAD💸',
    '48': '💸AUD/CHF💸',
    '49': '💸AUD/JPY💸',
    '5': '💸AUD/USD💸',
    '51': '💸CAD/JPY💸',
    '53': '💸GBP/AUD💸',
    '54': '💸GBP/CAD💸',
    '6': '💸EUR/GBP💸',
    '7': '💸USD/CAD💸',
    '9': '💸EUR/JPY💸'}

# Кнопки Валют
values_keyboards = asyncio.run(inline_keyboard_buttons(
    buttons_dct=dct_value_inverting,
    starts='val_',
    adjust=3,

))


# Словарь нужного времени
dct_time_out = {
    '⬛1 Минута⬛': '1m',
    '⬛5 Минут⬛': '5m',
    '⬛15 Минут⬛': '15m',
    '⬛30 Минут⬛': '30m',
    '⬛1 Час⬛': '1h',
    '⬛5 Часов⬛': '5h',
    '⬛1 День⬛': '1d',
    '⬛1 Неделя⬛': '1w',
    '⬛1 Месяц⬛': '1mo',
    }

# Кнопки дл времени
time_out_keyboards = asyncio.run(inline_keyboard_buttons(
    buttons_dct=dct_time_out,
    starts='time_',
    adjust=3,
))

# Функция для подтверждения пользователя
async def correct_status(tg_id: int) -> InlineKeyboardMarkup:
    # Кнопки для подтверждения
    correct = await inline_keyboard_buttons(
        buttons_dct={'Подтвердить': tg_id},
        starts='cor_',
        adjust=1
    )
    return correct


