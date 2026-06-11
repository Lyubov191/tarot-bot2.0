import asyncio
import random
import os
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command

TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()

# 🃏 Старшие арканы (22 карты)
major_arcana = [
    "0 Шут — начало, свобода",
    "I Маг — сила воли",
    "II Верховная Жрица — интуиция",
    "III Императрица — изобилие",
    "IV Император — структура",
    "V Иерофант — традиции",
    "VI Влюблённые — выбор",
    "VII Колесница — движение",
    "VIII Сила — контроль эмоций",
    "IX Отшельник — поиск истины",
    "X Колесо Фортуны — перемены",
    "XI Справедливость — баланс",
    "XII Повешенный — пауза",
    "XIII Смерть — трансформация",
    "XIV Умеренность — гармония",
    "XV Дьявол — зависимости",
    "XVI Башня — разрушение",
    "XVII Звезда — надежда",
    "XVIII Луна — иллюзии",
    "XIX Солнце — успех",
    "XX Суд — пробуждение",
    "XXI Мир — завершение"
]

# 🃏 Младшие арканы (56 карт)
suits = ["Жезлы", "Кубки", "Мечи", "Пентакли"]
ranks = [
    "Туз", "2", "3", "4", "5", "6", "7",
    "8", "9", "10", "Паж", "Рыцарь", "Королева", "Король"
]

minor_arcana = [f"{rank} {suit}" for suit in suits for rank in ranks]

# 🎴 Полная колода
deck = major_arcana + minor_arcana


def draw_card():
    card = random.choice(deck)
    reversed_flag = random.choice([True, False])
    return card + (" 🔄" if reversed_flag else "")


@dp.message(Command("start"))
async def start(message: Message):
    await message.answer(
        "🔮 Я Таро-бот\n\n"
        "Команды:\n"
        "/card — 1 карта\n"
        "/spread — расклад 3 карты"
    )


@dp.message(Command("card"))
async def card(message: Message):
    await message.answer(f"Твоя карта:\n\n{draw_card()}")


@dp.message(Command("spread"))
async def spread(message: Message):
    cards = [draw_card() for _ in range(3)]
    await message.answer(
        f"🔮 Расклад:\n\n"
        f"Прошлое: {cards[0]}\n"
        f"Настоящее: {cards[1]}\n"
        f"Будущее: {cards[2]}"
    )


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
