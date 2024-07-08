from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Driver:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)

    def get(self, url):
        self.driver.get(url)

    def find_element(self, by, value):
        return self.wait.until(EC.presence_of_element_located((by, value)))

    def find_elements(self, by, value):
        return self.wait.until(EC.presence_of_all_elements_located((by, value)))

    def close(self):
        self.driver.quit()
        
driver = Driver()
driver.get("https://www.ut.edu")