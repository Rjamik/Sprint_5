from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from datatest import emailForLogin, passwordForLogin
from locators import Locators

class TestLogout:
    def test_logout_from_profile(self, driver):
        driver.find_element(*Locators.loginButton).click()

        driver.find_element(*Locators.emailField).send_keys(emailForLogin)
        driver.find_element(*Locators.passwordField).send_keys(passwordForLogin)
        driver.find_element(*Locators.enterButton).click()

        WebDriverWait(driver, timeout=5).until(EC.visibility_of_element_located(Locators.makeBurgerText))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

        driver.find_element(*Locators.profileButton).click()
        WebDriverWait(driver, timeout=5).until(EC.visibility_of_element_located(Locators.profileLink))

        assert "profile" in driver.current_url

        driver.find_element(*Locators.logoutButton).click()
        WebDriverWait(driver, timeout=5).until(EC.visibility_of_element_located(Locators.enterLink))

        assert "login" in driver.current_url
