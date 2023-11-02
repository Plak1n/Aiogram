from aiogram import Bot
from aiogram.types import CallbackQuery

async def select_macbook_callback(call: CallbackQuery, bot: Bot):
    device = call.data.split('_')[1]
    model= call.data.split('_')[2]
    year = call.data.split('_')[3]
    await call.message.answer(f"{call.message.chat.first_name} ты выбрал {device} {model} {year}")
    await call.answer()
    
async def callback_query(call: CallbackQuery, bot: Bot):
    print(call.message)
    print(f"\n\n{call.data}")
    await call.message.answer(f"Была нажата инлайн кнопка {call.message.text}")
    await call.answer()