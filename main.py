import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from core.settings import settings
from core.handlers.basic import start_bot, stop_bot, get_start, get_photo, get_hello
from core.handlers.contact import get_true_contact, get_fake_contact
from core.filters.iscontact import IsTrueContact
from aiogram.enums import ContentType

logging.basicConfig(level=logging.INFO, 
                    format="%(asctime)s - [%(levelname)s] - %(name)s - "
                    "%(filename)s.%(funcName)s(%(lineno)d) - %(message)s")
bot = Bot(token=settings.bots.bot_token, parse_mode="HTML")
    
dp = Dispatcher()
dp.message.register(get_start, Command(commands=['start']))
dp.startup.register(start_bot)
dp.shutdown.register(stop_bot)
# F is magical filter used in aiogram3
dp.message.register(get_photo, F.photo)
dp.message.register(get_hello, F.text.lower() == 'привет')
dp.message.register(get_true_contact,  F.content_type == ContentType.CONTACT, IsTrueContact())
dp.message.register(get_fake_contact, F.content_type == ContentType.CONTACT)
    
async def start():
     # init
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()
    
if __name__ == "__main__":
    asyncio.run(start())