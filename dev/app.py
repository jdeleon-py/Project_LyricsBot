# TKINTER GUI CLASS

from tkinter import Tk, Frame
from tkinter import Button, Label, Entry
from tkinter import N, E, S, W, NE, NW, SE, SW

from lyric import Lyric
from scraper import Scraper
from bot import Bot

class App(Lyric):
	'''
	| METHODS:
	| - ability to add a line of lyrics before the current sample
	| - ability to remove a line of lyrics before the current sample
	| - ability to add a line of lyrics after the current sample
	| - ability to remove a line of lyrics after the current sample
	| - ability to choose a random song and then scrape the web for a sample of the artist's song
	| - ability to use the Twitter API to post the current sample on Twitter
	|
	| ATTRIBUTES:
	| - inherited Lyric data object
	| - Tkinter Interface with the following properties:
	| 		- a label displaying the chosen album name
	| 		- a label displaying the chosen song name
	| 		- a label displaying the chosen sample array
	| 		- a button to add a line of lyrics to the beginning of the chosen sample
	| 		- a button to remove a line of lyrics from the beginning of the chosen sample
	| 		- a button to add a line of lyrics to the end of the chosen sample
	| 		- a button to remove a line of lyrics from the end of the chosen sample
	|		- a button to initialize the scraping process to produce a sample of lyrics
	|		- a button to initialize the Twitter API to post the present sample 
	'''
	def __init__(self, master: object) -> None:
		Lyric.__init__(self)

		self.master = master
		self.frame = Frame(self.master)
		self.frame.pack()
		self.frame.columnconfigure(index = 1, weight = 3)

		# Add Line Before Button
		self.add_before_button = Button(master = self.frame, 
										text = "Add a line before", 
										command = self.add_before
		)
		self.add_before_button.grid(row = 0, column = 0, sticky = W)

		# Add Line After Button
		self.add_after_button = Button(master = self.frame, 
									   text = "Add a line after", 
									   command = self.add_after
		)
		self.add_after_button.grid(row = 1, column = 0, sticky = W)

		# Remove Line Before Button
		self.rem_before_button = Button(master = self.frame, 
										text = "Remove a line before", 
										command = self.rem_before
		)
		self.rem_before_button.grid(row = 2, column = 0, sticky = W)

		# Remove Line After Button
		self.rem_after_button = Button(master = self.frame,
									   text = "Remove a line after",
									   command = self.rem_after
		)
		self.rem_after_button.grid(row = 3, column = 0, sticky = W)

		# Get Lyrics Button
		self.choose_button = Button(master = self.frame, 
									text = "Get a Song's Lyrics", 
									command = self.choose
		)
		self.choose_button.grid(row = 4, column = 0, sticky = W)

		# Tweet Button
		self.tweet_button = Button(master = self.frame, 
								   text = "Tweet", 
								   command = self.tweet
		)
		self.tweet_button.grid(row = 5, column = 0, sticky = W)

		# Album Label
		self.album_label = Label(master = self.frame, text = "Album: ")
		self.album_label.grid(row = 0, column = 1)

		# Song Label
		self.song_label = Label(master = self.frame, text = "Song: ")
		self.song_label.grid(row = 1, column = 1)

		# Lyrics Label
		self.lyrics_label = Label(master = self.frame,
								  text = "Lyrics: ",
								  wraplength = 100
		)
		self.lyrics_label.grid(row = 2, rowspan = 4, column = 1)

	def add_before(self) -> None:
		'''
		- adds the line of lyrics prior to the sample to the sample's beginning
		- updates in real time
		'''
		self.sample_index_min -= 1
		self.sample_index_min = max(self.sample_index_min, 0)
		self.sample = self.sample_lyrics()
		self.lyrics_label.configure(text = "Lyrics: {}".format(self.sample))

	def add_after(self) -> None:
		'''
		- adds the line of lyrics preceding the sample to the sample's end
		- updates in real time
		'''
		self.sample_index_max += 1
		self.sample_index_max = min(self.sample_index_max, len(self.lyrics) - 1)
		self.sample = self.sample_lyrics()
		self.lyrics_label.configure(text = "Lyrics: {}".format(self.sample))

	def rem_before(self) -> None:
		'''
		- removes the line of lyrics prior to the sample from the sample's beginning
		- updates in real time
		'''
		self.sample_index_min += 1
		self.sample_index_min = max(self.sample_index_min, 0)
		self.sample = self.sample_lyrics()
		self.lyrics_label.configure(text = "Lyrics: {}".format(self.sample))

	def rem_after(self) -> None:
		'''
		- removes the line of lyrics preceding the sample to the sample's end
		- updates in real time
		'''
		self.sample_index_max -= 1
		self.sample_index_max = min(self.sample_index_max, len(self.lyrics) - 1)
		self.sample = self.sample_lyrics()
		self.lyrics_label.configure(text = "Lyrics: {}".format(self.sample))

	def tweet(self) -> None:
		'''
		- initializes the Twitter API bot object and tweets what 
		  the current sample is displaying
		- once the bot has been used, the sample is included in with an 
		  accumlating file representing the lyrics used to date
		'''
		bot = Bot()
		bot.send_tweet(data = self.sample)
		self.add_unique_lyrics()

	def choose(self) -> None:
		'''
		- chooses the song randomly, then chooses lyrics randomly from the
		  selected song
		'''
		self.album, self.song = self.get_song()
		self.album_label.configure(text = "Album: {}".format(self.album))
		self.song_label.configure(text = "Song: {}".format(self.song))
		self.get_lyrics()

	def get_lyrics(self) -> None:
		'''
		- uses the Selenium library to scrape and process the lyrics sample data
		'''
		scraper = Scraper()
		self.lyrics = scraper.process_lyrics(song_name = self.song)
		self.sample_index_min, self.sample_index_max = self.random_index()
		self.sample = self.sample_lyrics()
		self.lyrics_label.configure(text = "Lyrics: {}".format(self.sample))
		scraper.quit_scraper()


if __name__ == "__main__":
	root = Tk()
	root.geometry("500x500")
	root.wm_title('Twitter Lyrics Bot')
	app = App(master = root)

	root.mainloop()
