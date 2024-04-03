from datetime import datetime
from typing import Any, Awaitable, Callable, Dict
from aiogram import BaseMiddleware
from aiogram.types import Message, TelegramObject

def office_hours() -> bool:
    return datetime.now().weekday() in (0,1,2,3,4) and datetime.now().hour in ([i for i in (range(8,19))])

class OfficeHoursMiddleware(BaseMiddleware):
    def __init__(self) -> None:
        super().__init__()

    async def __call__(
        self, 
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]], 
        event: TelegramObject, 
        data: Dict[str, Any]
    ) -> Any:
        if office_hours():
           return await handler(event, data)

        # await event.answer("Время работы бота: \r\nПн-пт с 8 до 18. Приходите в рабочие часы.")