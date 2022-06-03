# SELENIUM SCRAPER CLASS

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random

class Scraper:
	'''
	| METHODS:
	| - Note: this scraper extracts lyrics from genius.com
	|
	| ATTRIBUTES:
	| -
	'''
	DRIVER = "/Users/jamesdeleon/Documents/chromedriver"

	def __init__(self) -> None:
		self.opt = Options()
		self.opt.headless = True
		self.driver = Chrome(driver = Scraper.DRIVER, options = self.opt)

	def scrape_data(self, driver: object) -> str:
		try:
			data = WebDriverWait(driver, 10).until(
				EC.presence_of_element_located((By.XPATH, '//*[@id="lyrics-root"]/div[1]'))
			)
			data = data.text
		except:
			data = ''
		finally:
			return "NO LYRICS FOUND" if not data else data

	def process_lyrics(self, song_name: str) -> list:
		song_name = song_name.replace(' ', '-')
		self.driver.get("https://www.genius.com/Alex-g-{}-lyrics/".format(song_name))
		text = self.scrape_data(driver = self.driver)
		return self.process_text(text = text)

	def sample_lyrics(self, text_arr: list, line_max: int) -> list:
		index = random.randint(0, len(text_arr))
		return text_arr[index : (index + line_max)]

	@staticmethod
	def process_text(text: str) -> list:
		text_arr = text.split('\n')
		text_arr = list(filter(None, text_arr))
		text_arr = [line for line in text_arr if not '[' in line]
		return text_arr

	def quit_scraper(self) -> None:
		self.driver.quit()


if __name__ == "__main__":
	pass