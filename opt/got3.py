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

def utc_to_jst(timestamp_utc):
    datetime_utc = datetime.datetime.strptime(timestamp_utc + "+0000", "%Y-%m-%d %H:%M:%S.%f%z")
    datetime_jst = datetime_utc.astimezone(datetime.timezone(datetime.timedelta(hours=+9)))
    timestamp_jst = datetime.datetime.strftime(datetime_jst, '%Y-%m-%d %H:%M:%S.%f')
    return timestamp_jst

for tweet in tweets:
  tweet_params = []
  #　調整中
  tweet_params.extend([utc_to_jst(tweet.date), tweet.username, tweet.text])
  tweet_lst.append(tweet_params)
  users.append(tweet.username)

# print(users)
users = list(set(users))

Column =['日付', 'アカウント名', 'ツイート']
df = pd.DataFrame(tweet_lst, columns=Column)


# 調整中
# filename = "/root/opt/" + {os.environ["TAG"]} + "from" + {(os.environ["FROM"],)} + "to"+ {os.environ["UNTIL"]} + {int(os.environ["NUM"]} + "_" + ".csv"

# # # # # csvの出力
df.to_csv(filename, encoding='utf_8_sig') # CSV形式で保存

df_users = pd.DataFrame(users)

# # # # # # csvの出力
df_users.to_csv('/root/opt/tweet_users.csv', encoding='utf_8_sig') # CSV形式で保存
