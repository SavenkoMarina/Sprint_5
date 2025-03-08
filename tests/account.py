import time

from selenium.webdriver.common.by import By
from locators import (
    LOGIN_ACCOUNT_BTN,
)

class TestAccount:
    MAIN_URL = 'https://stellarburgers.nomoreparties.site/'

    def test_enter_account_page(self, browser_auth):
        browser_auth.get(self.MAIN_URL)
        time.sleep(3)

        browser_auth.find_element(By.XPATH, LOGIN_ACCOUNT_BTN).click()
        time.sleep(3)

        assert "/account/profile" in browser_auth.current_url