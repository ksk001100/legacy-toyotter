from oauth import *
import json
import re
from requests_oauthlib import OAuth1Session
import coloring_string as cs


def getTimeLine():
    print('')
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
                Tweet = Tweet.replace('@' + m.group(0), cs.magenta("@" + m.group(0)))
            Tweet=Tweet.replace("\n", " ")
            print('[' + cs.yellow(time[3]) + ']', end = '')
            if(count % 2 == 0):
                print(cs.cyan('@' + tweet['user']['screen_name']), end = '')
            else:
                print(cs.green('@' + tweet['user']['screen_name']), end = '')
            print(' ' + Tweet + cs.red(str(tweet['id'])) + ' ')
    else:
        print("Error: %d" % req.status_code)
    print('')


def main():
    getTimeLine()


if __name__ == '__main__':
    main()
