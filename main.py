import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.enums import ContentType
from core.settings import settings
from core.handlers.basic import start_bot, stop_bot, get_start, get_photo, get_hello, get_location, get_inline, owner_messsage
from core.handlers.contact import get_true_contact, get_fake_contact
from core.handlers.callback import select_macbook_callback, callback_query
from core.filters.iscontact import IsTrueContact, IsOwner
from core.utils.commands import set_commands
from core.utils.callback_data import CallBackInfo


logging.basicConfig(level=logging.INFO, 
                    format="%(asctime)s - [%(levelname)s] - %(name)s - "
                    "%(filename)s.%(funcName)s(%(lineno)d) - %(message)s")

bot = Bot(token=settings.bots.bot_token, parse_mode="HTML")

dp = Dispatcher()
dp.message.register(get_start, Command(commands=["start"]))
dp.startup.register(start_bot)
dp.shutdown.register(stop_bot)
# F is magical filter used in aiogram3
dp.message.register(get_photo, F.photo)
dp.message.register(get_hello, F.text.lower() == "привет")
dp.message.register(get_true_contact,  F.content_type == ContentType.CONTACT, IsTrueContact())
dp.message.register(get_fake_contact, F.content_type == ContentType.CONTACT)
dp.message.register(get_location, F.content_type == ContentType.LOCATION)
dp.message.register(get_inline, Command("inline"))
dp.message.register(owner_messsage, F.text.lower() == "админ", IsOwner())
dp.callback_query.register(select_macbook_callback, F.data.startswith("apple_"))

#another way to register handlers  
@dp.message(Command("help"))
async def help(message: Message):
    await message.answer("Я проверяю функции и возможности библиотеки aiogram и telegram")

@dp.callback_query(CallBackInfo.filter(F.name== "button"))
async def callback_query(call: CallbackQuery, bot: Bot, callback_data: CallBackInfo):
    # print(call.message)
    await call.message.answer(f"Была нажата инлайн кнопка. Это callback с использование своего класса callbackdata {callback_data}")
    await call.answer()

async def start():
     # init
    await set_commands(bot)
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()
    
if __name__ == "__main__":
    asyncio.run(start())