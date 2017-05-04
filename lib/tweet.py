from oauth import *
from PIL import Image
import os
import os.path
import sys


def ImageProcessing(imagepath):
    img = Image.open(imagepath, "r")
    resize_img = img.resize((int(img.size[0] * 0.1), int(img.size[1] * 0.1)))
    resize_img.save('output.jpg', "JPEG", quality=100, optimize=True)


def tweet(text, filename):
    if filename == None:
        API(getOauth()).update_status(status=text)
    else:
        if os.path.getsize(filename) > 3000000:
            ImageProcessing(filename)
            filename = "output.jpg"
        API(getOauth()).update_with_media(filename, status=text)
        if filename == "output.jpg":
            os.system("rm output.jpg")


def main():
    param = sys.argv
    text = param[1]
    if('@' in text):
        text = text.replace('@', '\n')
    if('_' in text):
        text = text.replace('_', ' ')
    if len(param) >= 3:
        filename = param[2]
    else:
        filename = None
    tweet(text, filename)


if __name__ == '__main__':
    main()
