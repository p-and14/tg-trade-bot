from aiogram import F, Router, types
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

import tg_bot.kb as kb
import tg_bot.text as text
from tg_bot.states import Gen

from implemented import tg_user_dao


router = Router(name="main")


@router.message(Command("start"))
async def start_handler(msg: Message):
    user = tg_user_dao.get_or_create(
        user_id=msg.from_user.id, chat_id=msg.chat.id, username=msg.from_user.username,
        first_name=msg.from_user.first_name, last_name=msg.from_user.last_name)
        
    if not user:
        await msg.answer(text.greet_error.format(name=msg.from_user.full_name))
    else:
        await msg.answer(text.greet.format(name=msg.from_user.full_name), reply_markup=kb.menu)


@router.message(F.text == "Menu")
@router.message(F.text == "Exit to the menu")
@router.message(F.text == "◀️ Exit to the menu")
@router.message(Command("menu"))
async def menu(msg: Message, state: FSMContext):
    await state.set_state(Gen.menu)
    await msg.answer(text.menu, reply_markup=kb.menu)


@router.callback_query(F.data == "menu")
async def menu_data(clbck: types.CallbackQuery):
    await clbck.message.edit_text(text.menu, reply_markup=kb.menu)


@router.callback_query(F.data == "settings")
async def settings(clbck: types.CallbackQuery, state: FSMContext):
    await state.set_state(Gen.settings)
    await clbck.message.edit_text(text.settings_text, reply_markup=kb.settings)
