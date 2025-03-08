import time

from selenium.webdriver.common.by import By
from locators import (
    LOGIN_ACCOUNT_BTN,
    EXIT_BTN,
)

class TestExit:

    def test_profile_exit(self, browser_auth):
        browser_auth.find_element(By.XPATH, LOGIN_ACCOUNT_BTN).click()
        time.sleep(3)

        browser_auth.find_element(By.XPATH, EXIT_BTN).click()
        time.sleep(3)

        assert '/login' in browser_auth.current_url
