import tweepy
import random
import time
import datetime
from os import environ

# delta =  datetime.datetime(2020, 3, 1) - datetime.datetime.now()
# print(delta.days + 1)
# Authenticate to Twitter
CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_KEY = environ['ACCESS_KEY']
ACCESS_SECRET = environ['ACCESS_SECRET']
auth = tweepy.OAuthHandler(CONSUMER_KEY,
    CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY,
    ACCESS_SECRET)

api = tweepy.API(auth)


while True:
    INTERVAL = 60*60*random.random()*24
    delta = datetime.datetime(2020, 3, 1) - datetime.datetime.now()
    hours = str(int(delta.seconds/3600))
    minutes = str(int(delta.seconds/60)-(int(hours) * 60 ))
    # print(str(delta.days) + " Days " + hours + " Hours " + minutes + " minutes left till the Georgia Tech summer transfer decision")
    api.update_status(str(delta.days + 1 ) + " Days " + hours + " Hours " + minutes + " minutes left till the Georgia Tech Summer Transfer Decision")
    time.sleep(INTERVAL)

#
# try:
#     api.verify_credentials()
#     print("Authentication OK")
# except:
#     print("Error during authentication")
