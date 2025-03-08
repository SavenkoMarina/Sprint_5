import time
import string
import random

from selenium.webdriver.common.by import By
from locators import (
    REG_INPUT_NAME,
    REG_INPUT_PASSWORD,
    REG_INPUT_EMAIL,
    REG_BTN_REG,
    REG_TEXT_ERROR_PWD,
)

EMAIL_LEN = 6


class TestRegistration:
    REG_URL = 'https://stellarburgers.nomoreparties.site/register'

    def _generate_email(self):
        chars = string.ascii_lowercase + string.digits
        return ''.join(random.choice(chars) for _ in range(EMAIL_LEN))


    def test_registration_success(self, browser):
        browser.get(self.REG_URL)

        name_elem = browser.find_element(By.XPATH, REG_INPUT_NAME)
        name_elem.send_keys("Марина")

        pwd_elem = browser.find_element(By.XPATH, REG_INPUT_PASSWORD)
        pwd_elem.send_keys("123556")

        email_elem = browser.find_element(By.XPATH, REG_INPUT_EMAIL)
        email_elem.send_keys(f"{self._generate_email()}@ya.ru")

        browser.find_element(By.XPATH, REG_BTN_REG).click()
        time.sleep(5)

        assert '/login' in browser.current_url


    def test_registration_pwd(self, browser):
        browser.get(self.REG_URL)

        name_elem = browser.find_element(By.XPATH, REG_INPUT_NAME)
        name_elem.send_keys("Марина")

        pwd_elem = browser.find_element(By.XPATH, REG_INPUT_PASSWORD)
        pwd_elem.send_keys("12355")

        email_elem = browser.find_element(By.XPATH, REG_INPUT_EMAIL)
        email_elem.send_keys(f"{self._generate_email()}@ya.ru")

        browser.find_element(By.XPATH, REG_BTN_REG).click()

        label_error_elem = browser.find_element(By.XPATH, REG_TEXT_ERROR_PWD)
        assert label_error_elem.text == 'Некорректный пароль'