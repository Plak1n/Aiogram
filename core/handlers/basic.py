from aiogram import Bot
from aiogram.types import Message
from core.settings import settings
from core.keyboards.reply import reply_keyboard, get_reply_keyboard
from core.keyboards.inline import select_macbook, get_inline_keyboard

async def get_inline(message: Message, bot:Bot):
    await message.answer(f"Привет {message.from_user.first_name}. Показываю инлайн клавиатуру", reply_markup=select_macbook)

async def get_start(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id, f"<b>Привет {message.from_user.first_name} Я тестовый бот написанный на aiogram</b>")
    # Aiogram helpfull methods
    await message.answer(f"<s>Привет {message.from_user.first_name}</s>", reply_markup=get_inline_keyboard())
    await message.reply(f"<tg-spoiler>Привет {message.from_user.first_name}</tg-spoiler>", reply_markup=reply_keyboard)
    
async def start_bot(bot: Bot):
    await bot.send_message(settings.bots.bot_owner_id, text="Бот запущен")
    
async def stop_bot(bot: Bot):
    await bot.send_message(settings.bots.bot_owner_id, text="Бот остановлен")

async def get_photo(message: Message, bot: Bot):
    await message.answer(f"Ты отправил картинку сохраню её себе")
    file = await bot.get_file(message.photo[-1].file_id)
    await bot.download_file(file.file_path, 'photo.jpg')

async def get_hello(message: Message, bot: Bot):
    await message.answer(f"И тебе привет")
    
async def get_location(message: Message, bot: Bot):
    await message.answer(f"Ты отправил локацию \r\a"
                         f"{message.location.latitude}\r\n{message.location.longitude}")
    
async def owner_messsage(message: Message, bot: Bot):
    await message.answer(f"Это сообщение только для создателя бота")