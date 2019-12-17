import tweepy
from tweepy import OAuthHandler 
import os




 

def twitt(texto):
    # Configuracion de acceso con las credenciales
    auth = tweepy.OAuthHandler(os.environ.get('CONSUMER_KEY'), os.environ.get('ACCESS_TOKEN'))
    auth.set_access_token(os.environ.get('ACCESS_TOKEN'), os.environ.get('ACCESS_TOKEN_SECRET') )
  
    # Listos para hacer la conexion con el API
    api = tweepy.API(auth)
 
    # agregar un comentario a un tweet
    api.update_status(texto)

    return 1    
