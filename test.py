from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options


options = Options()
options.headless = True
options.binary_location = "C:/Program Files/Mozilla Firefox/firefox.exe"
PATH = "C:/Program Files (x86)/geckodriver.exe"
driver = webdriver.Firefox(executable_path=PATH, firefox_options=options)
url = 'https://www.bbc.com/worklife/article/20220119-is-having-a-favourite-child-really-a-bad-thing'

driver.get(url)

header = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
    (By.XPATH, "//div[@tabindex='-1']")))

intro = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
    (By.XPATH, "//div[@class='article__intro b-font-family-serif']")))

body = WebDriverWait(driver, 10).until(EC.visibility_of_any_elements_located((By.XPATH, "//div/div/p")))

print(header.text)
print(intro.text)

for p in body:
    print(p.text)

