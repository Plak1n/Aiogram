from aiogram import Bot
from core.settings import settings


async def send_message_time(bot: Bot):
    await bot.send_message(settings.bots.bot_owner_id, f"Прошло несколько секунд после старта бота")


async def send_message_crone(bot: Bot):
    await bot.send_message(settings.bots.bot_owner_id, f"Ежедневное сообщение в определенное время")


async def send_message_interval(bot: Bot):
    await bot.send_message(settings.bots.bot_owner_id, f"Сообщение которое отправляется с интервалом")