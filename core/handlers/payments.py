from aiogram import Bot
from aiogram.types import Message, LabeledPrice

async def order(messsage: Message, bot: Bot):
    await bot.send_invoice(
        chat_id=messsage.chat.id,
        title="Тестовая покупка через Telegram", #32 chars
        description="тестовое описание", # 256 chars
        payload="Testing payment capabilities", # internal information. User dont see it. Example using: collect data of payments
        provider_token="381764678:TEST:72488",
        currency="BYN",
        prices= [
            LabeledPrice(
                label="Подписка на группу",
                amount=1000
            ),
            LabeledPrice(
                label="НДС",
                amount=200
            ),
            LabeledPrice(
                label="Скидка",
                amount= -200
            ),
            LabeledPrice(
                label="Бонус",
                amount=-100
            )
        ],
        max_tip_amount=500,
        suggested_tip_amounts=[100,200,300,400],
        start_parameter='plak1n_payments',
        # If left empty, forwarded copies of the sent message will have a Pay button,
        # allowing multiple users to pay directly from the forwarded message
        provider_data=None, # data to provider
        photo_url="https://avatars.mds.yandex.net/i?id=2fedf0f5da0d8104b8df265dedb1d99abc46d0ef-10636720-images-thumbs&n=13",
        photo_size=100,
        photo_width=479,
        photo_height=320,
        need_name=True, # if needs full name of user
        need_email=True,
        need_phone_number=True,
        need_shipping_address=False, # to deliver
        send_phone_number_to_provider=False, # if providerasks
        send_email_to_provider=True,
        is_flexible=False, 
        disable_notification=False,
        protect_content=False, # protection from copying, forwarding, 
        reply_to_message_id=None,
        allow_sending_without_reply=True,
        reply_markup=None,
        request_timeout=15,
        
    )
    