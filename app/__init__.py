from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Connect to redis server
from app import redis

# MQTT initialise
from app import routes, mqtt
from threading import Thread

thread = Thread(target=mqtt.run)
thread.start()

# Set logging level
import logging
from logging.handlers import RotatingFileHandler
import os

if not os.path.exists('logs'):
    os.mkdir('logs')
file_handler = RotatingFileHandler('logs/server.log', maxBytes=10240, backupCount=10)
file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
file_handler.setLevel(logging.DEBUG)
app.logger.addHandler(file_handler)

app.logger.setLevel(logging.DEBUG)
app.logger.info('Server startup')