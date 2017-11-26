from oauth import *
from datetime import timedelta
import re
import coloring_string as cs


class Listener(StreamListener):

    def on_status(self, status):
        status.created_at += timedelta(hours=9)
        Tweet = status.text
        m = re.search('(?<=@)\w+', Tweet)
        if(m != None):
            Tweet = Tweet.replace(
                '@' + m.group(0), "\033[35m" + "@" + m.group(0) + "\033[0m")
        Tweet = Tweet.replace("\n", " ")
        print("[" + cs.green("via " + status.source) + "] [" + cs.yellow(str(status.created_at)) + "] @" +
              cs.cyan(status.author.screen_name) + " " + Tweet + " " + cs.red(str(status.id) + "\n"))
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
