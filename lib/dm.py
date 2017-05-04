from oauth import *
import sys

def directMessage(name,text):
    api = API(getOauth())
    api.send_direct_message(screen_name=name, text=text)

def main():
    param = sys.argv
    directMessage(param[2],param[1])

if __name__ == '__main__':
    main()
