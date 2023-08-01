import telebot
from telebot import types
from flight_search import FlightSearch


class Bot:
    def __init__(self, bot_token, data_manager):
        self.data_manager = data_manager
        self.bot = telebot.TeleBot(bot_token)
        self.current_result_index = 0
        self.result_messages = []
        self.set_handlers()

    def run_flight_search(self):
        list_of_destinations = self.data_manager.list_of_destinations
        flight_search = FlightSearch(self.data_manager, list_of_destinations)
        self.result_messages = flight_search.format_flights()

    def set_handlers(self):
        @self.bot.message_handler(commands=['start'])
        def startBot(message):
            welcome_message = "This is a bot that will send you to the cheapest place you want! Type your city name."
            self.bot.send_message(message.chat.id, welcome_message)

        @self.bot.message_handler(func=lambda message: True)
        def handle_city_name(message):
            city_name = message.text
            self.data_manager.retrieve_iata_code(city_name)
            self.run_flight_search()
            self.send_markup(message.chat.id)

        @self.bot.callback_query_handler(func=lambda call: True)
        def response(function_call):
            if function_call.data == "next":
                self.current_result_index += 1
                if self.current_result_index >= len(self.result_messages):
                    self.current_result_index = 0
                    self.run_flight_search()  # restart the flight search
                self.send_markup(function_call.message.chat.id)
                self.bot.answer_callback_query(function_call.id)
            elif function_call.data == "finish":
                self.bot.stop_polling()

    def send_markup(self, chat_id):
        markup = types.InlineKeyboardMarkup()
        if self.current_result_index == len(self.result_messages) - 1:
            button_text = 'Finish!'
            callback_data = 'finish'
        else:
            button_text = 'Next!'
            callback_data = 'next'
        button_next = types.InlineKeyboardButton(text=button_text, callback_data=callback_data)
        markup.add(button_next)
        self.bot.send_message(chat_id, self.result_messages[self.current_result_index],
                              parse_mode='HTML', reply_markup=markup)

    def start_polling(self):
        try:
            self.bot.infinity_polling()
        except Exception as e:
            print(f"An error occurred: {e}")
