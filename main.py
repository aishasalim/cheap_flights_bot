from data_manager import DataManager
from telegram_bot import Bot
from tokens_data import sheets_endpoint, kiwi_endpoint, kiwi_token, bot_token

# Create an instance of DataManager, pass the necessary parameters
data_manager = DataManager(sheets_endpoint, kiwi_endpoint, kiwi_token)

# Create an instance of BotHandler, pass the necessary parameters
bot_handler = Bot(bot_token, data_manager)
bot_handler.start_polling()
