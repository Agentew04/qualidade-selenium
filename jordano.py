from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from time import sleep

service = Service()

def test_acessibility_button():
    driver = webdriver.Chrome(service=service)
    try:
        driver.get("https://www.ut.edu/campus-life/calendar")
        sleep(5)
        acessibilityButton = driver.find_element(By.XPATH, f"//*[@id='monsido-pageassist']")
        assert acessibilityButton.is_displayed()
        acessibilityButton.click()
        sleep(2)
        assert not acessibilityButton.is_displayed()
        
    finally:
        driver.quit()