import asyncio
import random
import os
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart

TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Полная колода Таро
major_arcana = [
    "Шут — начало, свобода",
    "Маг — сила, действие",
    "Верховная Жрица — интуиция",
    "Императрица — изобилие",
    "Император — власть",
    "Иерофант — традиции",
    "Влюблённые — выбор",
    "Колесница — движение",
    "Сила — контроль эмоций",
    "Отшельник — поиск истины",
    "Колесо Фортуны — судьба",
    "Справедливость — баланс",
    "Повешенный — пауза",
    "Смерть — трансформация",
    "Умеренность — гармония",
    "Дьявол — зависимость",
    "Башня — разрушение",
    "Звезда — надежда",
    "Луна — иллюзии",
    "Солнце — успех",
    "Суд — пробуждение",
    "Мир — завершение"
]

suits = ["Жезлы", "Кубки", "Мечи", "Пентакли"]
ranks = [
    "Туз", "2", "3", "4", "5", "6", "7",
    "8", "9", "10", "Паж", "Рыцарь", "Королева", "Король"
]

# Генерация младших арканов
minor_arcana = [f"{rank} {suit}" for suit in suits for rank in ranks]

# Объединяем всё
deck = major_arcana + minor_arcana

def get_random_card():
    card = random.choice(deck)
    
    # 50% шанс перевёрнутой карты
    reversed_card = random.choice([True, False])
    
    if reversed_card:
        return f"{card} (перевёрнутая) 🔄"
    return card

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "🔮 Привет! Я бот-гадалка Таро.\n\n"
        "Напиши /card чтобы вытянуть карту\n"
        "Напиши /spread для расклада на 3 карты"
    )

@dp.message(lambda message: message.text == "/card")
async def get_card(message: Message):
    card = get_random_card()
    await message.answer(f"Твоя карта:\n\n{card}")

@dp.message(lambda message: message.text == "/spread")
async def spread(message: Message):
    cards = [get_random_card() for _ in range(3)]
    
    await message.answer(
        "🔮 Расклад на 3 карты:\n\n"
        f"Прошлое: {cards[0]}\n"
        f"Настоящее: {cards[1]}\n"
        f"Будущее: {cards[2]}"
    )

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())