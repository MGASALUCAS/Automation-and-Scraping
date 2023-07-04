import sqlite3
import json
from flask import Flask
import tweepy

# Initialize Flask app
app = Flask(__name__)

# Configure database connection
DATABASE = 'tweets.db'

# Create the tweets table if it doesn't exist
conn = sqlite3.connect(DATABASE)
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS tweets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        account_name TEXT,
        message TEXT,
        day_saved DATETIME,
        comments TEXT
    )
''')
conn.commit()
conn.close()

# Configure json file loading
with open('tweet_secrets.json') as config_file:
    config = json.load(config_file)

consumer_key = config['consumer_key']
consumer_secret = config['consumer_secret']
access_token = config['access_token']
access_token_secret = config['access_token_secret']


# Authenticate with Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


# Define route to fetch and save tweets
@app.route('/save_tweets')
def save_tweets():
    account_name = 'MgasaLucas'
    num_tweets = 10  # Number of tweets to retrieve

    # Fetch tweets from Twitter API
    tweets = api.user_timeline(screen_name=account_name, count=num_tweets)

    # Save tweets to the database
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    for tweet in tweets:
        cursor.execute('''
            INSERT INTO tweets (account_name, message, day_saved, comments)
            VALUES (?, ?, ?, ?)
        ''', (account_name, tweet.text, tweet.created_at, ''))  # Retrieve and store comments if available
    conn.commit()
    conn.close()

    return 'Tweets saved successfully!'

if __name__ == '__main__':
    app.run(debug=True)
