import asyncio
import datetime
import json
import math
import os
import random

import twitter
from dotenv import load_dotenv

from logger import Logger


target_date = datetime.datetime(2019, 10, 4, 15)


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
					exit('Target datetime archieved.')				

				timedelta = target_date - now
				temp = timedelta.strftime('%H{0}%M{1}%S{2}%f{3}').format('時間', '分', '秒', 'マイクロ秒')
				self.twitter_api.UpdateProfile(name=f'あてしあ！上場まで{temp}')
				self.logger.info('Profile updated.')
				self.date_on_twitter = now
				await asyncio.sleep(math.pi)
			except Exception as e:
				self.logger.critical(e)


if __name__ == '__main__':
	key = os.getenv('KEY')
	secret_key = os.getenv('KEY_SECRET')
	token = os.getenv('TOKEN')
	secret_token = os.getenv('TOKEN_SECRET')

	tc = Twittermanager(
		key,
		secret_key,
		token,
		secret_key
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
