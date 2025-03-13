from aiogram import F, Router, types
from aiogram.fsm.context import FSMContext

import tg_bot.text as text
from tg_bot.states import Gen


trade_router = Router(name="trade")


@trade_router.callback_query(F.data == "buy")
async def input_buy(clbck: types.CallbackQuery, state: FSMContext):
    await state.set_state(Gen.buy)
    await clbck.message.answer(text.buy_text)


@trade_router.callback_query(F.data == "sell")
async def input_sell(clbck: types.CallbackQuery, state: FSMContext):
    await state.set_state(Gen.sell)
    await clbck.message.answer(text.sell_text)


@trade_router.callback_query(F.data == "approve")
async def input_approve(clbck: types.CallbackQuery, state: FSMContext):
    await state.set_state(Gen.approve)
    await clbck.message.answer(text.approve_text)
