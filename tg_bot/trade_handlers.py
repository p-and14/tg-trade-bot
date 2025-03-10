from aiogram import F, Router, types
from aiogram.fsm.context import FSMContext

import tg_bot.kb as kb
import tg_bot.text as text
from tg_bot.states import Gen


trade_router = Router(name="trade")


@trade_router.callback_query(F.data == "buy")
async def input_buy(clbck: types.CallbackQuery, state: FSMContext):
    await state.set_state(Gen.buy)
    await clbck.message.edit_text(text.buy_text)
    await clbck.message.answer(text.exit_to_menu, reply_markup=kb.exit_kb)


@trade_router.callback_query(F.data == "sell")
async def input_sell(clbck: types.CallbackQuery, state: FSMContext):
    await state.set_state(Gen.sell)
    await clbck.message.edit_text(text.sell_text)
    await clbck.message.answer(text.exit_to_menu, reply_markup=kb.exit_kb)


@trade_router.callback_query(F.data == "approve")
async def input_approve(clbck: types.CallbackQuery, state: FSMContext):
    await state.set_state(Gen.approve)
    await clbck.message.edit_text(text.approve_text)
    await clbck.message.answer(text.exit_to_menu, reply_markup=kb.exit_kb)
