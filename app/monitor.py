from time import sleep
from app import redis, socketio, convert
from flask_socketio import emit
from threading import Thread

def monitor(status='True'):
	while status == 'True':
		sleep(0.2)
		status = redis.db.get('pihouse/sprinkler/status')
	socketio.emit('statechange', {"status": convert.switch(status), "opposite": convert.convert(status)})

def run():
	thread = Thread(target=monitor)
	thread.start()