from aiogram.fsm.state import StatesGroup, State


class UsersValueState(StatesGroup):
    value = State()
    time_out = State()