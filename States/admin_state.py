from aiogram.fsm.state import StatesGroup, State


# Состояния для добавления пользователя
class AdminAddDBUser(StatesGroup):
    user_id = State()
    status = State()