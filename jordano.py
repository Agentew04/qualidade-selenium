from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from time import sleep
from datetime import datetime

service = Service()
driver = webdriver.Chrome(service=service)


# Testará se a data dos eventos mostrados é a data atual (mês e ano)
def test_events_date():
    driver.get("https://www.ut.edu/campus-life/calendar")

    iframe = driver.find_element(By.ID, "trumba.spud.0.iframe")
    driver.switch_to.frame(iframe)

    eventsDate = driver.find_element(
        By.XPATH, f"//div[@class='twSimpleTableGroupHead']"
    )
    assert eventsDate.is_displayed()

    expected_date = f"{datetime.now().strftime('%B')} {datetime.now().year}"
    sleep(5)
    assert eventsDate.text == expected_date


# Testará se o botão de mostrar todos os eventos está funcionando corretamente
def test_view_all_events_button():
    driver.get("https://www.ut.edu")

    element = driver.find_element(By.XPATH, f"//a[@title='View All Events']")
    assert element.is_displayed()

    driver.execute_script("arguments[0].click();", element)
    sleep(5)
    assert "/campus-life/calendar" in driver.current_url


# Testará se o botão de play do vídeo dos estudantes está funcionando corretamente
def test_students_video_play_button():
    driver.get("https://www.ut.edu")
    element = driver.find_element(
        By.XPATH, f"//button[@class='video--vertical__button']"
    )
    assert element.is_displayed()
    element.click()
    sleep(2)

    videoIframe = driver.find_element(By.CLASS_NAME, "video--vertical__iFrame")
    assert videoIframe.is_displayed()


# Testará se o botão de acessibilidade está funcionando corretamente (outros botões da acessibilidade não puderam ser selecionados pelo Selenium por algum motivo)
def test_acessibility_button():
    driver.get("https://www.ut.edu/campus-life/calendar")
    sleep(3)
    acessibilityButton = driver.find_element(By.XPATH, f"//*[@id='monsido-pageassist']")
    accessibilityImage = driver.find_element(
        By.XPATH, f"//img[@class='mon-logo-image']"
    )
    assert acessibilityButton.is_displayed()
    assert accessibilityImage.is_displayed()
    acessibilityButton.click()
    sleep(4)
    accessibilityImage = driver.find_element(
        By.XPATH, f"//img[@class='mon-logo-image']"
    )
    assert not accessibilityImage.is_displayed()
