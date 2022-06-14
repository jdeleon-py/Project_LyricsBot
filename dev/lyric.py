# SONG AND LYRIC DATA CLASS

import json
import random

class Lyric:
	'''
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
		index = random.randint(0, len(self.lyrics))
		return index, index + Lyric.LINE_MAX

	def sample_lyrics(self) -> list:
		return self.lyrics[self.sample_index_min: self.sample_index_max]

	def get_song(self) -> [str, str]:
		with open(Lyric.SONG_FILE, 'r') as file:
			data = json.load(file)
		file.close()
		album = random.choice([album for album in data])
		song = random.choice([song for song in data[album]])
		return album, song


if __name__ == "__main__":
	pass