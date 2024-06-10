from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from time import sleep

service = Service()
driver = webdriver.Chrome(service=service)


def test_apply_now():
    try:
        driver.get("https://www.ut.edu")
        element = driver.find_element(By.XPATH, f"//*[@title='Apply Now']")
        element.click()
        assert "/apply" in driver.current_url
    finally:
        driver.quit()
