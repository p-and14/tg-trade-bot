import asyncio

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.utils.chat_action import ChatActionMiddleware

from config import TG_BOT_TOKEN

from tg_bot.main_handlers import router
from tg_bot.trade_handlers import trade_router
from tg_bot.settings_handlers import settings_router


bot_aio = Bot(token=TG_BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))


async def run_polling(bot: Bot) -> None:
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_routers(router, trade_router, settings_router)
    dp.message.middleware(ChatActionMiddleware())
    
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(run_polling(bot_aio))
