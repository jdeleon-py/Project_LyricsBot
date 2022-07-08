# SONG AND LYRIC DATA CLASS

import json
import random

class Lyric:
	'''
	| METHODS:
	| - ability to save the used lyrics (and stats) to a continuously written json file
	| - ability to randomly determine where in a 'song' the app will choose lyrics from
	| - ability to randomly choose a random song from a manually generated database of
	|	the artist's discography
	|
	| ATTRIBUTES:
	| - string output of the album
	| - string output of the song
	| - list of lyrics per selected song (delimiter = '\n')
	| - a sliced array from the lyrics array representing a sample
	| - an index representing where in the song the sample starts
	| - an index representing where in the song the sample ends
	| - a filepath directed to the collection of lysics already posted
	| - a filepath directed to the collection of songs to choose from
	| - a value representing the default number of lines of a song to sample from
	'''
	LINE_MAX = 3
	SONG_FILE = "../etc/alexg_song_data.json"
	UNIQUE_LYRICS_FILE = "../etc/alexg_lyrics_data.json"

	def __init__(self):
		self.album = ''
		self.song = ''
		self.lyrics = []
		self.sample = []
		self.sample_index_min = 0
		self.sample_index_max = 0

	def add_unique_lyrics(self) -> None:
		'''
		- saves formatted data in an accumating json file
		'''
		formatted_data = {
			"Album": self.album,
			"Song": self.song,
			"Sample Index Min": self.sample_index_min,
			"Sample Index Max": self.sample_index_max,
			"Lyrics": self.sample
		}
		with open(Lyric.UNIQUE_LYRICS_FILE, "r+") as file:
			data = json.load(file)
			data["lyrics_data"].append(formatted_data)
			file.seek(0)
			json_obj = json.dumps(data, indent = 4)
			file.write(json_obj)
		file.close()

	def random_index(self) -> [int, int]:
		'''
		- returns where in a selected song the sample will be indexed
		'''
		index = random.randint(0, len(self.lyrics))
		return index, index + Lyric.LINE_MAX

	def sample_lyrics(self) -> list:
		'''
		- returns the sample with the selected song lyrics and selected indices
		'''
		return self.lyrics[self.sample_index_min: self.sample_index_max]

	def get_song(self) -> [str, str]:
		'''
		- choses a random song to sample from a database of the artist's discography
		'''
		with open(Lyric.SONG_FILE, 'r') as file:
			data = json.load(file)
		file.close()
		album = random.choice([album for album in data])
		song = random.choice([song for song in data[album]])
		return album, song


if __name__ == "__main__":
	pass