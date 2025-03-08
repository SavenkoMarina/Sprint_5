import time

from selenium.webdriver.common.by import By
from locators import (
    LOGIN_ENTER_BTN,
    LOGIN_ACCOUNT_BTN,
    LOGIN_REG_BTN,
    LOGIN_RECOVER_BTN,
)


class TestLogin:
    MAIN_URL = 'https://stellarburgers.nomoreparties.site/'
    REG_URL = 'https://stellarburgers.nomoreparties.site/register'
    RECOVER_URL = 'https://stellarburgers.nomoreparties.site/forgot-password'

    def test_login_enter_btn(self, browser):
        browser.get(self.MAIN_URL)
        browser.find_element(By.XPATH, LOGIN_ENTER_BTN).click()
        time.sleep(5)
        assert '/login' in browser.current_url


    def test_login_account(self, browser):
        browser.get(self.MAIN_URL)
        browser.find_element(By.XPATH, LOGIN_ACCOUNT_BTN).click()
        time.sleep(5)
        assert '/login' in browser.current_url

    def test_login_from_registration(self, browser):
        browser.get(self.REG_URL)
        browser.find_element(By.XPATH, LOGIN_REG_BTN).click()
        time.sleep(5)
        assert '/login' in browser.current_url

    def test_login_recover(self, browser):
        browser.get(self.RECOVER_URL)
        browser.find_element(By.XPATH, LOGIN_RECOVER_BTN).click()
        time.sleep(5)
        assert '/login' in browser.current_url