# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 11:27:38 2020

@author: jmmungai
"""

import json
import requests
from requests_oauthlib import OAuth1

def get_tweets(*args,count=10):
    url = "https://api.twitter.com/1.1/search/tweets.json"
    tweets = []
    
    for search_terms in args:
        params = {"q":search_terms,"lang":"en","count":count,"tweet_mode":"extended"}
        
        response = requests.get(url,auth=auth,params=params)    
        tweets += response.json()["statuses"]
    
    return tweets
    
with open("../../Desktop/Documentations/DATASCIENCE/WORLDQUANT/Twitter/code/twitter secrets dbf.json", "r") as f:
    secrets = json.load(f)
    
auth = OAuth1(secrets[0]["CONSUMER_KEY"],
             secrets[0]["CONSUMER_SECRET"],
             secrets[0]["ACCESS_TOKEN"],
             secrets[0]["ACCESS_TOKEN_SECRET"])

tweets = get_tweets("mufc")
print(tweets[0])
print(tweets[0]['full_text'])

for tweet in tweets:
    print(tweet['full_text'])
    r = requests.get("http://127.0.0.1:5000/predict",params={"tweet":tweet['full_text']})
    print(r.text)
        