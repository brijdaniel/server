import paho.mqtt.client as mqtt
from app import configure
import os
from app import redis

global config
config = configure.Configure()

def on_connect(client, userdata, flags, rc):
	print("Connected with result code "+str(rc))

	subscriptions = config.read('MQTT', 'subscriptions')
	subscriptions = subscriptions.split(',')

	for topic in subscriptions:
		client.subscribe(topic)
		print("Subscribed to "+ topic)

def on_message(client, userdata, msg):		    
	topic = msg.topic
	payload_decode = str(msg.payload.decode("utf-8"))
	print(topic+": "+payload_decode)
	
	# Ignore status request from server to sprinkler controller
	if not payload_decode == "request":
		redis.db.set(topic, payload_decode)

	# Handle status request from window controller
	if topic == "pihouse/windows/status" and payload_decode == "request":
		client.publish('pihouse/windows/status', redis.db.get(topic))

# Main loop
def run():
	# Create and connect MQTT object
	client.on_message = on_message
	client.on_connect = on_connect
	client.connect(config.read('MQTT', 'server'), 1883, 60)
	client.loop_start()	

client = mqtt.Client(client_id=config.read('MQTT', 'client_id'))