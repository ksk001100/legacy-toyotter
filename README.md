# toyotter

CUI twitter client on Python3.  

## Install


1. `pip3 install tweepy pillow `

2. `cd ~/`   
   `git clone https://github.com/KeisukeToyota/toyotter.git`

3. `export PATH="$PATH:$HOME/toyotter/bin"`


## Usage
### Help  
`toyotter -help`  

### Tweet  
Text tweet  
`toyotter -tw [tweet_text]` or `toyotter [tweet_text]`  

Text and image file tweet  
`toyotter -tw [tweet_text] [image_file_path]` or `toyotter [tweet_text] [image_file_path]`

### Get the 20 home timeline  
`toyotter -tl`

### Favorite  
`toyotter -fav [tweet_id]`

### Reply  
`toyotter -rep [tweet_text] [tweet_id]`

### Retweet  
`toyotter -rt [tweet_id]`

### Streaming timeline (exit with Ctrl+C)  
`toyotter -stream`

### Automatic favorite (exit with Ctrl+C)
Add one line at a Twitter ID to `toyotter/data/id.txt`  
`toyotter -autoFav`

### Reading streaming timeline (exit with Ctrl+C)  
`toyotter -say`
