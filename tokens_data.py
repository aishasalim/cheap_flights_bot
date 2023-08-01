spreadsheets_id = "YOUR ID FROM GOOGLE SHEETS API"
spreadsheets_api_key = "YOUR API KEY FROM GOOGLE SHEETS API"
sheets_endpoint = f"https://sheets.googleapis.com/v4/spreadsheets" \
                         f"/{spreadsheets_id}/values/Sheet1?key={spreadsheets_api_key}"

kiwi_endpoint = "https://api.tequila.kiwi.com/v2/search"
kiwi_token = "YOUR TOKEN FROM KIWI API"

bot_token = "YOUR TOKEN FOR TELEGRAM BOT"

# will be changed to the empty list in data_manager so that bot would change it with data from user
list_of_destinations = [['city', 'iata code'],
                        ['Toronto', 'YYZ'],
                        ['San Francisco', 'SFO'],
                        ['New York', 'JFK'],
                        ['New York', 'LGA'],
                        ['San Jose', 'SVC'],
                        ['Washington DC', 'DCA']]
