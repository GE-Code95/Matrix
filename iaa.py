from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import itertools

# TODO - Keep table updated

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

# Get the table rows
table = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//*[@id=\"flight_board-arrivel_table\"]")))

# Put the rows into a list
list_to_break = [cell.text for row in table.find_elements_by_css_selector('tr') for cell in
                 row.find_elements_by_tag_name('td')]

# Break the list into a nested list - each list is a row
result = [list(v) for k, v in itertools.groupby(list_to_break, key=lambda sep: sep == "") if not k]

# Insert into Pandas Dataframe.
df_flights = pd.DataFrame(result, columns=columns)

# Convert table to json.
flights_json = df_flights.to_json()


driver.close()
driver.quit()
