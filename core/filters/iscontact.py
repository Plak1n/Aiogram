from aiogram import types
from aiogram.filters import BaseFilter

class IsTrueContact(BaseFilter):
    """
    Custom filter  "is_truecontact"
    """
    async def __call__(self, message: types.Message) -> bool:
        try:
            return message.contact.user_id == message.from_user.id
        except:
            return False