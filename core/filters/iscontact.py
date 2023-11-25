from typing import Any
from aiogram import types
from aiogram.filters import BaseFilter
from core.settings import settings

class IsTrueContact(BaseFilter):
    """
    Custom filter  "is_truecontact"
    """
    async def __call__(self, message: types.Message) -> bool:
        try:
            return message.contact.user_id == message.from_user.id
        except:
            return False
        
class IsOwner(BaseFilter):
    """
    Custom filter "is_owner"
    """
    async def __call__(self, message: types.Message) -> bool:
        try:
            return message.from_user.id == settings.bots.bot_owner_id
        except:
            return False