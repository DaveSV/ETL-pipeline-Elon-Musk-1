import snscrape.modules.twitter as sntwitter
import pandas as pd

query = "from:elonmusk since:2021-01-01 until:2022-01-01"

tweets = []
for i, tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
    tweets.append([tweet.date, tweet.rawContent])

df = pd.DataFrame(tweets, columns=['date', 'tweet'])
df.to_csv('tweets.csv', index=False)
