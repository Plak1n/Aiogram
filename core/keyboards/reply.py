from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, KeyboardButtonPollType
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

test_keyboard_func  = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text="Ряд 1. Кнопка 1"
        ),
        KeyboardButton(
            text="Ряд 1. Кнопка 2"
        ),
        KeyboardButton(
            text="Ряд 1. Кнопка 3"
        ),
    ],
    [
        KeyboardButton(
            text="Ряд 2. Кнопка 1"
        ),
        KeyboardButton(
            text="Ряд 2. Кнопка 2"
        ),
    ],
    [
        KeyboardButton(
            text="Ряд 3. Кнопка 1"
        )
    ]
], resize_keyboard=True, one_time_keyboard=True, input_field_placeholder="Выберите кнопку↓", selective=True)

reply_keyboard = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text="Отправка геолокации",
            request_location=True
        ),
        KeyboardButton(
            text="Отправка контакта",
            request_contact=True
        ),
    ],
    [
        KeyboardButton(
            text="Создать викторину",
            request_poll= KeyboardButtonPollType()
        )    
    ]
], resize_keyboard=True, one_time_keyboard=False, input_field_placeholder="Отправка геолокации, контакта или создание викторины")

def get_reply_keyboard():
    keyboard_builder = ReplyKeyboardBuilder()
    
    keyboard_builder.button(text="Кнопка 1")
    keyboard_builder.button(text="Кнопка 2", request_location=True)
    keyboard_builder.button(text="Кнопка 3", request_contact=True)
    keyboard_builder.button(text="Кнопка 4", request_poll=KeyboardButtonPollType(type="regular"))
    # To set how many buttons in each row
    keyboard_builder.adjust(2,2,1)
    return keyboard_builder.as_markup(resize_keyboard=True, one_time_keyboard=True, input_field_placeholder="KeyboardBuilder")