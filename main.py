from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
import asyncio
import os

TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()

menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📥 VPN olish")],
        [KeyboardButton(text="👤 Profil"), KeyboardButton(text="ℹ️ Yordam")],
    ],
    resize_keyboard=True
)

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "👋 Assalomu alaykum!\n\n"
        "DexxVPN botiga xush kelibsiz!",
        reply_markup=menu
    )

@dp.message(F.text == "📥 VPN olish")
async def vpn(message: Message):
    await message.answer(
        "VPN havolasi:\n\n"
        "https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/refs/heads/main/BLACK_VLESS_RUS_mobile.txt"
    )

@dp.message(F.text == "👤 Profil")
async def profile(message: Message):
    await message.answer(
        f"🆔 ID: {message.from_user.id}\n"
        f"👤 Ism: {message.from_user.full_name}"
    )

@dp.message(F.text == "ℹ️ Yordam")
async def help_menu(message: Message):
    await message.answer(
        "📌 VPN olish uchun \"📥 VPN olish\" tugmasini bosing."
    )

async def main():
    print("DexxVPN ishga tushdi...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())