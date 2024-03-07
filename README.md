# Pdf Finder Telegram bot

This is a Telegram bot that allows users to search for book PDFs by entering the book name. The bot uses the Google Search API to find relevant PDF files and sends them to the user via Telegram.

## Features

- Search for book PDFs by entering the book name
- Automatically sends the first 20 PDF files found in the search results
- Supports Markdown formatting in bot messages
- Logging functionality to track bot activity and errors

## Prerequisites

Before running the bot, make sure you have the following:

- Python 3.x installed
- Required Python packages: `telebot` and `googlesearch`
- Telegram Bot API token (obtain it from the BotFather on Telegram)

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/mshojaei77/Pdf-Finder-Telegram-bot.git
   ```

2. Install the required Python packages:

   ```
   pip install telebot googlesearch
   ```

3. Set up the environment variable for your Telegram Bot API token:

   ```
   export TELEGRAM_BOT_TOKEN=your-bot-token-here
   ```

   Replace `your-bot-token-here` with your actual bot token.

## Usage

1. Start the bot by running the Python script:

   ```
   python bot.py
   ```

2. Open the Telegram app and search for your bot using its username.

3. Start a conversation with the bot by sending the `/start` or `/help` command.

4. Enter the name of the book you want to search for.

5. The bot will search for relevant PDF files and send them to you automatically.

## Configuration

- The bot is configured to search for a maximum of 20 PDF files per book search. You can modify this limit by changing the value of `counter` in the `search_and_send_book_pdf` function.

- The logging level is set to `INFO` by default. You can change it to `DEBUG`, `WARNING`, `ERROR`, or `CRITICAL` based on your requirements.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- This bot uses the [Telegram Bot API](https://core.telegram.org/bots/api) and the [Google Search API](https://developers.google.com/custom-search/v1/overview).
- Thanks to the developers of the `telebot` and `googlesearch` Python packages for their contributions.
