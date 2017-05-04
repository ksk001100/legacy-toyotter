from oauth import *

class FavoriteListener(StreamListener):

    def on_status(self, status):
        f = open(os.path.abspath(os.path.dirname(__file__)) + '/../data/id.txt', 'r')
        userList = f.readlines()
        for i in range(len(userList)):
            userList[i] = userList[i].replace('\n', '')
            
        if(status.author.screen_name in userList):
            API(getOauth()).create_favorite(status.id)
        return True

    def on_error(self, status_code):
        print('Got an error with status code: ' + str(status_code))
        return True

    def on_timeout(self):
        print('Timeout...')
        return True

def main():
    listener = FavoriteListener()
    stream = Stream(getOauth(), listener)
    stream.userstream()

if __name__ == '__main__':
    main()
