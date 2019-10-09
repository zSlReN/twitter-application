import asyncio
import datetime
import json
import math
import os
import random

import twitter
from dotenv import load_dotenv

from logger import Logger


target_date = datetime.datetime(2019, 10, 11, 15)


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


	async def start(self):
		"""
		Super super driver a super driver!
		"""
		self.logger.info('Starting twitter-manager.')
		while 1:
			try:
				now = datetime.datetime.now()
				if now > target_date:
					self.twitter_api.UpdateProfile(name='［ZEAL］あてしあ！')
					exit(0)

				delta = target_date - now
				self.twitter_api.UpdateProfile(name=f'あてしあ！上場まで{delta.days}日{delta.seconds // (60 * 60)}時間{delta.seconds // 60 % 60}分{delta.seconds % 60}秒')
				self.logger.info('Profile updated.')
				self.date_on_twitter = now
			except Exception as e:
				self.logger.critical(e)
				
			await asyncio.sleep(math.pi * 4)


if __name__ == '__main__':
	key, secret_key, token, secret_token = twitter_setup()
	
	tc = Twittermanager(
		key,
		secret_key,
		token,
		secret_token
	)

	loop = asyncio.get_event_loop()

	try:
		loop.run_until_complete(
			asyncio.wait([
				tc.start()
			])
		)
	except KeyboardInterrupt:
		pass
	finally:
		loop.close()
