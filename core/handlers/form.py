from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from core.utils.states_form import StepsForm

async def get_form(message: Message, state: FSMContext):
    await message.answer(f"{message.from_user.first_name}, начинаем заполнять анкету. Введите свое имя")
    await state.set_state(StepsForm.GET_NAME)


async def get_name(message: Message, state: FSMContext):
    await message.answer(f"Твоё имя:\r\n{message.text}\r\n Теперь введи фамилию")
    await state.update_data(name=message.text)
    await state.set_state(StepsForm.GET_LAST_NAME)


async def get_last_name(message: Message, state: FSMContext):
    await message.answer(f"Твоя фамилия:\r\n{message.text}\r\n Теперь введи возраст")
    await state.update_data(last_name=message.text)
    await state.set_state(StepsForm.GET_AGE)


async def get_age(message: Message, state: FSMContext):
    await message.answer(f"Твой возраст:\r\n{message.text}\r\n")
    context_data = await state.get_data()
    await message.answer(f"Cохранённые данные в машие состояний \r\n{str(context_data)}")
    name = context_data.get("name")
    last_name = context_data.get("last_name")
    data_user = f"Вот твои данные\r\n" \
                f"Имя {context_data.get('name')} \r\n" \
                f"Фамилия {context_data.get('last_name')}\r\n" \
                f"Фамилия {message.text}"
    await message.answer(data_user)
    await state.clear()    