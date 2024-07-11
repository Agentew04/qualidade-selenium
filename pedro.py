from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from time import sleep

service = Service()


options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(service=service, options=options)


def test_apply_now_link():
    driver.get("https://www.ut.edu")
    element = driver.find_element(By.XPATH, f"//a[@title='Apply Now']")
    assert element.is_displayed()
    element.click()
    sleep(5)
    assert "/apply" in driver.current_url


def test_play_button():
    driver.get("https://www.ut.edu")
    driver.execute_script("window.scrollTo(0, 1000);")
    sleep(3)
    element = driver.find_element(By.XPATH, f"//img[@alt='Play']")
    assert element.is_displayed()
    element.click()
    sleep(3)
    video_container = driver.find_element(By.CLASS_NAME, "mfp-content")
    assert video_container.is_displayed()


def is_valid_number(text):
    try:
        float(text)
        return True
    except ValueError:
        return False


def is_in_reasonable_temperature_range(temperature):
    return temperature >= -100 and temperature <= 150


def test_temperature_text():
    driver.get("https://www.ut.edu")
    temperature_text = driver.find_element(
        By.XPATH, f"//span[@class='js--weather-temperature']"
    )
    assert temperature_text.is_displayed()
    assert temperature_text.text.find("°") != -1
    text_temperature = temperature_text.text.replace("°", "")
    assert is_valid_number(text_temperature)
    assert is_in_reasonable_temperature_range(float(text_temperature))


def test_search_input():
    driver.get("https://www.ut.edu")
    start_search_button = driver.find_element(
        By.XPATH,
        f"//li[@class='search']//a[@href='#']",
    )
    start_search_button.click()
    sleep(2)
    search_input = driver.find_element(By.XPATH, f"//input[@id='searchInput']")
    search_input.send_keys("Computer Science")
    sleep(3)
    submit_button = driver.find_element(
        By.XPATH, f"//button[@aria-label='Submit Search']"
    )
    submit_button.click()
    sleep(3)
    assert "/search-results?q=Computer+Science" in driver.current_url
