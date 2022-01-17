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

main = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'page')))
print(main.text)
driver.close()


'''


class Base:
    def __init__(self, driver):
        self.driver = driver

    def click(self, by_locator):
        #WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()
        self.driver.find_element_by_class(by_locator).click()

    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.text

    def store(self, driver):
        self.driver = driver

    def search(self, driver):
        self.driver = driver

    def close(self, driver):
        self.driver = driver
        driver.close()
'''

