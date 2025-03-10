from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import (
    LOGIN_ACCOUNT_BTN,
    LOGO_BTN,
)
from urls import MAIN_URL

class TestAccount:
    def test_enter_account_page(self, browser_auth):
        browser_auth.get(MAIN_URL)
        WebDriverWait(browser_auth, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, LOGO_BTN)))

        browser_auth.find_element(By.XPATH, LOGIN_ACCOUNT_BTN).click()
        WebDriverWait(browser_auth, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, LOGO_BTN)))

        assert "/account/profile" in browser_auth.current_url