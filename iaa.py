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

# Get the table headers
table_headers = WebDriverWait(driver, 10).until(
    EC.visibility_of_any_elements_located((By.XPATH, "//table[@id='flight_board-arrivel_table']//thead//tr//th")))

# Put headers names into a list
columns = list(map(lambda name: name.text, table_headers))

'''table_rows = WebDriverWait(driver, 10).until(
    EC.visibility_of_any_elements_located((By.XPATH, "//*[@id='flight_board-arrivel_table']/tbody/tr/td/div/div[2]")))

for row in table_rows:
    print(row.text)'''

table = WebDriverWait(driver, 10).until(
    EC.visibility_of_any_elements_located((By.XPATH, "//table[@id='flight_board-arrivel_table']")))

for row in table.find_elements_by_xpath(".//tr"):
    print([td.text for td in row.find_elements_by_xpath(".//td[@class='dddefault'][1]]")])

driver.close()
driver.quit()
