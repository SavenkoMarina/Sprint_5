import time
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from locators import (
    AUTH_BTN_LOGIN,
    AUTH_INPUT_PWD,
    AUTH_INPUT_EMAIL,
)

@pytest.yield_fixture
def browser():
    b = webdriver.Chrome()
    yield b
    b.quit()


@pytest.yield_fixture
def browser_auth():
    b = webdriver.Chrome()
    b.get("https://stellarburgers.nomoreparties.site/login")
    time.sleep(3)

    b.find_element(By.XPATH, AUTH_INPUT_EMAIL).send_keys("mnedozrelova@gmail.com")
    b.find_element(By.XPATH, AUTH_INPUT_PWD).send_keys("123456")
    b.find_element(By.XPATH, AUTH_BTN_LOGIN).click()
    time.sleep(3)

    yield b
    b.quit()