from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd

# TODO fix status in first column - example CANCELED

# //table[@id='flight_board-arrivel_table']//tbody//tr[@role='row']//div/*

# //*[@id="flight_board-arrivel_table"]/tbody/tr/td/div/div[2]

PATH = "C:/Program Files (x86)/chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.maximize_window()
url = 'https://www.iaa.gov.il/en/airports/ben-gurion/flight-board/'

driver.get(url)

table = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//*[@id=\"flight_board-arrivel_table\"]")))

for row in table.find_elements_by_css_selector('tr'):
    for cell in row.find_elements_by_tag_name('td'):
        print(cell.text)
