from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

PATH = "C:/Program Files (x86)/chromedriver.exe"
driver = webdriver.Chrome(PATH)
url = 'https://www.bbc.com/'

driver.get(url)
actions = ActionChains(driver)


# Getting all sections from BBC
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a.block-link__overlay-link")))
time.sleep(1)
media_list = driver.find_elements_by_css_selector("a.block-link__overlay-link")
for idx, val in enumerate(media_list):
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a.block-link__overlay-link")))
    time.sleep(1)
    media_list = driver.find_elements_by_css_selector("a.block-link__overlay-link")
    item = media_list[idx]
    actions.move_to_element(item).perform()
    time.sleep(0.5)
    item.click()
    #scrape your data
    driver.execute_script("window.history.go(-1)")

driver.close()
driver.quit()


class Base(webdriver.Chrome):
    path = r"C:/Program Files (x86)/chromedriver.exe"

    def __init__(self, driver_path=f"{path}"):
        self.drive_path = driver_path
        super(Base, self).__init__()

    def access_page(self, url):
        self.get(url)


