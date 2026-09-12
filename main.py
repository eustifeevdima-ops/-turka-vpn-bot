import asyncio
import os

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🔐 Купить VPN — 199 ₽",
                    callback_data="buy"
                )
            ],
            [
                InlineKeyboardButton(
                    text="👤 Мой VPN",
                    callback_data="myvpn"
                )
            ],
            [
                InlineKeyboardButton(
                    text="📖 Инструкция",
                    callback_data="help"
                )
            ]
        ]
    )

    await message.answer(
        "🤖 <b>TURKA VPN</b>\n\n"
        "Быстрый VPN для телефона.\n"
        "Подключение через HAPP.\n\n"
        "Выбери действие:",
        reply_markup=keyboard,
        parse_mode="HTML"
    )


@dp.callback_query()
async def callbacks(callback):
    if callback.data == "buy":
        await callback.message.answer(
            "🔐 <b>VPN на 30 дней</b>\n\n"
            "Стоимость: <b>199 ₽</b>\n\n"
            "После оплаты ты получишь персональную ссылку "
            "для подключения в HAPP.",
            parse_mode="HTML"
        )

    elif callback.data == "myvpn":
        await callback.message.answer(
            "👤 У тебя пока нет активной подписки."
        )

    elif callback.data == "help":
        await callback.message.answer(
            "📖 <b>Как подключить VPN</b>\n\n"
            "1. Установи HAPP.\n"
            "2. Получи ссылку после покупки.\n"
            "3. Добавь ссылку в HAPP.\n"
            "4. Включи VPN.",
            parse_mode="HTML"
        )

    await callback.answer()


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
