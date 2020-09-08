import GetOldTweets3 as got
import pandas as pd
import time
from datetime import datetime, date, time, timedelta
from pytz import timezone
import os
tweetCriteria = got.manager.TweetCriteria().setQuerySearch(os.environ["TAG"])\
                                           .setSince(os.environ["FROM"],)\
                                           .setUntil(os.environ["UNTIL"])\
                                           .setMaxTweets(int(os.environ["NUM"]))

tweets = got.manager.TweetManager.getTweets(tweetCriteria)
tweet_lst = []
users = []

for tweet in tweets:
  tweet_params = []
  jst_tweet_date = tweet.date + timedelta(hours=9)
  tweet_params.extend([jst_tweet_date, tweet.username, tweet.text])
  tweet_lst.append(tweet_params)
  users.append(tweet.username)

Column =['日付', 'アカウント名', 'ツイート']
df = pd.DataFrame(tweet_lst, columns=Column)


filename = "/root/opt/" + (os.environ["TAG"]) + "_from_" + (os.environ["FROM"]) + "_to_" + (os.environ["UNTIL"]) + "_" +(os.environ["NUM"]) + "件" + ".csv"

# csvの出力
df.to_csv(filename, encoding='utf_8_sig') # CSV形式で保存
