import requests
import json
from datetime import datetime

headers = {
    'User-Agent': 'My Weather app',
    'From': 'kim.rosvoll@gmail.com'
}

url = "https://graph.microsoft.com/v1.0/me/messages?filter=emailAddress eq 'kim.rosvoll@nordomatic.com'"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

print(data)