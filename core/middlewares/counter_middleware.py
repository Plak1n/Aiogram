from typing import Any, Awaitable, Callable, Dict
from aiogram import BaseMiddleware
from aiogram.types import Message, TelegramObject

# Middleware can modify, extend or reject processing event in many places of pipeline.
# You need register middleware before handlers
# https://docs.aiogram.dev/en/dev-3.x/dispatcher/middlewares.html

class CounterMiddleware(BaseMiddleware):
    """ This middleware count messages
    """
    def __init__(self) -> None:
        self.counter = 0
    
    async def __call__(
        self, 
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]], 
        event: Message, 
        data: Dict[str, Any]
    ) -> Any:
        self.counter +=1
        data['counter'] = self.counter
        return await handler(event, data)
