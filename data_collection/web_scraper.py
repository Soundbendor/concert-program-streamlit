import requests 
import shutil 
from selenium import webdriver
from selenium.webdriver.common.by import By
from PIL import Image
from urllib.request import urlopen
import json
import time

METADATA_KEYS = ['season', 'first_conductor', 'orch', 'first_location', 'first_venue', 'event_name', 'first_date', 'num_perfs', 'first_soloist', 'id']

start_page = 1
pages_to_scrape = 200
get_metadata = False
get_ocr = True	
get_images = False

def write_to_json(concert_dictionary):
	json_object = json.dumps(concert_dictionary, indent=4)
	with open("output_ocr2.json", "w") as outfile:
		outfile.write(json_object)

def download_image(image_url):
	file_name = 'example_output.png'
	im = Image.open(urlopen(image_url))
	print(im.info)
	im = im.convert("RGB")
	im.save(file_name)

def get_concert_meta_data(row, driver):
	metadata = {}
	data = ([i.text for i in row.find_elements(by=By.TAG_NAME, value="td")])
	for i in range(len(METADATA_KEYS)):
		metadata[METADATA_KEYS[i]] = data[i]
	return metadata

def get_concert_id(row, driver):
	row_data = []
	data = ([i.text for i in row.find_elements(by=By.TAG_NAME, value="td")])
	for attribute in data:
		row_data.append(attribute)
	print(row_data[9])
	return row_data[9]

def get_page(page_number, driver):
	concerts = {}
	i = 0
	for page in range(page_number):
		grid = driver.find_element(by=By.CLASS_NAME, value="backgrid")
		rows = grid.find_elements(by=By.TAG_NAME, value="tr")
		for row in rows[1:]:
			concert = {}
			if (get_metadata):
				concert['metadata'] = get_concert_meta_data(row, driver)
			if (get_ocr):
				concert['id'] = get_concert_id(row, driver)
				concert['ocr_text'] = get_concert_ocr(row, driver)
			if (get_images):
				concert['images'] = get_concert_images(row, driver)
			concerts[str(i)] = (concert)
			i+=1
		page_button = driver.find_element("xpath", '//a[@title="Next"]')
		# driver.implicitly_wait(5)
		page_button.click()
		time.sleep(1)
	return concerts

def get_concert_images(row, driver):

	image_sources = []
	
	# navigate window
	image_button = row.find_element(by=By.CLASS_NAME, value="uriCell")
	image_button.click()
	driver.switch_to.window(driver.window_handles[1])
	program_page = driver.find_element(by=By.CLASS_NAME, value="thumb")
	image_link = program_page.find_element(by=By.CSS_SELECTOR, value="a")
	image_link.click()

	# save image sources
	[image_sources.append(i.get_attribute("src")) for i in driver.find_elements(by=By.CLASS_NAME, value="BRpageimage")]

	# navigate window
	driver.close()
	driver.switch_to.window(driver.window_handles[0])

	# save images to dict
	concert_images = {}
	for i in range(len(image_sources)):
		concert_images[str(i)] = image_sources[i]

	return concert_images
	
def get_concert_ocr(row, driver):
	ocr_data = []
	image_button = row.find_element(by=By.CLASS_NAME, value="uriCell")
	image_button.click()
	driver.switch_to.window(driver.window_handles[1])
	url = driver.current_url
	url += "/fullview#page/1/mode/2up"
	print("url", url)
	driver2 = webdriver.Chrome()
	driver2.get(url)
	driver2.implicitly_wait(20)
	ocr_button_exists = driver2.find_elements(by=By.CLASS_NAME, value="NYTransMode")
	if len(ocr_button_exists) > 0:
		ocr_button = driver2.find_element(by=By.CLASS_NAME, value="NYTransMode")
		ocr_button.click()
		time.sleep(.5)
		content = driver2.find_elements(by=By.CLASS_NAME, value="BRtransview-content")
		if content: 
			for i in range(len(content)):
				print(i)
				ocr_data.append(content[i].text)
	driver2.implicitly_wait(20)
	driver.close()
	driver.switch_to.window(driver.window_handles[0])
	print(ocr_data)
	return(ocr_data)

def initialize():
	# select page to scrape
	driver = webdriver.Chrome()
	driver.get("https://archives.nyphil.org/performancehistory/#program")
	driver.implicitly_wait(0.5)
	submit_button = driver.find_element(by=By.CLASS_NAME, value="search-btn")
	submit_button.click()
	
	# navigate to correct pages
	for i in range(start_page): 
		page_button = driver.find_element("xpath", '//a[@title="Next"]')
		# driver.implicitly_wait(5)
		page_button.click()
		time.sleep(1)

	## run script to write to JSON
	concerts = get_page(pages_to_scrape, driver)
	write_to_json(concerts)	

initialize()
