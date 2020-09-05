import GetOldTweets3 as got
import pandas as pd
from datetime import datetime
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
  # tweet.date = tweet.date.strftime('%Y年%m月%d日')
  tweet_params.extend([tweet.date, tweet.username, tweet.text])
  tweet_lst.append(tweet_params)
  users.append(tweet.username)

# print(users)
users = list(set(users))

Column =['日付', 'アカウント名', 'ツイート']
df = pd.DataFrame(tweet_lst, columns=Column)

# # # # # csvの出力
df.to_csv('/root/opt/tweet_test.csv',encoding='utf_8_sig') # CSV形式で保存

df_users = pd.DataFrame(users)

# # # # # # csvの出力
df_users.to_csv('/root/opt/tweet_users.csv', encoding='utf_8_sig') # CSV形式で保存