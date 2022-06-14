# TWITTER API BOT CLASS

from twitter import Twitter, OAuth
from login import Login

class Bot:
	'''
	| METHODS:
	| - ability to send a tweet with randomly selected lyrics
	| - ability to like tweets that are relevant to the automated account
	|
	| ATTRIBUTES:
	| -
	'''
	def __init__(self):
		self.auth = OAuth(token = Login.ACCESS_TOKEN, 
						  token_secret = Login.ACCESS_TOKEN_SECRET, 
						  consumer_key = Login.API_KEY, 
						  consumer_secret = Login.API_KEY_SECRET
		)
		self.bot = Twitter(auth = self.auth)

	def send_tweet(self, data: list) -> None:
		text = '\n'.join(data)
		self.bot.statuses.update(status = text)
		print("Tweet sent successfully!")


if __name__ == "__main__":
	pass