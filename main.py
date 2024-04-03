import asyncio
import logging
import psycopg_pool
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.enums import ContentType
from core.settings import settings
from core.handlers.basic import start_bot, stop_bot, get_start, get_photo, get_hello, get_location, get_inline, owner_messsage
from core.handlers.contact import get_true_contact, get_fake_contact
from core.handlers.callback import select_macbook_callback, callback_query
from core.handlers.payments import order, pre_checkout_query, successful_payment, shipping_check
from core.filters.iscontact import IsTrueContact, IsOwner
from core.utils.commands import set_commands
from core.utils.callback_data import CallBackInfo
from core.middlewares.counter_middleware import CounterMiddleware
from core.middlewares.office_hours import OfficeHoursMiddleware
from core.middlewares.db_middleware import DbSession

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

dp = Dispatcher()

#another way to register handlers  
@dp.message(Command("help"))
async def help(message: Message):
    await message.answer("Я проверяю функции и возможности библиотеки aiogram и telegram")

@dp.callback_query(CallBackInfo.filter(F.name== "button"))
async def callback_query(call: CallbackQuery, bot: Bot, callback_data: CallBackInfo):
    # print(call.message)
    await call.message.answer(f"Была нажата инлайн кнопка. Это callback с использование своего класса callbackdata {callback_data}")
    await call.answer()

def create_pool():
    return psycopg_pool.AsyncConnectionPool(f"host=127.0.0.1 port=5432 dbname=users_aiogram user=plak1n password=Danko560x9z "
                                                  f"connect_timeout=60")

async def start():
    # init
    logging.basicConfig(level=logging.INFO, 
                    format="%(asctime)s - [%(levelname)s] - %(name)s - "
                    "%(filename)s.%(funcName)s(%(lineno)d) - %(message)s")

    bot = Bot(token=settings.bots.bot_token, parse_mode="HTML")
    pool_connect = create_pool()
    dp.update.middleware.register(DbSession(pool_connect))
    
    # You need register middleware before handlers
    dp.message.middleware.register(CounterMiddleware())
    dp.update.middleware.register(OfficeHoursMiddleware())
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
    dp.shipping_query.register(shipping_check)
    dp.message.register(order, Command(commands="pay"))
    dp.message.register(successful_payment, F.content_type == ContentType.SUCCESSFUL_PAYMENT)
    dp.callback_query.register(select_macbook_callback, F.data.startswith("apple_"))
    dp.pre_checkout_query.register(pre_checkout_query)

    await set_commands(bot)
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()
    
if __name__ == "__main__":
    asyncio.run(start())