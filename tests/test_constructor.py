from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import (
    CONSTRUCTOR_BTN,
    LOGIN_ACCOUNT_BTN,
    LOGO_BTN,
    CONSTRUCTOR_HEADER,
)

class TestConstructor:

    def test_enter_account_page(self, browser_auth):
        browser_auth.find_element(By.XPATH, LOGIN_ACCOUNT_BTN).click()
        WebDriverWait(browser_auth, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, LOGO_BTN)))

        browser_auth.find_element(By.XPATH, CONSTRUCTOR_BTN).click()
        WebDriverWait(browser_auth, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, LOGO_BTN)))

        header = browser_auth.find_element(By.XPATH, CONSTRUCTOR_HEADER)
        assert header.text == 'Соберите бургер'

    def test_logo_page(self, browser_auth):
        browser_auth.find_element(By.XPATH, LOGIN_ACCOUNT_BTN).click()
        WebDriverWait(browser_auth, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, LOGO_BTN)))

        browser_auth.find_element(By.XPATH, LOGO_BTN).click()
        WebDriverWait(browser_auth, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, LOGO_BTN)))

        header = browser_auth.find_element(By.XPATH, CONSTRUCTOR_HEADER)
        assert header.text == 'Соберите бургер'