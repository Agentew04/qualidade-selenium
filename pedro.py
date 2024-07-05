from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from time import sleep

service = Service()


# def test_apply_now():
#     driver = webdriver.Chrome(service=service)
#     try:
#         driver.get("https://www.ut.edu")
#         element = driver.find_element(By.XPATH, f"//a[@title='Apply Now']")
#         assert element.is_displayed()
#         element.click()
#         assert "/apply" in driver.current_url
#     finally:
#         driver.quit()


def test_play_button():
    driver = webdriver.Chrome(service=service)
    try:
        driver.get("https://www.ut.edu")
        scrollToElement = driver.find_element(
            By.XPATH, f"//section[@class='tray tray-instagram']"
        )
        actions = ActionChains(driver)
        actions.move_to_element(scrollToElement).perform()
        element = driver.find_element(By.XPATH, f"//img[@alt='Play']")
        assert element.is_displayed()
        element.click()
        video_container = driver.find_element(
            By.XPATH, f"//div[@class='html5-video-container']"
        )
        assert video_container.is_displayed()
    finally:
        driver.quit()
