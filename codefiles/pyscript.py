import paho.mqtt.client as mqtt
import json
import time
from random import uniform

# Define MQTT parameters
broker_address = "your_broker_address"
port = 1883
topic = "water_consumption"

# Function to simulate water consumption data
def generate_water_data():
return {"timestamp": int(time.time()), "flow_rate": round(uniform(0.5, 5.0), 2)}

# Callback when the client connects to the broker
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe(topic)

# Callback when a message is published to the topic
def on_publish(client, userdata, mid):
    print("Message Published")

# Main script
client = mqtt.Client()
client.on_connect = on_connect
client.on_publish = on_publish

# Connect to the broker
client.connect(broker_address, port, 60)
try:
    while True:
        water_data = generate_water_data()
        payload = json.dumps(water_data)
       # Publish the data to the topic
        client.publish(topic, payload)
       time.sleep(10)  # Adjust the interval based on your requirements
       except KeyboardInterrupt:
print("Script terminated by user.")
    client.disconnect()

