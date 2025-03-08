import time

from selenium.webdriver.common.by import By
from locators import (
    CONSTRUCTOR_BTN,
    LOGIN_ACCOUNT_BTN,
    LOGO_BTN,
)

class TestConstructor:

    def test_enter_account_page(self, browser_auth):
        browser_auth.find_element(By.XPATH, LOGIN_ACCOUNT_BTN).click()
        time.sleep(3)

        browser_auth.find_element(By.XPATH, CONSTRUCTOR_BTN).click()
        time.sleep(3)

        assert browser_auth.current_url == 'https://stellarburgers.nomoreparties.site/'

    def test_logo_page(self, browser_auth):
        browser_auth.find_element(By.XPATH, LOGIN_ACCOUNT_BTN).click()
        time.sleep(3)

        browser_auth.find_element(By.XPATH, LOGO_BTN).click()
        time.sleep(3)

        assert browser_auth.current_url == 'https://stellarburgers.nomoreparties.site/'