import json

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

'''
1. Find elements for each section
2. Enter article
3. Extract data
'''
# ID, Name, Class


PATH = "C:/Program Files (x86)/chromedriver.exe"
driver = webdriver.Chrome(PATH)
url = 'https://www.bbc.com/'

driver.get(url)

'''
elems = driver.find_elements_by_class_name("media__link")
for elem in elems:
    print(elem.get_attribute("href"))
'''

media_dict = {}

media_list = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.TAG_NAME, "section"))
)



print(type(media_list))

print(media_dict)
driver.close()
driver.quit()



'''
class Base:
    def __init__(self, driver):
        self.driver = driver

    def download(self, by_locator):
        elements = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, by_locator)))
        print(type(elements))

    def close(self, driver):
        driver.quit()
'''


