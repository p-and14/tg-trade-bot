import asyncio

from aiogram import F, Router, types, flags
from aiogram import types
from aiogram.fsm.context import FSMContext

from eth_account.signers.local import LocalAccount

from cryptography.fernet import Fernet

from config import SALT

import tg_bot.kb as kb
import tg_bot.text as text
from tg_bot.states import Gen

from web3_manager import web3

from implemented import tg_user_dao, wallet_dao
from functions import generate_key


settings_router = Router(name="settings")


@settings_router.callback_query(F.data == "wallet_settings")
async def wallet_settings(clbck: types.CallbackQuery, state: FSMContext):
    await state.set_state(Gen.wallet_settings)
    wallet = wallet_dao.get_one_by_tg_user_id(clbck.from_user.id)

    if wallet:
        balance = round(web3.from_wei(await web3.eth.get_balance(wallet.address), "ether"), 4)
        send_text = text.wallet_available_settings_text.format(address=wallet.address, balance=balance)
        reply_markup = kb.wallet_available
    else:
        send_text = text.wallet_not_available_settings_text
        reply_markup = kb.wallet_not_available
    
    await clbck.message.edit_text(send_text, reply_markup=reply_markup, parse_mode="html")


@settings_router.callback_query(F.data == "add_wallet")
async def add_wallet(clbck: types.CallbackQuery, state: FSMContext):
    wallet = wallet_dao.get_one_by_tg_user_id(clbck.from_user.id)

    if wallet:
        await clbck.message.answer(text.wallet_exist_text)
    else:
        await state.set_state(Gen.add_wallet)
        await clbck.message.edit_text(text.wallet_pr_key_texts[0])
        await asyncio.sleep(2)
        await clbck.message.answer(text.exit_to_menu, reply_markup=kb.exit_kb)


@settings_router.message(Gen.add_wallet)
@flags.chat_action("typing")
async def input_pr_key(msg: types.Message, state: FSMContext):
    if not await web3.is_connected():
        await msg.answer(text.web3_error)
    else:
        pr_key = msg.text
        try:
            acc: LocalAccount = web3.eth.account.from_key(private_key=pr_key)
        except Exception:
            await msg.answer(text.wallet_pr_key_error)
        else:
            user = tg_user_dao.get_or_create(
                user_id=msg.from_user.id, chat_id=msg.chat.id, username=msg.from_user.username,
                first_name=msg.from_user.first_name, last_name=msg.from_user.last_name)
            if user is None:
                await msg.answer(text.greet_error.format(name=msg.from_user.full_name))
            else:
                key = generate_key(str(msg.from_user.id), SALT)
                pr_key = Fernet(key).encrypt(acc._private_key).decode()
                wallet = wallet_dao.create(address=acc.address, private_key=pr_key, tg_user=user)
                await state.set_state(Gen.wallet_settings)

                if wallet is None:
                    await msg.answer(text.wallet_add_error)
                    await msg.answer(text.wallet_not_available_settings_text, reply_markup=kb.wallet_not_available)
                else:
                    await msg.answer(text.wallet_pr_key_texts[1])
                    balance = round(web3.from_wei(await web3.eth.get_balance(wallet.address), "ether"), 4)
                    await msg.answer(
                        text.wallet_available_settings_text.format(
                            address=wallet.address, balance=balance
                            ),
                            reply_markup=kb.wallet_available)


@settings_router.callback_query(F.data == "create_wallet")
async def create_wallet(clbck: types.CallbackQuery, state: FSMContext):
    await state.set_state(Gen.create_wallet)
    await clbck.message.answer(text.wallet_create_text)


@settings_router.callback_query(F.data == "delete_wallet")
async def delete_wallet(clbck: types.CallbackQuery, state: FSMContext):
    await state.set_state(Gen.delete_wallet)
    await clbck.message.answer(text.wallet_delete_text)


@settings_router.callback_query(F.data == "buy_settings")
async def buy_settings(clbck: types.CallbackQuery, state: FSMContext):
    await state.set_state(Gen.buy_settings)
    await clbck.message.answer(text.buy_settings_text)


@settings_router.callback_query(F.data == "sell_settings")
async def sell_settings(clbck: types.CallbackQuery, state: FSMContext):
    await state.set_state(Gen.sell_settings)
    await clbck.message.answer(text.sell_settings_text)


@settings_router.callback_query(F.data == "approve_settings")
async def approve_settings(clbck: types.CallbackQuery, state: FSMContext):
    await state.set_state(Gen.approve_settings)
    await clbck.message.answer(text.approve_settings_text)
