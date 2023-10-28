from aiogram import types
from aiogram import Bot

async def get_true_contact(message: types.Message, bot: Bot):
    await message.answer(f"Ты отправил <u>свой</u> контакт.")

async def get_fake_contact(message: types.Message, bot: Bot):
    print(message.contact)
    await message.answer(f"Ты отправил <u>не свой</u> контакт.")
