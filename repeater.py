import requests

API_LINK = "https://api.telegram.org/bot5500847779:AAGvLeoWW4eJccjF767IU8tR1tXpM0WVYyQ"

UPDATES = requests.get(API_LINK + "/getUpdates?offset=-1").json()

print(UPDATES)

message = UPDATES['result'][0]['message']
chat_id = message['from']['id']
text = message['text']

# not used anymore
#sent_message = requests.get(API_LINK + f'/sendMessage?chat_id={chat_id}&text=Привет, ты написал(-a) {text}')