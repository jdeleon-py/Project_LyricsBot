# GUI CLASS

from tkinter import Tk, Frame, Menu
from tkinter import Button, Label, Entry
import random
import json
import time
from scraper import Scraper

class App:
	'''
	| METHODS:
	| -
	|
	| ATTRIBUTES:
	| -
	'''
	def __init__(self, master: object) -> None:
		self.master = master
		self.frame = Frame(self.master)
		self.frame.pack()

		self.tweet_button = Button(self.frame, text = "Tweet", command = self.tweet)
		self.choose_button = Button(self.frame, text = "Get a Song's Lyrics", command = self.choose)

		self.album_label = Label(self.frame, text = "Album: ")
		self.song_label = Label(self.frame, text = "Song: ")
		self.lyrics_label = Label(self.frame, text = "Lyrics: ")

		self.tweet_button.grid(row = 1, columnspan = 3)
		self.choose_button.grid(row = 2, columnspan = 3)
		self.album_label.grid(row = 3, columnspan = 9)
		self.song_label.grid(row = 4, columnspan = 9)
		self.lyrics_label.grid(row = 5, columnspan = 9)

	def tweet(self) -> None:
		print("This song lyric has been posted to Twitter.")

	def choose(self) -> None:
		album, song = self.get_song()
		self.album_label.configure(text = "Album: {}".format(album))
		self.song_label.configure(text = "Song: {}".format(song))
		time.sleep(3)
		self.get_lyrics(song = song)

	def get_lyrics(self, song: str) -> None:
		scraper = Scraper()
		lyrics = scraper.process_lyrics(song_name = song)
		self.lyrics_label.configure(text = "Lyrics: {}".format(lyrics))
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
	root.geometry("400x400")
	root.wm_title('Twitter Lyrics Bot')
	app = App(master = root)

	root.mainloop()