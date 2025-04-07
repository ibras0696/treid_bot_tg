import asyncio
import logging
import os
from logging import BASIC_FORMAT

from aiogram import  Bot, Dispatcher
import dotenv

from Handlers import router


async def main():
    dotenv.load_dotenv()
    # Бот и подключение к Токен
    bot = Bot(os.getenv('TOKEN'))
    # Основной диспетчер для выполнения команд
    dp = Dispatcher()
    dp.include_router(router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    # Логирование процессов
    # logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Выход')
