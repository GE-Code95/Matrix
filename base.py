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

bbc_hrefs = []
content_dict = {}

WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a.block-link__overlay-link")))
time.sleep(1)
media_list = driver.find_elements_by_css_selector("a.block-link__overlay-link")

for link in media_list:
    bbc_hrefs.append(link.get_attribute('href'))


def previous():
    driver.execute_script("window.history.go(-1)")


for idx, url in enumerate(bbc_hrefs):
    driver.get(url)
    header = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "main-heading")))
    if header is None:
        header = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
            (By.XPATH, "//div[@class='article-headline__text b-reith-sans-font b-font-weight-300']")))
        data_block = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//div[@class='article__body-content']")))
        for block in data_block:
            print(block.text)
        previous()
    else:
        data_block = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//div[@data-component='text-block']")))
        for block in data_block:
            print(block.text)
        previous()

    '''content_dict[idx] = header.text
    print(content_dict)

    # This part gets the rest of the articles.
    header = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
        (By.XPATH, "//div[@class='article-headline__text b-reith-sans-font b-font-weight-300']")))
    data_block = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, "//div[@class='article__body-content']")))
    for block in data_block:
        print(block.text)

    content_dict[idx] = header.text
    print(content_dict)
    previous()
'''
driver.close()
driver.quit()

'''class Base(webdriver.Chrome):

    # Add previous

    def __init__(self, driver_path="C:/Program Files (x86)/chromedriver.exe", teardown=False):
        self.teardown = teardown
        self.driver_path = driver_path
        os.environ['PATH'] += self.driver_path
        super(Base, self).__init__()

    def access_page(self, url):
        self.get(url)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()
'''
