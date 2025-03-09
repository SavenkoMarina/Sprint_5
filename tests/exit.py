from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import (
    LOGIN_ACCOUNT_BTN,
    EXIT_BTN,
    AUTH_BTN_LOGIN,
)


class TestExit:

    def test_profile_exit(self, browser_auth):
        browser_auth.find_element(By.XPATH, LOGIN_ACCOUNT_BTN).click()
        WebDriverWait(browser_auth, 5).until(expected_conditions.element_to_be_clickable((By.XPATH, EXIT_BTN)))
        browser_auth.find_element(By.XPATH, EXIT_BTN).click()
        WebDriverWait(browser_auth, 5).until(expected_conditions.element_to_be_clickable((By.XPATH, AUTH_BTN_LOGIN)))

        assert '/login' in browser_auth.current_url
