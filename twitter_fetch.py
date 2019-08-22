import tweepy
import json
from datetime import datetime


def twitter_fetch(consumer_key, consumer_secret, access_token, access_token_secret,search_handle, search_size):
	results = []
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	try:
		api = tweepy.API(auth)
		#api.verify_credentials()
		print("Authentication OK")
	except:
	    print("Error during authentication")
	    return None
	public_tweets = api.user_timeline(id=search_handle, count=search_size)
	for tweet in public_tweets:    
	   	time = tweet.created_at
	   	time = time.strftime("%m/%d/%Y, %H:%M:%S")
	   	screen_name = tweet.user.screen_name
	   	tweet_id = tweet.id
	   	source_url = "https://twitter.com/"+screen_name +"/status/"+str(tweet_id)
	   	results.append({"text" : tweet.text.rstrip('\n') ,"created_at" : time, "source_url" : source_url, "id": tweet_id})
	   	#results.append(tweet._json)
	return json.dumps(results)

