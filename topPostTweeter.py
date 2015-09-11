# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 15:33:37 2015

@author: Jacob van Gogh

This bot monitors a subreddit and tweets posts which reach a certain score
threshold. the subreddit and threshold are set via the initial constants.

A python file, named "apiInfo.py" needs to be present that contains Twitter
API key info.

Note: Posts are obtained by repeatedly scanning a subreddit's top monthly 
posts. However, depending on the score threshold, a different time frame should
be used. High thresholds might need to look at larger time frames, while 
smaller ones will see better performance looking at smaller time frames.
"""

import apiInfo
import tweepy
import praw
import time


# Set Constants

SUBREDDIT_NAME = 'ENTER SUBREDDIT NAME HERE'
THRESHOLD = 'ENTER THRESHOLD HERE'
AGENT_NAME = 'ENTER AGENT NAME HERE'
GET_LIMIT = 'ENTER LIMIT HERE'     # Limit on number of submissions to get at once


# Initialize Tweepy

TWITTER_CONSUMER_KEY = apiInfo.TWITTER_CONSUMER_KEY
TWITTER_CONSUMER_SECRET = apiInfo.TWITTER_CONSUMER_SECRET

TWITTER_ACCESS_TOKEN = apiInfo.TWITTER_ACCESS_TOKEN
TWITTER_ACCESS_TOKEN_SECRET = apiInfo.TWITTER_ACCESS_TOKEN_SECRET

auth = tweepy.OAuthHandler(TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET)
auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)

tweep = tweepy.API(auth)


# Initialize Praw

agent = AGENT_NAME
pr = praw.Reddit(user_agent=agent)


# Method definitions   


def tweet_posts(posts, tweeted_set, threshold, tweepy_api, initialize=False):
    """
    This method takes all of the submissions in posts and iterates through
    them. If a post's score is higher than the threshold and is not in the
    tweeted_set, it is tweeted out and added to the set. If initialize is true,
    it is added to the set, but not tweeted out.
    
    If the last post in the list has a score higher than the threshold, returns
    the post's ID. Otherwise, returns '0'
    
    Keyword arguments:
    posts -- list of reddit submissions (sorted by score)
    tweeted_set -- set of posts already tweeted out
    tweepy_api -- tweepy API object
    initialize -- boolean indicating if the tweeted_set is being initialized
    """
    for post in posts:
        if post.score >= threshold and post.id not in tweeted_set:
            tweeted_set.add(post.id)
            if not initialize:
                tweet_text = (post.title + '\n' + post.permalink)
                tweepy_api.update_status(status=tweet_text)
    
    if posts[-1].score >= threshold:
        return posts[-1].name
    else:
        return '0'
    
    

# Start and run bot: during the first check of submissions, posts that breach
# the point threshold are added to the tweeted set, but not actually tweeted
# out. This prevents previous posts from being tweeted out on the bots start up

sub = pr.get_subreddit(SUBREDDIT_NAME)
tweeted = set()

is_initializing = True
while(True):
    after = None
    while(after is not '0'):
        posts = sub.get_top_from_month(limit=GET_LIMIT, params={'after':after})
        time.sleep(3)
        
        after = tweet_posts(posts, tweeted, THRESHOLD, tweep, is_initializing)
    
    time.sleep(120)




