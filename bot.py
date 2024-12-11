import logging
import os
from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Configure logging
logging.basicConfig(level=logging.INFO)

# Load API token
API_TOKEN = os.getenv('TELEGRAM_API_TOKEN')
if not API_TOKEN:
    raise ValueError("TELEGRAM_API_TOKEN is not set. Please check your environment variables.")

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Create the main menu
main_menu = ReplyKeyboardMarkup(resize_keyboard=True)
button_books = KeyboardButton('📚 Список книг')
main_menu.add(button_books)

# Dictionary to store book links
books = {
    "Питер Моузес - Исполнение библейских пророчеств": "http://www.blagovestnik.org/books/00139.htm",
    "Каргель И.В. - Лекции о втором пришествии Господа Иисуса Христа": "http://www.blagovestnik.org/books/00417.htm",
    "И. В. Каргель - Толкование на Книгу Откровение": "http://www.blagovestnik.org/books/00260.htm",
    "YouTube проповедь - А Копылов. МСЦ ЕХБ - 'Израиль. Признаки пришествия': "https://www.youtube.com/watch?v=8xvFY7FrwEk&ab_channel=%D0%95%D0%B2%D0%B0%D0%BD%D0%B3%D0%B5%D0%BB%D1%8C%D1%81%D0%BA%D0%B0%D1%8F%D0%92%D0%B5%D1%81%D1%82%D1%8C",
    
    # Add more books here as needed
}

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """Send a welcome message and show the main menu."""
    await message.reply("Книги, статьи, проповеди о последнем времени...", reply_markup=main_menu)

@dp.message_handler(lambda message: message.text == '📚 Список книг')
async def send_book_list(message: types.Message):
    """Send the list of available books as clickable links."""
    response = "\u0414\u043e\u0441\u0442\u0443\u043f\u043d\u044b\u0435 \u043a\u043d\u0438\u0433\u0438:\n\n"
    for book_name, book_link in books.items():
        response += f"<a href=\"{book_link}\">{book_name}</a>\n"
    await message.reply(response, parse_mode="HTML")

@dp.message_handler()
async def handle_unknown_message(message: types.Message):
    """Handle unknown messages."""
    await message.reply("\u041f\u043e\u0436\u0430\u043b\u0443\u0439\u0441\u0442\u0430, \u0432\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043e\u0434\u0438\u043d \u0438\u0437 \u0434\u043e\u0441\u0442\u0443\u043f\u043d\u044b\u0445 \u0432\u0430\u0440\u0438\u0430\u043d\u0442\u043e\u0432 \u043c\u0435\u043d\u044e.", reply_markup=main_menu)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
