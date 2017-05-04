def main():
    print("""
            \033[32m-tw\033[0m : \033[36mTweet\033[0m -> \033[33mtoyotter -tw\033[0m \033[31m[tweet_text]\033[0m \033[33m(or toyotter\033[0m \033[31m[tweet_text]\033[0m\033[33m)\033[0m
            \033[32m-tl\033[0m : \033[36mGet the 20 home timeline\033[0m -> \033[33mtoyotter -tl\033[0m
            \033[32m-fav\033[0m : \033[36mFavorite\033[0m -> \033[33mtoyotter -fav\033[0m \033[31m[tweet_id]\033[0m
            \033[32m-rep\033[0m : \033[36mReply\033[0m -> \033[33mtoyotter -rep\033[0m \033[31m[tweet_text]\033[0m \033[31m[tweet_id]\033[0m
            \033[32m-rt\033[0m : \033[36mRetweet\033[0m -> \033[33mtoyotter -rt\033[0m \033[31m[tweet_id]\033[0m
            \033[32m-dm\033[0m : \033[36mSend diriect message\033[0m -> \033[33mtoyotter -dm\033[0m \033[31m[screen_name]\033[0m \033[31m[text]\033[0m
            \033[32m-stream\033[0m : \033[36mStreaming timeline (exit with Ctrl+C)\033[0m -> \033[33mtoyotter -stream\033[0m
            \033[32m-autoFav\033[0m : \033[36mAuto favorite (exit with Ctrl+C)\033[0m -> \033[33mtoyotter -autoFav\033[0m
            \033[32m-say\033[0m : \033[36mReading streaming timeline (exit with Ctrl+C)\033[0m -> \033[33mtoyotter -say\033[0m
            """)

if __name__ == '__main__':
    main()
