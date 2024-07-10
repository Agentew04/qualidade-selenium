from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class Driver:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(options=options)
        self.wait = WebDriverWait(self.driver, 10)

    def get(self, url):
        self.driver.get(url)

    def find_element(self, by, value):
        return self.wait.until(EC.presence_of_element_located((by, value)))

    def close(self):
        self.driver.quit()


def test_video_button():
    driver = Driver()
    try:
        driver.get("https://www.ut.edu")
        video_button = driver.find_element(By.CLASS_NAME, "video--vertical__button")
        assert video_button.is_displayed(), "O botão de vídeo não está visível"
        video_button.click()

    finally:
        driver.close()
    

def test_virtual_event_calendar():
    driver = Driver()
    try:
        driver.get("https://apply-undg.ut.edu/portal/virtual")
        available_date = driver.find_element(By.CLASS_NAME, "available")

        assert available_date.is_displayed(), "Nenhum elemento com a classe 'available' está visível"

        available_date.click()
        virtual_admissions_presentation_link = driver.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[text()='Virtual Admissions Presentation']"))
        )
        assert virtual_admissions_presentation_link.is_displayed(), "O link 'Virtual Admissions Presentation' não está visível"
        virtual_admissions_presentation_link.click()
    finally:
        driver.close()


def test_admissions_form():
    driver = Driver()
    try:
        driver.get("https://apply-undg.ut.edu/portal/virtual")
        available_date = driver.find_element(By.CLASS_NAME, "available")
        available_date.click()
        virtual_admissions_presentation_link = driver.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[text()='Virtual Admissions Presentation']"))
        )
        virtual_admissions_presentation_link.click()
        admissions_form= driver.wait.until(
            EC.presence_of_element_located((By.ID, "form_page_1"))
        )
        first_name = driver.find_element(By.ID, "form_8d4c442a-c1de-4b07-a395-87a3ff999b3e")
        first_name.send_keys("prego")

        assert first_name.get_attribute("value") == "prego"

        middle_name = driver.find_element(By.ID, "form_040f73be-559c-4902-a689-9f813ab604b0")
        middle_name.send_keys("preguinho")

        assert middle_name.get_attribute("value") == "preguinho"

        last_name = driver.find_element(By.ID, "form_2ef8b3f8-caa4-4702-9a5a-36c85dc9b06c")
        last_name.send_keys("pregão")

        assert last_name.get_attribute("value") == "pregão"

        month_dropdown = Select(driver.find_element(By.ID, "form_3668389e-ba93-40ac-b0c0-065b7f092741_m"))
        month_dropdown.select_by_value("07")  # July

        # Assuming the IDs for day and year fields
        day_field = driver.find_element(By.ID, "form_3668389e-ba93-40ac-b0c0-065b7f092741_d")
        day_field.send_keys("10")

        year_field = driver.find_element(By.ID, "form_3668389e-ba93-40ac-b0c0-065b7f092741_y")
        year_field.send_keys("2024")

        assert month_dropdown.first_selected_option.text == "July"
        assert day_field.get_attribute("value") == "10"
        assert year_field.get_attribute("value") == "2024"

        email = driver.find_element(By.ID, "form_a8a97ada-e3b4-4fad-b31b-2b6b68e83b73")
        email.send_keys("prego@gmail.com")

        assert email.get_attribute("value") == "prego@gmail.com"

        cell_phone = driver.find_element(By.ID, "form_a2e835b7-7d33-428e-b11a-20c7cd688fe0")
        cell_phone.send_keys("4002-8922")

        assert cell_phone.get_attribute("value") == "4002-8922"

        country_dropdown = Select(driver.find_element(By.ID, "form_8640c7ef-f956-43fc-a08f-e2badc25539b_country"))
        country_dropdown.select_by_visible_text("Brazil")

        assert country_dropdown.first_selected_option.text == "Brazil"

        street_address = driver.find_element(By.ID, "form_8640c7ef-f956-43fc-a08f-e2badc25539b_street")
        street_address.send_keys("Rua do Prego")

        assert street_address.get_attribute("value") == "Rua do Prego"

        city = driver.find_element(By.ID, "form_8640c7ef-f956-43fc-a08f-e2badc25539b_city")
        city.send_keys("Prego City")

        assert city.get_attribute("value") == "Prego City"

        state_dropdown = Select(driver.find_element(By.ID, "form_8640c7ef-f956-43fc-a08f-e2badc25539b_region"))
        state_dropdown.select_by_visible_text("Rio Grande do Sul")

        assert state_dropdown.first_selected_option.text == "Rio Grande do Sul"

        postal_code = driver.find_element(By.ID, "form_8640c7ef-f956-43fc-a08f-e2badc25539b_postal")
        postal_code.send_keys("90000-000")

        assert postal_code.get_attribute("value") == "90000-000"

        start_year_dropdown = Select(driver.find_element(By.ID, "form_0054640c-e0f3-4590-bd20-abf6c385040f"))
        start_year_dropdown.select_by_visible_text("2024")

        assert start_year_dropdown.first_selected_option.text == "2024"

        to_help_us_dropdown = Select(driver.find_element(By.ID, "form_66bce342-a498-4852-9ec2-d445fcf611da"))
        to_help_us_dropdown.select_by_visible_text("Auditing")

        assert to_help_us_dropdown.first_selected_option.text == "Auditing"

        major_selection = Select(driver.find_element(By.ID, "form_52734dbe-28c0-439d-85cd-8fc8913eac9d"))
        major_selection.select_by_visible_text("Computer Science")

        assert major_selection.first_selected_option.text == "Computer Science"

    finally:
        driver.close()


def test_map():
    driver = Driver()
    try:
        driver.get("https://www.ut.edu/about-ut/campus-map")

        map_frame = driver.find_element(By.ID, "map_frame")
        driver.driver.switch_to.frame(map_frame)

        search_input = driver.find_element(By.ID, "search-query")
        search_input.send_keys("Sykes Chapel")

        assert search_input.get_attribute("value") == "Sykes Chapel"

        search_button = driver.find_element(By.CLASS_NAME, "search-button")
        search_button.click()

        search_results = driver.find_element(By.CLASS_NAME, "search-results")
        assert search_results.is_displayed()

    finally:
        driver.close()