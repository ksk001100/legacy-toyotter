from oauth import *
import json
import re
from requests_oauthlib import OAuth1Session


def getTimeLine():
    print ('')
    url = "https://api.twitter.com/1.1/statuses/home_timeline.json"
    count = 0
    params = {}
    oauth = getOauth()
    CK = oauth.consumer_key
    CS = oauth.consumer_secret
    AT = oauth.access_token
    AS = oauth.access_token_secret
    twitter = OAuth1Session(CK, CS, AT, AS)
    req = twitter.get(url, params=params)
    if req.status_code == 200:
        timeline = json.loads(req.text)
        for tweet in timeline:
            count += 1
            creat = tweet['created_at']
            time = creat.split(" ")
            Tweet = tweet["text"]
            m = re.search('(?<=@)\w+', Tweet)
            if(m != None):
                Tweet = Tweet.replace(
                    '@' + m.group(0), "\033[35m" + "@" + m.group(0) + "\033[0m")
            Tweet = Tweet.replace("\n", " ")
            print("[\033[33m" + time[3] + "\033[0m]", end='')
            if(count % 2 == 0):
                print("\033[36m@" + tweet['user']['screen_name'] + " \033[0m", end='')
            else:
                print("\033[32m@" + tweet['user']['screen_name'] + " \033[0m",end='')
            print(Tweet + " \033[31m" + str(tweet['id']) + "\033[0m")
    else:
        print("Error: %d" % req.status_code)
    print ('')


def main():
    getTimeLine()


if __name__ == '__main__':
    main()
