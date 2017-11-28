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
        print("[via {src}] [{created}] @{screen} {text} {id}\n".format(
            screen=cs.cyan(status.author.screen_name), created=cs.yellow(str(status.created_at)),
            text=Tweet, src=cs.green(status.source), id=cs.red(str(status.id)))
            ), "\r",
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
