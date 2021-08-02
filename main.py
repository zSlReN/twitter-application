import asyncio
import datetime
import json
import math
import os
import random
import docx

import twitter
from dotenv import load_dotenv
from logger import Logger

tz = datetime.timezone(datetime.timedelta(hours=9))

target = datetime.datetime(year=2021, month=10, day=1, hour=0)

def twitter_setup():
	# path to environment variables
	env_path = '.env'
	load_dotenv(dotenv_path=env_path)

	# get data from .env
	key = os.getenv('KEY')
	key_secret = os.getenv('KEY_SECRET')	
	token = os.getenv('TOKEN')
	token_secret = os.getenv('TOKEN_SECRET')	

	return key, key_secret, token, token_secret


class Twittermanager:
	def __init__(self, key, secret_key, token, token_secret, logger=None):
		self.twitter_api = twitter.Api(
			consumer_key = key,
			consumer_secret = secret_key,
			access_token_key = token,
			access_token_secret = token_secret
		)
		self.logger = Logger('Twittermanger') if logger is None else logger


	def tweet(self):
		"""
		Super super driver a super driver!
		"""
		try:
			t = target - datetime.datetime.now()
			self.twitter_api.UpdateProfile(name=f'しあまで{t.days}日！')
			self.logger.info('Profile updated.')
		except Exception as e:
			self.logger.critical(e)
			

if __name__ == '__main__':
	key, secret_key, token, secret_token = twitter_setup()
	
	tc = Twittermanager(
		key,
		secret_key,
		token,
		secret_token
	)
	print((target-datetime.datetime.now()).days)