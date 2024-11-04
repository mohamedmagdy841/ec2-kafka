from kafka import KafkaProducer
import requests
import json
import time
import random

access_key = "YOUR_API_KEY"
limit = 1
url = "https://api.aviationstack.com/v1/flights"

producer = KafkaProducer(
    bootstrap_servers='YOUR_PUBLIC_IP:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')  
)

def fetch_and_send_data():
    random_offset = random.randint(0, 100)
    
    params = {
        "access_key": access_key,
        "limit": limit,
        "offset": random_offset,
    }
    
    response = requests.get(url, params=params)
    if response.status_code == 200:
        
        response_json = response.json()
        
        
        if 'data' in response_json:
            data = response_json['data']
            
            
            for item in data:
                producer.send('aviation_flights', item)
            print("Sending to Consumer")
    
            producer.flush()
        else:
            print("No data found in the response.")
    else:
        print(f"Failed to retrieve data: {response.status_code}")

while True:
    fetch_and_send_data()
    time.sleep(10)
