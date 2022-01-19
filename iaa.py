from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


PATH = "C:/Program Files (x86)/chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.maximize_window()
url = 'https://www.iaa.gov.il/en/airports/ben-gurion/flight-board/'

driver.get(url)


table_headers = WebDriverWait(driver, 10).until(
    EC.visibility_of_any_elements_located((By.XPATH, "//table[@id='flight_board-arrivel_table']//thead//tr//th")))

columns = list(map(lambda name: name.text, table_headers))



driver.close()
driver.quit()