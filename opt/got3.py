import GetOldTweets3 as got
import pandas as pd
from datetime import datetime

tweetCriteria = got.manager.TweetCriteria().setQuerySearch('#TEST')\
                                           .setSince("2020-08-28")\
                                           .setUntil("2020-09-1")\
                                           .setMaxTweets(50)

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
df.to_csv('/root/opt/tweet_test.csv',) # CSV形式で保存

# df_users = pd.DataFrame(users)

# # # # # # csvの出力
# df_users.to_csv('/root/opt/tweet_users.csv',) # CSV形式で保存