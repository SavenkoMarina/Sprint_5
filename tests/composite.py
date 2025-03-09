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
    PARENT_ELEMENT,
)

class TestComposite:

    def test_constructor_toppings(self, browser_auth):
        browser_auth.find_element(By.XPATH, TOPPINGS_BTN).click()
        WebDriverWait(browser_auth, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, TOPPINGS_HEADER)))

        header = browser_auth.find_element(By.XPATH, TOPPINGS_BTN).find_element(By.XPATH, PARENT_ELEMENT)
        assert "noselect" in header.get_attribute("class")

    def test_constructor_sauces(self, browser_auth):
        browser_auth.find_element(By.XPATH, SAUCES_BTN).click()
        WebDriverWait(browser_auth, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, SAUCES_HEADER)))

        header = browser_auth.find_element(By.XPATH, SAUCES_BTN).find_element(By.XPATH, PARENT_ELEMENT)
        assert "noselect" in header.get_attribute("class")

    def test_constructor_bread(self, browser_auth):
        browser_auth.find_element(By.XPATH, SAUCES_BTN).click()
        browser_auth.find_element(By.XPATH, BREAD_BTN).click()
        WebDriverWait(browser_auth, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, BREAD_HEADER)))

        header = browser_auth.find_element(By.XPATH, BREAD_BTN).find_element(By.XPATH, PARENT_ELEMENT)
        assert "noselect" in header.get_attribute("class")
