from oauth import *
import sys

def createFavorite(id):
    API(getOauth()).create_favorite(id)

def main():
    param = sys.argv
    createFavorite(param[1])

if __name__ == '__main__':
    main()
