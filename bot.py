
import logging
import json
import os
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import executor
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
API_TOKEN = os.getenv('TELEGRAM_API_TOKEN')

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Create the main menu
main_menu = ReplyKeyboardMarkup(resize_keyboard=True)
button_books = KeyboardButton('📚 Список книг')
main_menu.add(button_books)

# Load books from books.json
with open('books.json', 'r', encoding='utf-8') as f:
    books = json.load(f)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Привет! Я бот, который поможет тебе получить доступ к книгам.", reply_markup=main_menu)

@dp.message_handler(lambda message: message.text == '📚 Список книг')
async def send_book_list(message: types.Message):
    response = "Доступные книги:\n\n"
    for book_name, book_link in books.items():
        response += f"<a href=\"{book_link}\">{book_name}</a>\n"
    await message.reply(response, parse_mode="HTML")

@dp.message_handler()
async def handle_unknown_message(message: types.Message):
    await message.reply("Пожалуйста, выберите один из доступных вариантов меню.", reply_markup=main_menu)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
