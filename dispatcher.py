from aiogram import Bot, Dispatcher
from filters import IsOwnerFilter
from config import BOT_TOKEN, BOT_OWNER

# init
bot = Bot(token=BOT_TOKEN, parse_mode="HTML")
dispatcher = Dispatcher(bot)

# activate filters
dispatcher.filters_factory.bind(IsOwnerFilter)
