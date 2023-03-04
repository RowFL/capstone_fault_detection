import requests
import time

# Channel ID and API Key
channel_id = "2051011"
api_key = "4HOUS9JD1YDNCE9T"

# URL for the ThingSpeak channel
base_url = "https://api.thingspeak.com/update?api_key={}".format(api_key)

# String data to send
my_string = "Hello ThingSpeak!"

# Integer data to send
my_integer = 42

# Send data to ThingSpeak
response = requests.get("{}&field1={}&field2={}".format(base_url, my_string, my_integer))

# Wait for 15 seconds before sending the next data
time.sleep(15)
