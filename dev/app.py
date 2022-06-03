# GUI CLASS

from tkinter import Tk, Frame, Menu
from tkinter import Button, Label, Entry
from tkinter import N, E, S, W, NE, NW, SE, SW
import random
import json
from scraper import Scraper

class App:
	'''
	| METHODS:
	| -
	|
	| ATTRIBUTES:
	| -
	|
	| CHANGES TO BE MADE:
	| - implement add/remove line before/after buttons
	| - fix app layout
	| - implement twitter bot
	| - add as button to change the initial line count
	'''
	LINE_MAX = 3

	def __init__(self, master: object) -> None:
		self.master = master
		self.frame = Frame(self.master)
		self.frame.pack()

		self.lyrics = []
		self.frame.columnconfigure(1, weight = 3)

		# Add Line Before Button
		self.add_before_button = Button(master = self.frame, 
										text = "Add a line before", 
										command = self.add_before)
		self.add_before_button.grid(row = 0, column = 0, sticky = W)

		# Add Line After Button
		self.add_after_button = Button(master = self.frame, 
									   text = "Add a line after", 
									   command = self.add_after)
		self.add_after_button.grid(row = 1, column = 0, sticky = W)

		# Remove Line Before Button
		self.rem_before_button = Button(master = self.frame, 
										text = "Remove a line before", 
										command = self.rem_before)
		self.rem_before_button.grid(row = 2, column = 0, sticky = W)

		# Remove Line After Button
		self.rem_after_button = Button(master = self.frame,
									   text = "Remove a line after",
									   command = self.rem_after)
		self.rem_after_button.grid(row = 3, column = 0, sticky = W)

		# Get Lyrics Button
		self.choose_button = Button(master = self.frame, 
									text = "Get a Song's Lyrics", 
									command = self.choose)
		self.choose_button.grid(row = 4, column = 0, sticky = W)

		# Tweet Button
		self.tweet_button = Button(master = self.frame, 
								   text = "Tweet", 
								   command = self.tweet)
		self.tweet_button.grid(row = 5, column = 0, sticky = W)

		# Album Label
		self.album_label = Label(master = self.frame, 
								 text = "Album: ")
		self.album_label.grid(row = 0, column = 1)

		# Song Label
		self.song_label = Label(master = self.frame, 
								text = "Song: ")
		self.song_label.grid(row = 1, column = 1)

		# Lyrics Label
		self.lyrics_label = Label(master = self.frame, 
								  text = "Lyrics: ", 
								  wraplength = 100)
		self.lyrics_label.grid(rowspan = 4, column = 1)

	def add_before(self): pass

	def add_after(self): pass

	def rem_before(self): pass

	def rem_after(self): pass

	def tweet(self) -> None:
		print("This song lyric has been posted to Twitter.")

	def choose(self) -> None:
		album, song = self.get_song()
		self.album_label.configure(text = "Album: {}".format(album))
		self.song_label.configure(text = "Song: {}".format(song))
		self.get_lyrics(song = song)

	def get_lyrics(self, song: str) -> None:
		scraper = Scraper()
		self.lyrics = scraper.process_lyrics(song_name = song)
		sample = scraper.sample_lyrics(text_arr = self.lyrics, 
									   line_max = App.LINE_MAX)
		self.lyrics_label.configure(text = "Lyrics: {}".format(sample))
		scraper.quit_scraper()

	@staticmethod
	def get_song() -> [str, str]:
		with open('../etc/alexg_data.json', 'r') as file:
			data = json.load(file)
		file.close()
		album = random.choice([album for album in data])
		song = random.choice([song for song in data[album]])
		return album, song


if __name__ == "__main__":
	root = Tk()
	root.geometry("500x200")
	root.wm_title('Twitter Lyrics Bot')
	app = App(master = root)

	root.mainloop()
