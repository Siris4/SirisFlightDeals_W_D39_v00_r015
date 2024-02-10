import json
# from pprint import pprint

data_dict_in_json_format = {
  "prices": [
    {
      "city": "Tokyo",
      "iataCode": "HND",
      "lowestPrice": 500,
      "id": 2
    },
    {
      "city": "Sydney",
      "iataCode": "SYD",
      "lowestPrice": 550,
      "id": 3
    },
    {
      "city": "Frankfurt",
      "iataCode": "FRA",
      "lowestPrice": 500,
      "id": 4
    },
    {
      "city": "Cairo",
      "iataCode": "CAI",
      "lowestPrice": 500,
      "id": 5
    },
    {
      "city": "Honolulu",
      "iataCode": "HNL",
      "lowestPrice": 500,
      "id": 6
    },
    {
      "city": "San Francisco",
      "iataCode": "SFO",
      "lowestPrice": 200,
      "id": 7
    },
    {
      "city": "Singapore",
      "iataCode": "SIN",
      "lowestPrice": 500,
      "id": 8
    }
  ]
}

# print(JSON_data)
# pprint((JSON_data))
sheet_data = JSON_data['prices']
prices_of_json_data = JSON_data

# Python Dictionary dict:
# prices = {sheet_data['prices']}   # extra: [0]['city']['iataCode']['lowestPrice']}
# pprint(prices)
