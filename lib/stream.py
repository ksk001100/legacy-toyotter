from oauth import *
from datetime import timedelta
import re


class Listener(StreamListener):

    def on_status(self, status):
        status.created_at += timedelta(hours=9)
        Tweet = status.text
        m = re.search('(?<=@)\w+', Tweet)
        if(m != None):
            Tweet = Tweet.replace(
                '@' + m.group(0), "\033[35m" + "@" + m.group(0) + "\033[0m")
        Tweet = Tweet.replace("\n", " ")
        print("[\033[32mvia {src}\033[0m] [\033[33m{created}\033[0m] \033[36m@{screen}\033[0m {text} \033[31m{id}\033[0m\n".format(
            name=status.author.name, screen=status.author.screen_name,
            created=status.created_at, text=Tweet, src=status.source, id=status.id)), "\r",
        return True

    def on_error(self, status_code):
        print('Got an error with status code: ' + str(status_code))
        return True

    def on_timeout(self):
        print('Timeout...')
        return True


def main():
    listener = Listener()
    stream = Stream(getOauth(), listener)
    stream.userstream()


if __name__ == "__main__":
    main()
