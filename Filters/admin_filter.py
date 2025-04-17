from aiogram.filters import BaseFilter
from aiogram.types import Message, CallbackQuery
from treid_bot_tg.config import ADMIN

class AdminTypeFilter(BaseFilter):
    def __init__(self, id_admin: int):
        self.id_admin = id_admin

    async def __call__(self, message: Message):
        return True if message.from_user.id == ADMIN else False


is_admin_filter = AdminTypeFilter(ADMIN)