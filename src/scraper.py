# SELENIUM SCRAPER CLASS

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Scraper:
	'''
	| NOTE: this scraper extracts lyrics from https://genius.com
	|
	| METHODS:
	| - ability to scrape the data pertaining to the web 
	| 	element consisting of the song's lyrics
	| - ability to format the song name from the database into the URL
	| - ability to process (clean) the scraped lyrics
	| - ability to quit the scraper object when finished
	|
	| ATTRIBUTES:
	| - headless Selenium driver object used to surf the web
	| - filepath directed to the Selenium webdriver for the Chrome browser
	'''
	DRIVER = "/Users/jamesdeleon/Documents/chromedriver"

	def __init__(self) -> None:
		self.opt = Options()
		self.opt.headless = True
		self.driver = Chrome(Scraper.DRIVER, options = self.opt)

	def scrape_data(self, driver: object) -> str:
		'''
		- finds the web element associated with the hardcoded XPATH and URL
		'''
		try:
			data = WebDriverWait(driver, 10).until(
				EC.presence_of_element_located((By.XPATH, '//*[@id="lyrics-root"]/div[2]'))
			)
			data = data.text
		except:
			data = ''
		finally:
			return "NO LYRICS FOUND" if not data else data

	def process_lyrics(self, song_name: str) -> list:
		'''
		- any song in the song database that has a space character 
		  is replaced with a '-' character to play nicely with the URL specs
		'''
		song_name = song_name.replace(' ', '-')
		self.driver.get("https://www.genius.com/Alex-g-{}-lyrics/".format(song_name))
		text = self.scrape_data(driver = self.driver)
		return self.process_text(text = text)

	def process_text(self, text: str) -> list:
		'''
		- filters the lyric data by
			- giving each line their own array index
			- removing any extra indices with no data present
			- removing any instrumental queues enclosed by "[]"
			- removing any metadata ads for other songs with '|' char present
		'''
		text_arr = text.split('\n')
		text_arr = list(filter(None, text_arr))
		text_arr = [line for line in text_arr if not '[' in line]
		text_arr = [line for line in text_arr if not '|' in line]
		return text_arr

	def quit_scraper(self) -> None: self.driver.quit()


if __name__ == "__main__":
	pass