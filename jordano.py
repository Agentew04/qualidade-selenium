from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from time import sleep
from datetime import datetime

service = Service()

# Testará se a data dos eventos mostrados é a data atual (mês e ano)
def test_events_date():
    driver = webdriver.Chrome(service=service)
    try:
        driver.get("https://www.ut.edu/campus-life/calendar")
        sleep(5)
        
        iframe = driver.find_element(By.ID, "trumba.spud.0.iframe")
        driver.switch_to.frame(iframe)

        eventsDate = driver.find_element(By.XPATH, f"//div[@class='twSimpleTableGroupHead']")
        assert eventsDate.is_displayed()

        expected_date = f"{datetime.now().strftime('%B')} {datetime.now().year}"
        assert eventsDate.text == expected_date
    finally:
        driver.quit()


#Testará se o botão de play do vídeo dos estudantes está funcionando corretamente
def test_students_video_play_button():
    driver = webdriver.Chrome(service=service)
    try:
        driver.get("https://www.ut.edu")
        element = driver.find_element(By.XPATH, f"//button[@class='video--vertical__button']")
        assert element.is_displayed()
        element.click()
        sleep(2)

        videoIframe = driver.find_element(By.CLASS_NAME, "video--vertical__iFrame")
        assert videoIframe.is_displayed()
    finally:
        driver.quit()


#Testará se o botão de acessibilidade está funcionando corretamente (outros botões da acessibilidade não puderam ser selecionados pelo Selenium por algum motivo)
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





        