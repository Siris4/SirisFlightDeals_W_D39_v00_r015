#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from pprint import pprint

from data_manager_W_D39_v00_r015 import DataManager
#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
data_manager = DataManager()  # needs () because it is a Class
sheet_data = data_manager.get_request_for_getting_destination_data()


# TODO: Authenticate with a Bearer Token
# TODO: Ensure all sensitive data is extracted and created into an Environment Variable, above here.


print("Sheet Data: ")
pprint(sheet_data)

#  5. In main.py check if sheet_data contains any values for the "iataCode" key.
#  If not, then the IATA Codes column is empty in the Google Sheet.
#  In this case, pass each city name in sheet_data one-by-one
#  to the FlightSearch class to get the corresponding IATA code
#  for that city using the Flight Search API.
#  You should use the code you get back to update the sheet_data dictionary.
def iataCode_Checking():
    if sheet_data[0]["iataCode"] == "":  # take out 'is None'
        print("iataCode data is empty")
        from flight_search_W_D39_v00_r015 import FlightSearch
        flight_search = FlightSearch()
        for row in sheet_data:    #use the response from the FlightSearch class to update the sheet_data dict
            row["iataCode"] = flight_search.get_destination_code(row["city"])
        print(f"sheet_data:\n {sheet_data}")

        data_manager.destination_data = sheet_data
        data_manager.update_destination_codes()

iataCode_Checking()



# previous code:
'''
ef iataCode_Checking():
    if sheet_data[0]["iataCode"] == "":  # take out 'is None'
        print("iataCode data is empty")
        return
        if "prices" not in sheet_data:
            print(f"prices key was checked. prices key is missing.")
        elif "prices" in sheet_data:
            print(f"prices key was found inside!")
    elif sheet_data["iataCode"] is not None:
        print("iataCode data found inside!")
        for item in sheet_data['prices']:
            if "iataCode" not in item or item["iataCode"] is None:
                print("An item is missing an iataCode within 'prices'.")
            else:
                print(f"iataCode data found inside: {item['iataCode']}")
                '''