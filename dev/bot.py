# TWITTER API BOT CLASS

from twitter import Twitter, OAuth
from login import Login

class Bot:
	'''
	| METHODS:
	| - ability to initialize the API for secure use (posting only for now)
	| - ability to send a tweet with user-processed data
	|
	| ATTRIBUTES:
	| - authorized token using (secret) login codes
	| - the actual bot object (following authorization)
	'''
	def __init__(self) -> None:
		'''
		self.auth = OAuth(token = Login.ACCESS_TOKEN, 
						  token_secret = Login.ACCESS_TOKEN_SECRET, 
						  consumer_key = Login.API_KEY, 
						  consumer_secret = Login.API_KEY_SECRET
		)
		self.bot = Twitter(auth = self.auth)
		'''
		print("Bot Initiated!")

	def send_tweet(self, data: list) -> None:
		text = '\n'.join(data)
		print("{}".format(text))
		# self.bot.statuses.update(status = text)
		print("Tweet sent successfully!")


if __name__ == "__main__":
	pass