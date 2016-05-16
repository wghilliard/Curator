__author__ = 'William Hilliard'

from mongoengine import connect
from pymongo import read_preferences
from celery import Celery
import config

app = Celery('curator')
app.config_from_object(config)


read_preference = read_preferences.ReadPreference.PRIMARY
db = connect(db=config.MONGODB_DB, host=config.MONGODB_HOST, port=config.MONGODB_PORT, read_preference=read_preference)


path = config.PATH

