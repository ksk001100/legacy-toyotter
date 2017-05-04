from tweepy import *
import webbrowser
import os
import signal

signal.signal(signal.SIGPIPE, signal.SIG_DFL)
signal.signal(signal.SIGINT, signal.SIG_DFL)

def getOauth():
    consumer_key = 'lsyVfSuFs5N6KaZqzxDfBFyyh'
    consumer_secret = 'JGmCtwmi9nSxwFossoaRtGnkZYka13PYWGlJsyNtH1H1wmM6FA'
    auth = OAuthHandler(consumer_key, consumer_secret)
    if os.path.isfile(os.path.abspath(os.path.dirname(__file__)) + "/../data/access_token.txt"):
        with open(os.path.abspath(os.path.dirname(__file__)) + '/../data/access_token.txt','r') as f:
            token = f.read()
        token = token.split('\n')
        access_token = token[0]
        access_token_secret = token[1]
        auth.set_access_token(access_token, access_token_secret)
        return auth
    else:
        f = open(os.path.abspath(os.path.dirname(__file__)) + '/../data/access_token.txt','w+')
        url = auth.get_authorization_url()
        webbrowser.open(url)
        pin = input('Enter PIN code : ')
        auth.get_access_token(pin)
        auth.set_access_token(auth.access_token, auth.access_token_secret)
        f.write(auth.access_token + '\n' + auth.access_token_secret)
        f.close()
        return auth
