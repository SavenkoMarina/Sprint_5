from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import (
    REG_INPUT_NAME,
    REG_INPUT_PASSWORD,
    REG_BTN_REG,
    REG_TEXT_ERROR_PWD,
    AUTH_RECOVERY_HREF,
)
from urls import REG_URL
from helpers import generate_email


class TestRegistration:
    def test_registration_success(self, browser):
        browser.get(REG_URL)

        name_elem, email_elem = browser.find_elements(By.XPATH, REG_INPUT_NAME)
        name_elem.send_keys("Марина")
        email_elem.send_keys(f"{generate_email()}@ya.ru")

        pwd_elem = browser.find_element(By.XPATH, REG_INPUT_PASSWORD)
        pwd_elem.send_keys("123556")

        browser.find_element(By.XPATH, REG_BTN_REG).click()
        WebDriverWait(browser, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, AUTH_RECOVERY_HREF)))

        assert '/login' in browser.current_url


    def test_registration_pwd(self, browser):
        browser.get(REG_URL)

        name_elem, email_elem = browser.find_elements(By.XPATH, REG_INPUT_NAME)
        name_elem.send_keys("Марина")
        email_elem.send_keys(f"{generate_email()}@ya.ru")

        pwd_elem = browser.find_element(By.XPATH, REG_INPUT_PASSWORD)
        pwd_elem.send_keys("12355")

        browser.find_element(By.XPATH, REG_BTN_REG).click()

        label_error_elem = browser.find_element(By.XPATH, REG_TEXT_ERROR_PWD)
        assert label_error_elem.text == 'Некорректный пароль'