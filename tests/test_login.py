from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import (
    LOGIN_ENTER_BTN,
    LOGIN_ACCOUNT_BTN,
    LOGIN_REG_BTN,
    LOGIN_RECOVER_BTN,
    LOGO_BTN,
)
from urls import (
    MAIN_URL,
    REG_URL,
    RECOVER_URL,
)


class TestLogin:
    def test_login_enter_btn(self, browser):
        browser.get(MAIN_URL)
        browser.find_element(By.XPATH, LOGIN_ENTER_BTN).click()
        WebDriverWait(browser, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, LOGO_BTN)))
        assert '/login' in browser.current_url


    def test_login_account(self, browser):
        browser.get(MAIN_URL)
        browser.find_element(By.XPATH, LOGIN_ACCOUNT_BTN).click()
        WebDriverWait(browser, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, LOGO_BTN)))
        assert '/login' in browser.current_url

    def test_login_from_registration(self, browser):
        browser.get(REG_URL)
        browser.find_element(By.XPATH, LOGIN_REG_BTN).click()
        WebDriverWait(browser, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, LOGO_BTN)))
        assert '/login' in browser.current_url

    def test_login_recover(self, browser):
        browser.get(RECOVER_URL)
        browser.find_element(By.XPATH, LOGIN_RECOVER_BTN).click()
        WebDriverWait(browser, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, LOGO_BTN)))
        assert '/login' in browser.current_url