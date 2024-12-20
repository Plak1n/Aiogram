import asyncio
import logging
import psycopg_pool
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.enums import ContentType, ParseMode
from aiogram.client.default import DefaultBotProperties
from core.settings import settings
from core.handlers.basic import start_bot, stop_bot, get_start, get_photo, get_hello, get_location, get_inline, owner_messsage
from core.handlers.contact import get_true_contact, get_fake_contact
from core.handlers.callback import select_macbook_callback, callback_query
from core.handlers.payments import order, pre_checkout_query, successful_payment, shipping_check
from core.handlers import form
from core.filters.iscontact import IsTrueContact, IsOwner
from core.utils.states_form import StepsForm
from core.utils.commands import set_commands
from core.utils.callback_data import CallBackInfo
from core.middlewares.counter_middleware import CounterMiddleware
from core.middlewares.office_hours import OfficeHoursMiddleware
from core.middlewares.db_middleware import DbSession
from core.handlers import apshedule
from datetime import datetime, timedelta
from apscheduler.schedulers.asyncio import AsyncIOScheduler


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
    db = settings.database
    return psycopg_pool.AsyncConnectionPool(f"host={db.host} port={db.port} dbname={db.dbname} "
           f"user={db.user} password={db.password} connect_timeout=60")

async def start():
    # init
    logging.basicConfig(level=logging.INFO, 
                    format="%(asctime)s - [%(levelname)s] - %(name)s - "
                    "%(filename)s.%(funcName)s(%(lineno)d) - %(message)s")

    bot = Bot(token=settings.bots.bot_token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    # A way to schedule apps
    # scheduler = AsyncIOScheduler(timezone="Europe/Minsk")
    # scheduler.add_job(apshedule.send_message_time, trigger='date', run_date=datetime.now()+timedelta(seconds=10),
    #                   kwargs={'bot':bot})
    # scheduler.add_job(apshedule.send_message_crone, trigger='cron', hour=datetime.now().hour, 
    #                   minute=datetime.now().minute+1,
    #                   start_date =datetime.now(),
    #                   kwargs={'bot':bot})
    # scheduler.add_job(apshedule.send_message_interval, trigger='interval', seconds=60,
    #                   kwargs={'bot':bot})
    # scheduler.start()
    pool_connect = create_pool()
    dp.update.middleware.register(DbSession(pool_connect))
    
    # You need register middleware before handlers
    dp.message.middleware.register(CounterMiddleware())
    # Will work only in specific hours
    #dp.update.middleware.register(OfficeHoursMiddleware())
    dp.message.register(get_start, Command(commands=["start"]))
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)
    dp.message.register(form.get_form, Command(commands="form"))
    dp.message.register(form.get_name, StepsForm.GET_NAME)
    dp.message.register(form.get_last_name, StepsForm.GET_LAST_NAME)
    dp.message.register(form.get_age, StepsForm.GET_AGE)
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