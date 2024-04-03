from aiogram import Bot
from aiogram.types import Message, LabeledPrice, PreCheckoutQuery, InlineKeyboardButton, \
    InlineKeyboardMarkup, ShippingOption, ShippingQuery

keyboards = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text="Оплатить заказ",
            pay=True
        )
    ],
    [
        InlineKeyboardButton(
            text="Link",
            url="https://example.com"
        )
    ]
    ]
    )

BY_SHIPPING = ShippingOption(
    id="by",
    title="Доставка в Беларусь почтой",
    prices=[
        LabeledPrice(
            label="Доставка Белпочтой",
            amount=500
        ),
    ]
)

BY_SHIPPING_S = ShippingOption(
    id="by_sdek",
    title="Доставка в Беларусь СДЭК",
    prices=[
        LabeledPrice(
            label="Доставка СДЭК",
            amount=500
        )
    ]
)

RU_SHIPPING_S = ShippingOption(
    id="by_sdek",
    title="Доставка в Россию СДЭК",
    prices=[
        LabeledPrice(
            label="Доставка СДЭК",
            amount=500
        )
    ]
)

RU_SHIPPING = ShippingOption(
    id="ru",
    title="Доставка в Россию",
    prices=[
        LabeledPrice(
            label="Доставка почтой России",
            amount=1000
        ),
    ]
)

CITIES_SHIPPING = ShippingOption(
    id="capitals",
    title="Быстрая доставка по городу",
    prices=[
        LabeledPrice(
            label="Доставка курьером",
            amount=1500
        )
    ]
)

async def shipping_check(shipping_query: ShippingQuery, bot: Bot):
    shipping_options = []
    countries = ["BY","RU"]
    cities = ["Минск", "Москва", "Minsk", "Moscow"]
    
    if shipping_query.shipping_address.country_code not in countries:
        return await bot.answer_shipping_query(shipping_query.id, ok=False,
                                               error_message="Доставка в вашу страну не доступна")

    if shipping_query.shipping_address.country_code == "BY":
        shipping_options.append(BY_SHIPPING)
        shipping_options.append(BY_SHIPPING_S)
    
    if shipping_query.shipping_address.country_code == "RU":
        shipping_options.append(RU_SHIPPING)
        shipping_options.append(RU_SHIPPING_S)
    
    if shipping_query.shipping_address.city in cities:
        shipping_options.append(CITIES_SHIPPING)
        
    await bot.answer_shipping_query(shipping_query.id, ok=True, shipping_options=shipping_options)
    
async def order(messsage: Message, bot: Bot):
    await bot.send_invoice(
        chat_id=messsage.chat.id,
        title="Тестовая покупка через Telegram", #32 chars
        description="тестовое описание", # 256 chars
        payload="Testing payment capabilities", # internal information. User dont see it. Example using: collect data of payments
        provider_token="381764678:TEST:72488",
        currency="rub",
        prices= [
            LabeledPrice(
                label="Подписка на группу",
                amount=10000
            ),
            LabeledPrice(
                label="НДС",
                amount=2000
            ),
            LabeledPrice(
                label="Скидка", 
                amount= -2000
            ),
            LabeledPrice(
                label="Бонус",
                amount=-1000
            )
        ],
        max_tip_amount=5000,
        suggested_tip_amounts=[1000,2000,3000,4000],
        start_parameter="plak1n_payments",
        # If left empty, forwarded copies of the sent message will have a Pay button,
        # allowing multiple users to pay directly from the forwarded message
        provider_data=None, # data to provider
        photo_url="https://avatars.mds.yandex.net/i?id=2fedf0f5da0d8104b8df265dedb1d99abc46d0ef-10636720-images-thumbs&n=13",
        photo_size=100,
        photo_width=479,
        photo_height=320,
        need_name=False, # if needs full name of user
        need_email=False,
        need_phone_number=False,
        need_shipping_address=False, # to deliver
        send_phone_number_to_provider=False, # if provider asks
        send_email_to_provider=True,
        is_flexible=True, # if final price depends on delivery
        disable_notification=False,
        protect_content=False, # protection from copying, forwarding, 
        reply_to_message_id=None,
        allow_sending_without_reply=True,
        reply_markup=keyboards,
        request_timeout=15
    )


async def pre_checkout_query(pre_checkout_query: PreCheckoutQuery, bot: Bot):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


async def successful_payment(message: Message):
    msg = f"Спасибо за оплату {message.successful_payment.total_amount / 100} {message.successful_payment.currency}." \
          f"\r\nНаш менеджер получил заявку и уже набирает ваш номер телефона" \
          f"\r\nПока вы можете скачать цифровую версию нашего продукта https://test_link.by"
    await message.answer(msg)