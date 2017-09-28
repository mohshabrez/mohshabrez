# importing the module
import tweepy
import os
img="fswebcam  -F 3 -r 800x600 img.jpg"
os.system(img)



 
# personal details
consumer_key ="mJYZ7cTREFYKW1IVS1Vo8o3rG"
consumer_secret ="FVLRm9UP8fHhCoEgJE2zjojeI3GcUUaDq03BOfN4IQjcWxYSI1"
access_token ="819840518624542722-elxp1ewAP96ihQ3gp84XBYfAlBY27UI"
access_token_secret ="a2iSB7HiZDnzjXHuE003nuYRMT89U2B5jQFGPyiW5AqnD"

 
# authentication of consumer key and secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
 
# authentication of access token and secret
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
 
tweet ="my frnd is rich man" # toDo
image_path ="img.jpg" # toDo
 
# to attach the media file
status = api.update_with_media(image_path, tweet) 
api.update_status(status = tweet)
