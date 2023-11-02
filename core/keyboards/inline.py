from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from core.utils.callback_data import CallBackInfo

select_macbook = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text="Mackbook Air 15",
            callback_data="apple_macbook_air_15" 
        )
    ],
    [
        InlineKeyboardButton(
            text="Mackbook Pro 15",
            callback_data="apple_macbook_pro_15"
        ) 
    ],
    [
        InlineKeyboardButton(
            text="Mackbook Pro 16",
            callback_data="apple_macbook_pro_16"
        )
    ],
    [
    InlineKeyboardButton(
        text="Link",
        url="https://www.youtube.com"
        ),
    InlineKeyboardButton(
        text="My profile",
        # getting link to user profile by id
        url="tg://user?id=6200739572"
    )
    ]
]
)

def get_inline_keyboard()-> InlineKeyboardMarkup:
    keyborad_builder = InlineKeyboardBuilder()
    keyborad_builder.button(text="Button1",callback_data=CallBackInfo(name="button",number=1))
    keyborad_builder.button(text="Button2", callback_data=CallBackInfo(name="button",number=2))
    keyborad_builder.button(text="Button3", callback_data=CallBackInfo(name="button",number=3))
    keyborad_builder.button(text="Button4(link)", url="youtube.com")
    keyborad_builder.button(text="Button5(profile)", url="tg://user?id=6200739572")
    keyborad_builder.adjust(1,1,2)
    return keyborad_builder.as_markup()
    
    