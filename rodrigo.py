from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep


def test_giving_button():
    firefox_driver = webdriver.Firefox()
    firefox_driver.get("https://www.ut.edu")
    sleep(1)
    giving_button = firefox_driver.find_element(By.XPATH, '//*[@id="page"]/header/div[1]/div[2]/nav/ul/li[5]/a')
    assert giving_button is not None
    print('Botao existe')
    sleep(1)
    assert giving_button.is_displayed()
    print('Botao esta aparecendo')
    sleep(1)
    giving_button.click()
    assert firefox_driver.current_url == "https://www.ut.edu/development-and-university-relations"
    sleep(1)

    sleep(10)
    give_now_button = firefox_driver.find_element(By.XPATH, '//*[@id="content"]/div/div/div[2]/div/div/ul/li[2]/a')
    assert give_now_button is not None
    print('Botao Give Now existe')
    assert give_now_button.is_displayed()
    print('Botao Give Now aparece')
    actions = ActionChains(firefox_driver)
    actions.move_to_element(give_now_button).perform()
    # WebDriverWait(driver, 20).until(
    #     EC.element_to_be_clickable((By.XPATH, '//*[@id="content"]/div/div/div[2]/div/div/ul/li[2]/a'))).click()
    give_now_button.click()
    assert firefox_driver.current_url == "https://www.ut.edu/development-and-university-relations/give-now"
    print('Botao Give Now Manda para pagina certa')
    firefox_driver.quit()


def testa_formulario_doacao():
    chrome_driver = webdriver.Chrome()
    chrome_driver.get('https://www.ut.edu/development-and-university-relations/give-now')
    print('Esperando 10s para js atualizar')
    sleep(10)
    fifty_dollars_donation_button = chrome_driver.find_element(By.XPATH, '//*[@id="bboxdonation_gift_rdlstGiving'
                                                                         'Levels"]/div[2]/div/label')
    # fifty_dollars_donation_input = chrome_driver.find_element(By.XPATH, '//*[@id="bboxdonation_gift_rdGiving'
    #                                                                     'Level2"]')
    hundred_dollars_donation_button = chrome_driver.find_element(By.XPATH, '//*[@id="bboxdonation_gift_rdlstGiving'
                                                                           'Levels"]/div[4]/div/label')
    # hundred_dollars_donation_input = chrome_driver.find_element(By.XPATH, '//*[@id="bboxdonation_gift_rdGiving'
    #                                                                       'Level4"]')
    assert fifty_dollars_donation_button is not None
    print('Botao de 50 dolares existe')
    assert hundred_dollars_donation_button is not None
    print('Botao de 100 dolares existe')

    assert fifty_dollars_donation_button.is_displayed()
    assert hundred_dollars_donation_button.is_displayed()
    print('Dois botoes de quantidade aparecem')

    hundred_dollars_donation_button.click()

    assert (hundred_dollars_donation_button.get_attribute("class")
            == "BBFormRadioLabel BBFormRadioLabelGivingLevel BBFormRadioLabelGivingLevelSelected")
    assert (fifty_dollars_donation_button.get_attribute("class")
            == "BBFormRadioLabel BBFormRadioLabelGivingLevel BBFormRadioLabelGivingLevelNotSelected")

    sleep(3)
    fifty_dollars_donation_button.click()
    assert (hundred_dollars_donation_button.get_attribute("class")
            == "BBFormRadioLabel BBFormRadioLabelGivingLevel BBFormRadioLabelGivingLevelNotSelected")
    assert (fifty_dollars_donation_button.get_attribute("class")
            == "BBFormRadioLabel BBFormRadioLabelGivingLevel BBFormRadioLabelGivingLevelSelected")
    print('Clicar no outro radiobutton apaga o primeiro')
    sleep(4)

    primeiro_nome_textbox = chrome_driver.find_element(By.XPATH, '//*[@id="bboxdonation_billing_txtFirstName"]')
    assert primeiro_nome_textbox is not None
    assert primeiro_nome_textbox.is_displayed()
    primeiro_nome_textbox.send_keys('Carlos')
    sleep(1)

    segundo_nome_textbox = chrome_driver.find_element(By.XPATH, '//*[@id="bboxdonation_billing_txtLastName"]')
    assert segundo_nome_textbox is not None
    assert segundo_nome_textbox.is_displayed()
    segundo_nome_textbox.send_keys('Silva')
    sleep(1)

    email_textbox = chrome_driver.find_element(By.XPATH, '//*[@id="bboxdonation_billing_txtEmail"]')
    assert email_textbox is not None
    assert email_textbox.is_displayed()
    email_textbox.send_keys('teste@gmail.com')
    sleep(1)

    country_combobox = chrome_driver.find_element(By.XPATH, '//*[@id="bboxdonation_billing_billingAddress_ddCountry"]')
    assert country_combobox is not None
    assert country_combobox.is_displayed()
    countries_options = country_combobox.find_elements(By.XPATH, '*')
    assert len(countries_options) == 5
    print('Tem os 5 paises')
    sleep(1)

    endereco_textbox = chrome_driver.find_element(By.XPATH, '//*[@id="bboxdonation_billing_billingAddress_txtAddress"]')
    assert endereco_textbox is not None
    assert endereco_textbox.is_displayed()
    endereco_textbox.send_keys('palacio do planalto')
    sleep(1)

    submit = chrome_driver.find_element(By.XPATH, '//*[@id="bboxdonation_btnSecurePayment"]')
    assert submit is not None
    assert submit.is_displayed()

    ActionChains(chrome_driver).move_to_element(submit).perform()
    assert submit.value_of_css_property("background-color") == "rgba(0, 178, 0, 1)"
    assert submit.value_of_css_property("border") == "0 solid rgba(0, 178, 0, 1)"
    sleep(1)
    chrome_driver.quit()


