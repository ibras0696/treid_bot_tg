# Обработчик команд

from aiogram import Router, F, Bot
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery

# Функция для работы с БД
from treid_bot_tg.DataBase.users_db import (check_user_db,
                                            status_check_user_db)
from treid_bot_tg.Utils.logger import logg_info_admin
from treid_bot_tg.Utils.message_text.user_text import welcome_message
from treid_bot_tg.config import ADMIN

# Кнопки
from treid_bot_tg.Keyboards.admin_keyboard import correct_user_keyboard
from treid_bot_tg.Keyboards.users_keyboards import (correct_status, values_keyboards,
                                       time_out_keyboards, back_user_button, reverse_dct_value_inverting)

# Функция для трейдинга
from treid_bot_tg.Parsing.pars_treid import parse_trade_json

router = Router()

@router.message(CommandStart())
async def start_cmd(message: Message):
    # Айди пользователя
    user_id = message.chat.id
    # проверка
    await check_user_db(user_id)
    status = await status_check_user_db(user_id)
    if status:
        await message.answer(f'⏭︎ Приветствую {message.chat.username} ⏮︎'
                             f'\n📊 В Бота для Трейдинга и Тех. Анализа Рынка 📊'
                             f'\n➕ Выберите нужную волюту для Анализа данных➖',
                             reply_markup=values_keyboards)
    else:
        await message.answer(text=welcome_message,
                             reply_markup=await correct_status(user_id)
                             )

# Обработчик заявок на получение доступа для пользователя
@router.callback_query(F.data.startswith('cor_'))
async def corr_user_cmd(call_back: CallbackQuery, bot: Bot):
    await call_back.message.delete()
    await call_back.message.answer('Ждите подтверждения')
    user_id = call_back.message.chat.id
    username = call_back.message.chat.username
    await bot.send_message(int(ADMIN),
                           text='Новый пользователь хочет подтверждения'
                                f'\nID: {user_id}'
                                f'\nИмя: {username}',
                           reply_markup=await correct_user_keyboard(user_id))


# Словарь для Обработки волют
DATA_VALUE = {}


# Обработка Волют
@router.callback_query(F.data.startswith('val_'))
async def value_user_cmd(call_back: CallbackQuery, bot: Bot):
    user_id = call_back.message.chat.id
    value_data = call_back.data.replace('val_', '')
    DATA_VALUE[user_id] = value_data
    try:
        await call_back.message.edit_text('⏱ Выбери Временной Интервал ⏱', reply_markup=time_out_keyboards)
    except Exception as ex:
        await logg_info_admin(log=str(ex), message=call_back.message, bot=bot)
        await call_back.message.answer('Не нужно нажимать кнопки несколько раз !'
                                       '\nПодожди пожалуйста и попробуй чуть позже')

# Обработчик выбора времени
@router.callback_query(F.data.startswith('time_'))
async def time_out_cmd(call_back: CallbackQuery, bot: Bot):
    # Получение нужных данных
    user_id = call_back.message.chat.id
    # Время волюты
    time_data = call_back.data.replace('time_', '')
    # Индекс Волюты
    val = DATA_VALUE.get(user_id)
    # Название Волюты
    value_name = reverse_dct_value_inverting.get(val)

    # Удаление нужных сообщений
    await call_back.message.delete()
    time_message = await call_back.message.answer('⌛️')
    try:
        # Парсинг данных
        data = await parse_trade_json(
            value=val,
            timeframe=time_data
        )

        # Распаковка данных
        # Тех. Индикаторы
        # Индикаторы Резюме
        indicators_rezume = data['data']['indicators']['rezume']
        # Индикаторы Покупка
        indicators_buy = data['data']['indicators']['buy']
        # Индикаторы Продажа
        indicators_sell = data['data']['indicators']['sell']

        # Среднее Резюме
        averages_rezume = data['data']['averages']['rezume']
        # Среднее Покупка
        averages_buy = data['data']['averages']['buy']
        # Среднее Продажа
        averages_sell = data['data']['averages']['sell']

        # Последнее обновление
        lastUpdateTime = data['data']['lastUpdateTime']
        # Выбранное время
        timeframe = data['data']['timeframe']
        new_txt = (f"\t\t💎 Анализ Данных Волюты 💎"
                   f"\n\t{value_name}"
                   f"\n💻 Технический Индикатор 💻"
                   f"\n\t\t➕ Покупают: {indicators_buy} ➕"
                   f"\n\t\t➖ Продают: {indicators_sell} ➖"
                   f"\n\n⚖ Средняя Статистика ⚖"
                   f"\n\t\t➕ Покупают: {averages_buy} ➕"
                   f"\n\t\t➖ Продают: {averages_sell} ➖"
                   f"\n💹 Общий Результат 💹"
                   f"\n\t\t➕ Покупки: {averages_buy+indicators_buy} ➕"
                   f"\n\t\t➖ Продажи: {averages_sell+indicators_sell} ➖"
                   f"\n⏳ Выбранное Время: {timeframe} ⏳"
                   f"\n🕰 Последнее Время Обновления: {lastUpdateTime} 🕰")

        await time_message.delete()

        await call_back.message.answer(text=new_txt, reply_markup=back_user_button)
    except Exception as ex:
        await logg_info_admin(log=str(ex), message=call_back.message, bot=bot)
        await call_back.message.answer('Не нужно нажимать кнопки несколько раз !'
                                       '\nПодожди пожалуйста и попробуй чуть позже')


@router.callback_query(F.data=='back')
async def back_user_cmd(call_back: CallbackQuery, bot: Bot):
    try:
        await call_back.message.edit_text(f'⏭︎ Приветствую {call_back.message.chat.username} ⏮︎'
                             f'\n📊 В Бота для Трейдинга и Тех. Анализа Рынка 📊'
                             f'\n➕ Выберите нужную волюту для Анализа данных➖', reply_markup=values_keyboards )
    except Exception as ex:
        await logg_info_admin(log=str(ex), message=call_back.message, bot=bot)
        await call_back.message.answer('Не нужно нажимать кнопки несколько раз !'
                                   '\nПодожди пожалуйста и попробуй чуть позже')










