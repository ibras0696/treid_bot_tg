from aiogram import Bot
from aiogram.types import Message
from treid_bot_tg.config import ADMIN
from datetime import datetime

now = datetime.now()

async def logg_info_admin(log:str, message: Message, bot: Bot):
    try:
        await bot.send_message(ADMIN, text=f'Ошибка: {log}'
                                                          f'\nПользователь: {message.chat.id}'
                                                          f'\nНик: {message.chat.username}'
                                                          f'\nДата: {now.strftime("%d.%m.%Y %H:%M:%S")}')
    except Exception as ex:
        raise ex