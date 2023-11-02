from aiogram.filters.callback_data import CallbackData

class CallBackInfo(CallbackData, prefix='callback'):
    name: str
    number: int
    