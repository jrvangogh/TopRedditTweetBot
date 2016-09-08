# TopRedditTweetBot -- v. 1.0 (development indefinitely paused)
## A bot that monitors a single subreddit and tweets posts which surpass a score threshold
##### Author: Jacob van Gogh (jrvangogh@gmail.com)
&nbsp;

Notes:
* The subreddit and threshold are set via constants within the main script. 
* A python file, named "apiInfo.py" needs to be present that contains Twitter API key info as variables:
  * TWITTER_CONSUMER_KEY
  * TWITTER_CONSUMER_SECRET
  * TWITTER_ACCESS_TOKEN
  * TWITTER_ACCESS_TOKEN_SECRET
* Posts are obtained by repeatedly scanning a subreddit's top monthly posts
  * Depending on the score threshold, a different time frame should be used. High thresholds might need to look at larger time frames, while smaller ones will see better performance looking at smaller time frames.
* Posts are only tweeted out if they surpass the score threshold after the bot is started

### Action Items/Changelog
##### Current Version: 1.0

##### Action Items:
* Continue debugging
* Evaluate better methods for tracking posts
