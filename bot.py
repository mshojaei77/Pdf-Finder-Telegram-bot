import logging
import os
from telebot import TeleBot
from googlesearch import search

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Initialize the Telegram bot with your token from environment variables
bot = TeleBot(os.getenv("TELEGRAM_BOT_TOKEN"))

def send_pdf(chat_id, url):
    try:
        bot.send_document(chat_id, url)
        logger.info(f"PDF sent to user {chat_id} from URL: {url}")
    except Exception as e:
        logger.error(f"Failed to send PDF to user {chat_id}. Error: {e}")

def search_and_send_book_pdf(chat_id, book_name):
    counter = 0
    while counter < 20:
        query = f'"{book_name}" filetype:pdf'
        search_results = search(query, advanced=True, num_results=10)
        
        for result in search_results:
            counter += 1
            if result.url.endswith('.pdf'):
                send_pdf(chat_id, result.url)
    bot.send_message(chat_id, f"✅ Search for `{book_name}` complete.",   parse_mode='Markdown')

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, " Welcome! ✨ Please enter the **book name** you want to search for.",  parse_mode='Markdown')

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    book_name = message.text
    bot.reply_to(message, f" Searching for `{book_name}` and sending PDFs ⏳ ",   parse_mode='Markdown')
    search_and_send_book_pdf(message.chat.id, book_name)

if __name__ == "__main__":
    bot.polling()
