# Old aiogram
# import config
# from aiogram import types
# from main import dispatcher

# @dispatcher.message_handler(is_owner=True, commands=["post"])
# async def post_command(message: types.Message):
#     config.IS_POSTING_REQUESTED = True
    
#     await message.answer("Пришлите текст поста (с картинкой или без):")
    
# @dispatcher.message_handler(is_owner=True, commands=["setlink"])
# async def setlink_command(message: types.Message):
#     with open("link.txt", "w+") as file:
#         file.write(message.text.replace("/setlink ", "").strip())
#         file.close()
#     await message.answer("Ссылка успешно сохранена")


# @dispatcher.message_handler(is_owner=True, commands=["getlink"])
# async def getlink_command(message: types.Message):
#     with open("link.txt", "r") as file:
#         content = file.readlines()
    
#     await message.answer(f"Текущая ссылка: {content[0].strip()}")
    
# @dispatcher.message_handler(is_owner=True)
# async def messages_handler(message: types.Message):
#     if config.IS_POSTING_REQUESTED:
#         config.IS_POSTING_REQUESTED = False
        
#         await message.answer("Пост опубликован!")