from aiogram import types
from aiogram.dispatcher.filters import BoundFilter
from config import BOT_OWNER


class IsOwnerFilter(BoundFilter):
    """
    Custom filter  "is_owner"
    """
    key = "is_owner"
    
    def __init__(self, is_owner):
        self.is_owner = is_owner
    
    async def check(self, message: types.Message):
        print(message.from_user.id)
        print(message.from_user.id == BOT_OWNER)
        return message.from_user.id == BOT_OWNER
        