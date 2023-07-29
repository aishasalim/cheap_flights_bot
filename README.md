# cheap_flights_bot
This is a telegram bot that will search for you the CHEAPEST airplane tickets

As for now, the functionality of the code is following:

1. There is a Google Spreadsheet, having information on the city/IATA code/Maximum price you're ready to spend.
   
<img width="308" alt="SpreadSheets example image" src="https://github.com/aishasalim/cheap_flights_bot/assets/87562264/74e98873-f30f-4463-8f3e-f28fc5dcfe7f">

2. Kiwi API searches for information from the spreadsheet, sorting the maximum price from the table.
   
3. If there are any flights starting today and 30 days in the future for up to 10 days, there will be a notification on the telegram bot. Each time a person presses the "Next!" button triggers a new flight search. 
   
<img width="374" alt="Telegram bot-message" src="https://github.com/aishasalim/cheap_flights_bot/assets/87562264/2db1c02e-5f29-412e-946f-92831775ed26">

4. As for now, whenever there will be no more flight deals that will align with the requirements of the spreadsheets, the button "Finish!" will terminate the code.
<img width="368" alt="Finish Button picture" src="https://github.com/aishasalim/cheap_flights_bot/assets/87562264/a62204dc-e46d-4104-aa96-4723727198e8">

The project is not done yet. I am aiming at doing more functionality so that the user could enter:
1. Passenger number and their type.
2. Maximum stopover number.
3. Flight class.
4. Starting city they are flying from.
5. Data from the Spreadsheets that they could post from the chat.

