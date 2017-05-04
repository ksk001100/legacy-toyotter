from oauth import *
import sys

def reply(text, id):
    name = API(getOauth()).get_status(id).author.screen_name
    text = "@" + name + " " + text
    API(getOauth()).update_status(status=text, in_reply_to_status_id=id)

def main():
    param = sys.argv
    reply(param[1], param[2])

if __name__ == '__main__':
    main()
