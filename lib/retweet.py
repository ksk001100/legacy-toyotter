from oauth import *
import sys

def retweet(id):
    API(getOauth()).retweet(id)

def main():
    param = sys.argv
    retweet(param[1])

if __name__ == '__main__':
    main()
