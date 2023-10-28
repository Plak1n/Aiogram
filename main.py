import asyncio
import logging
from aiogram import Bot, Dispatcher
from core.handlers.basic import get_start, start_bot, stop_bot
from core.settings import settings


async def start():
    # init
    logging.basicConfig(level=logging.INFO, 
                        format="%(asctime)s - [%(levelname)s] - %(name)s - "
                        "%(filename)s.%(funcName)s(%(lineno)d) - %(message)s")
    bot = Bot(token=settings.bots.bot_token, parse_mode="HTML")
    
    dispatcher = Dispatcher()
    dispatcher.message.register(get_start)
    dispatcher.startup.register(start_bot)
    dispatcher.shutdown.register(stop_bot)
    
    try:
        await dispatcher.start_polling(bot)
    finally:
        await bot.session.close()
    
if __name__ == "__main__":
    asyncio.run(start())