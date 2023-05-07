from aiogram import types
from dispatcher import dispatcher
from config import BOT_OWNER, BOT_TOKEN

@dispatcher.message_handler(is_owner=True, commands=["setlink"])
async def setlink_command(message: types.Message):
    print("Staring set")
    with open("link.txt", "w+") as file:
        file.write(message.text.replace("/setlink ", "").strip())
        file.close()
    await message.answer("Ссылка успешно сохранена")


@dispatcher.message_handler(is_owner=True, commands=["getlink"])
async def getlink_command(message: types.Message):
    print("Staring get")
    with open("link.txt", "r") as file:
        content = file.readlines()
    
    await message.answer(f"Текущая ссылка: {content[0].strip()}")