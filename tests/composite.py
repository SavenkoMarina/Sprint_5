import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import (
    BREAD_BTN,
    SAUCES_BTN,
    TOPPINGS_BTN,
    BREAD_HEADER,
    SAUCES_HEADER,
    TOPPINGS_HEADER,
)

class TestComposite:

    def test_bread(self, browser_auth):
        browser_auth.find_element(By.XPATH, TOPPINGS_BTN).click()
        WebDriverWait(browser_auth, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, TOPPINGS_HEADER)))
        time.sleep(2)

        browser_auth.find_element(By.XPATH, SAUCES_BTN).click()
        WebDriverWait(browser_auth, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, SAUCES_HEADER)))
        time.sleep(2)

        browser_auth.find_element(By.XPATH, BREAD_BTN).click()
        WebDriverWait(browser_auth, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, BREAD_HEADER)))
        time.sleep(2)
