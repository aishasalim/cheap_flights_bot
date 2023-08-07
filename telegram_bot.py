import telebot
from telebot import types
from flight_search import FlightSearch


class Bot:
    def __init__(self, bot_token, data_manager):
        self.data_manager = data_manager
        self.bot = telebot.TeleBot(bot_token)
        self.current_result_index = 0 # Index of the current flight result shown to user
        self.result_messages = [] # List of flight result messages
        self.set_handlers() # Set bot command and message handlers
        
    # Sends list of available IATA codes to user
    def buttons_of_iata(self, chat_id, iata_codes):
        markup = types.InlineKeyboardMarkup()
        for code in iata_codes:
            button_text = f"{code[0]} ({code[1]})"
            button_callback_data = f"iata:{code[1]}"
            button = types.InlineKeyboardButton(text=button_text, callback_data=button_callback_data)
            markup.add(button)
        self.bot.send_message(chat_id, "Available IATA Codes:", reply_markup=markup)

    # Handles incoming city name messages from users
    def handle_city_name(self, message):
        city_name = message.text
        iata_codes = self.data_manager.retrieve_iata_code(city_name)
        self.buttons_of_iata(message.chat.id, iata_codes)
        # self.send_markup(message.chat.id)

    # Starts a flight search based on the destinations in data_manager
    def run_flight_search(self):
        list_of_destinations = self.data_manager.list_of_destinations
        flight_search = FlightSearch(self.data_manager, list_of_destinations)
        self.result_messages = flight_search.format_flights()

    # Sets bot command and message handlers
    def set_handlers(self):
        # Handler for /start command
        @self.bot.message_handler(commands=['start'])
        def startBot(message):
            welcome_message = "This is a bot that will send you on the " \
                              "CHEAPEST airplane ticket in the nearest month! " \
                              "✈️ Type your city name and let's explore the " \
                              "world together! 🌍"
            self.bot.send_message(message.chat.id, welcome_message)

        # Handler for any text message
        @self.bot.message_handler(func=lambda message: True)
        def handle_city_name_message(message):
            self.handle_city_name(message)
            
        # Handler for IATA button callback queries
        @self.bot.callback_query_handler(func=lambda call: call.data.startswith('iata:'))
        def handle_iata_button(function_call):
            iata_code = function_call.data.split(':')[1]
            print(f"IATA Code pressed: {iata_code}")
            self.data_manager.set_selected_iata_code(iata_code)  # Set the selected IATA code in data_manager
            self.run_flight_search()  # Run the flight search immediately after setting the IATA code
            self.bot.answer_callback_query(function_call.id)

        # Handler for any callback query
        @self.bot.callback_query_handler(func=lambda call: True)
        # If the 'Next!' button was pressed
        def response(function_call):
            if function_call.data == "next":
                self.current_result_index += 1 # Move to the next flight result
                if self.current_result_index >= len(self.result_messages): # If there are no more results
                    self.current_result_index = 0  # Reset the result index
                    self.run_flight_search()  # restart the flight search
                self.send_markup(function_call.message.chat.id) # Send the next flight result
                self.bot.answer_callback_query(function_call.id) # Notify Telegram that callback query was processed
            # If the 'Finish!' button was pressed
            elif function_call.data == "finish":
                self.bot.stop_polling() # Stop bot's message polling

    # Sends flight result message to user with inline keyboard button
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
        
    # Starts bot's message polling
    def start_polling(self):
        try:
            self.bot.infinity_polling()  # Start message polling in an infinite loop
        except Exception as e:
            print(f"An error occurred: {e}")

