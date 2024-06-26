from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault

async def set_commands(bot: Bot):
    commands = [
        BotCommand(
            command="start",
            description="Начало работы"
        ),
        BotCommand(
            command="help",
            description="Помощь"
        ),
        BotCommand(
            command="cancel",
            description="Сбросить"
        ),
        BotCommand(
            command="about",
            description="О боте"
        ),
        BotCommand(
            command="inline",
            description="Получение инлайн клавиатуры"
        ),
        BotCommand(
            command="pay",
            description="Купить продукт"
        ),
        BotCommand(
            command="form",
            description="Начать опрос"
        )
    ]
    
    await bot.set_my_commands(commands, BotCommandScopeDefault())