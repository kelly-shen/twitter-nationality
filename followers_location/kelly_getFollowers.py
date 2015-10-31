import time
import io
import tweepy

CONSUMER_KEY = 'lyI0jZEbPLJK1mPLYsgIrlsTG'
CONSUMER_SECRET = 'IfyrTRwIqSgV95Zl14UQsBa9ChPeohW9eSI7sWABxX23cki8Ee'
OAUTH_TOKEN = '2977560412-Rmf2FiRzkSDUNvwAUs5Qx6EDEj0kxcDquzhcgOL'
OAUTH_SECRET = 'SlWuglWaX2d2LD4nSnHUXr50bb2CS1Juck8UcThhwPOTK'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_SECRET)

api = tweepy.API(auth)

# Open/Create a file to append data
csvFile = open('tweets.csv', 'a')
#Use csv Writer
csvWriter = csv.writer(csvFile)


for tweet in tweepy.Cursor(api.search,
                           q="NASA",
                           since="2014-01-01",
                           until="2014-02-01",
                           lang="en").items():
    print tweet.created_at, tweet.text
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])