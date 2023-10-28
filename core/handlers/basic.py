from aiogram import Bot
from aiogram import types
from core.settings import settings

async def get_start(message: types.Message, bot: Bot):
    await bot.send_message(message.from_user.id, f"<b>Привет {message.from_user.first_name} Я тестовый бот написанный на aiogram</b>")
    # Aiogram helpfull methods
    await message.answer(f"<s>Привет {message.from_user.first_name}</s>")
    await message.reply(f"<tg-spoiler>Привет {message.from_user.first_name}</tg-spoiler>")

async def start_bot(bot: Bot):
    await bot.send_message(settings.bots.bot_owner_id, text="Бот запущен")
    
async def stop_bot(bot: Bot):
    await bot.send_message(settings.bots.bot_owner_id, text="Бот остановлен")
