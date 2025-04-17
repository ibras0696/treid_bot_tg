import asyncio
from aiogram import  Bot, Dispatcher


from treid_bot_tg.Handlers import router
from treid_bot_tg.DataBase.models import create_table
from treid_bot_tg.config import BOT_TOKEN


async def main():
    # Бот и подключение к Токен
    bot = Bot(BOT_TOKEN)
    # Основной диспетчер для выполнения команд
    dp = Dispatcher()
    dp.include_router(router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    # Логирование процессов
    # logging.basicConfig(level=logging.INFO)
    try:
        create_table()
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Выход')
