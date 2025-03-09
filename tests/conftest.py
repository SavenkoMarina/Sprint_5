import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import (
    AUTH_BTN_LOGIN,
    AUTH_INPUT_PWD,
    AUTH_INPUT_EMAIL,
    TOPPINGS_HEADER,
)

@pytest.yield_fixture
def browser():
    b = webdriver.Chrome()
    yield b
    b.quit()


@pytest.fixture
def browser_auth(browser):
    browser.get("https://stellarburgers.nomoreparties.site/login")
    WebDriverWait(browser, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, AUTH_BTN_LOGIN)))

    browser.find_element(By.XPATH, AUTH_INPUT_EMAIL).send_keys("mnedozrelova@gmail.com")
    browser.find_element(By.XPATH, AUTH_INPUT_PWD).send_keys("123456")
    browser.find_element(By.XPATH, AUTH_BTN_LOGIN).click()
    WebDriverWait(browser, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, TOPPINGS_HEADER)))

    return browser