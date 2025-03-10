from aiogram import F, Router, types
from aiogram import types
from aiogram.fsm.context import FSMContext

import tg_bot.kb as kb
import tg_bot.text as text
from tg_bot.states import Gen


settings_router = Router(name="settings")


@settings_router.callback_query(F.data == "wallet_settings")
async def wallet_settings(clbck: types.CallbackQuery, state: FSMContext):
    await state.set_state(Gen.wallet_settings)
    await clbck.message.edit_text(text.wallet_settings_text)
    await clbck.message.answer(text.exit_to_menu, reply_markup=kb.exit_kb)


@settings_router.callback_query(F.data == "buy_settings")
async def buy_settings(clbck: types.CallbackQuery, state: FSMContext):
    await state.set_state(Gen.buy_settings)
    await clbck.message.edit_text(text.buy_settings_text)
    await clbck.message.answer(text.exit_to_menu, reply_markup=kb.exit_kb)


@settings_router.callback_query(F.data == "sell_settings")
async def sell_settings(clbck: types.CallbackQuery, state: FSMContext):
    await state.set_state(Gen.sell_settings)
    await clbck.message.edit_text(text.sell_settings_text)
    await clbck.message.answer(text.exit_to_menu, reply_markup=kb.exit_kb)


@settings_router.callback_query(F.data == "approve_settings")
async def approve_settings(clbck: types.CallbackQuery, state: FSMContext):
    await state.set_state(Gen.approve_settings)
    await clbck.message.edit_text(text.approve_settings_text)
    await clbck.message.answer(text.exit_to_menu, reply_markup=kb.exit_kb)
