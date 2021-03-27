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
docxpath = 'D:\sia\documents\Project\Project-Final-Report.docx'


def word_count():
	d = docx.Document(docxpath)
	ps = d.paragraphs
	count = sum(map(lambda p:len(p.text.split()), ps))
	return count


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


	def tweet(self, l):
		"""
		Super super driver a super driver!
		"""
		try:
			self.twitter_api.UpdateProfile(name=f'課題文字数{l}/15000')
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

	tc.tweet(word_count())
	