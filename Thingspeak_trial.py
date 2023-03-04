import requests
import time

# Channel ID and API Key
channel_id = "2051011"
write_api_key = "4HOUS9JD1YDNCE9T"

# URL for the ThingSpeak channel
base_url = f"https://api.thingspeak.com/channels/{channel_id}/feeds.json"

# Data to send
data = {'api_key': write_api_key, 'field1': '10'}

# Send data to ThingSpeak
response = requests.post(base_url, json=data)

# Wait for 15 seconds before sending the next data
time.sleep(15)
