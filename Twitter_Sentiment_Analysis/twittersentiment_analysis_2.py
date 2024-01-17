import json
import requests
import re
from requests_oauthlib import OAuth1
from textblob import TextBlob         #for checking the sentiment of each tweet
from collections import Counter       #for counting each sentiment in format of a dictionary.


api_key = 'qp6AIqtOWVJrAi1EmvCviwAlz'					# enter api key
api_secret_key = 'oPVDMFbY5dcIMHA7pKuwuJnWeVfOfBwr7phS1riab1NtVdTPSC'   #enter api secret key
auth = OAuth1(api_key, api_secret_key)

screen_name = 'realDonaldTrump' 					#search keyword  
url="https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name="+screen_name+"&count=200"

response = requests.get(url, auth=auth)
jtweet = json.loads(response.text)
# print(jtweet)

twi_li = []

for x in range(1, 10):
	#print(x)
	a = jtweet[x]['text']

	# to clean tweet text by removing links, special characters using simple regex statements.
	clean_var = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) |(\w+:\/\/\S+)", " ", a).split())

	# create TextBlob object of passed tweet text
	a1 = TextBlob(clean_var)

	# to classify sentiment of passed tweet using textblob's sentiment method 
	if (a1.sentiment.polarity > 0):
		twi_li.append("positive")
	elif (a1.sentiment.polarity < 0):
		twi_li.append("negative")
	else:
		twi_li.append("neutral")


twi_li_count = Counter(twi_li)
# print(twi_li_count)

b = []

for x in twi_li_count: 
	b.append(twi_li_count[x])
# print(b)

key_max = max(b)
# print(key_max)

max_words = [key for key, value in twi_li_count.items() if value == key_max]
print("The overall sentiment analysis: "+ str(*max_words)) # "*" is used to remove brackets
