from aiogram.fsm.state import StatesGroup, State


class Gen(StatesGroup):
    error = State()
    menu = State()
    settings = State()
    wallet_settings = State()
    add_wallet = State()
    create_wallet = State()
    delete_wallet = State()
    buy_settings = State()
    sell_settings = State()
    approve_settings = State()
    buy = State()
    sell = State()
    approve = State()
