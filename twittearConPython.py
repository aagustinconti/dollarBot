import tweepy
from tweepy import OAuthHandler 
import os





 

def twitt(texto):
    # Configuracion de acceso con las credenciales
    CONSUMER_KEY = os.environ.get('CONSUMER_KEY')
    CONSUMER_SECRET = os.environ.get('CONSUMER_SECRET')
    ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN')
    ACCESS_TOKEN_SECRET = os.environ.get('ACCESS_TOKEN_SECRET')
    
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)
  
    # Listos para hacer la conexion con el API
    api = tweepy.API(auth)
 
    # agregar un comentario a un tweet
    api.update_status(texto)

    return 1    
