import tweepy
from tweepy import OAuthHandler 
import os





 

def twitt(texto):
    #Credential access configuration (we obtain the credentials creating a new app on https://developer.twitter.com -Twitter API-)
    CONSUMER_KEY = os.environ.get('CONSUMER_KEY')
    CONSUMER_SECRET = os.environ.get('CONSUMER_SECRET')
    ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN')
    ACCESS_TOKEN_SECRET = os.environ.get('ACCESS_TOKEN_SECRET')
    
    #Autentification
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)
  
    #Ready to connect with the API
    api = tweepy.API(auth)
 
    #we finally twitt! updating the status.
    api.update_status(texto)

    return 1    