def test_expander_admissions():
    firefox_driver = webdriver.Firefox()
    firefox_driver.get("https://www.ut.edu")

    admissions = firefox_driver.find_element(By.XPATH, '//*[@id="page"]/header/div[1]/div[3]/nav/ul/li[1]/a')
    assert admissions is not None
    assert admissions.is_displayed()
    sleep(4)

    ActionChains(firefox_driver).move_to_element(admissions).perform()
    sleep(3)
    parent = admissions.find_element(By.XPATH, './..')
    ul = parent.find_element(By.XPATH, './ul')
    lis = ul.find_elements(By.XPATH, '*')
    sleep(3)
    assert len(lis) == 9
    print("todos elementos estao ali")

    sleep(3)

    for li in lis:
        ActionChains(firefox_driver).move_to_element(li).perform()
        sleep(1)
        assert li.is_displayed()
        print('Elemento visivel')
        sleep(1)

    lis[-1].click()
    assert firefox_driver.current_url == 'https://www.ut.edu/admissions/spartan-ambassadors'
    firefox_driver.quit()


def test_expander_academics():
    firefox_driver = webdriver.Firefox()
    firefox_driver.get("https://www.ut.edu")

    academics = firefox_driver.find_element(By.XPATH, '//*[@id="page"]/header/div[1]/div[3]/nav/ul/li[3]/a')
    assert academics is not None
    assert academics.is_displayed()
    sleep(4)

    ActionChains(firefox_driver).move_to_element(academics).perform()
    sleep(3)
    parent = academics.find_element(By.XPATH, './..')
    ul = parent.find_element(By.XPATH, './ul')
    lis = ul.find_elements(By.XPATH, '*')
    sleep(3)
    assert len(lis) == 7
    print("todos elementos estao ali")

    sleep(3)

    for li in lis:
        ActionChains(firefox_driver).move_to_element(li).perform()
        sleep(1)
        assert li.is_displayed()
        print('Elemento visivel')
        sleep(1)

    lis[-1].click()
    assert firefox_driver.current_url == 'https://www.ut.edu/academics/accreditation'
    firefox_driver.quit()
