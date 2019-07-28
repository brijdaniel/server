from time import sleep
from app import redis, socketio, convert
from flask_socketio import emit
from threading import Thread

"""
Function to monitor status changes
These changes trigger js messages to client to update client content
Generic function used to drive sprinkler, windows etc

**Dont actually need this for windows because the status change is published straight away from ESP**

TODO: want to change this to ISR, then it wont need a loop in a new thread
"""

def monitor(channel, status='True'):
	channel = str('pihouse/'+str(channel)+'/status') # dont think I need all these str declarations
	while status == 'True':
		sleep(0.2)
		status = redis.db.get(channel)
	socketio.emit('statechange', {"status": convert.switch(status), "opposite": convert.convert(status)})
	# need to make sure this will only emit to the right URL

def run():
	thread = Thread(target=monitor)
	thread.start()