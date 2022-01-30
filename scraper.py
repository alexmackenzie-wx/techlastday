# Import dotenv -- use dotenv to load in environment variables.

import dotenv
import sys
import os

dotenv.load_dotenv()

CONSUMER_KEY = os.getenv("CONSUMER_KEY")
CONSUMER_SECRET = os.getenv("CONSUMER_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")

# Import Tweepy -- an easy-to-use Python library for accessing the Twitter API.

import tweepy

# Authenticate with keys & secrets -- ensure your keys/secrets are kept secret & secure. 

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth) # Twitter api object now ready to use. 

from pyairtable import Table

airtable_key = os.getenv("AIRTABLE_KEY")
airtable_base = os.getenv("AIRTABLE_BASE")
airtable_table_name = os.getenv("TABLE_NAME")

table = Table(airtable_key, airtable_base, airtable_table_name)