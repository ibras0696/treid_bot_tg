import os
import dotenv

dotenv.load_dotenv()

def get_id_admin():
    try:
        return int(os.getenv('ADMIN1'))
    except Exception:
        raise 'Не правильный ID админа или отсутствует'


def get_api_toke_bot():
    try:
        return os.getenv('TOKEN')
    except Exception:
        raise 'Отсутствует Токен или не правильный'


BOT_TOKEN = get_api_toke_bot()

ADMIN = get_id_admin()