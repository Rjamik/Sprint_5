import random

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class TestRegistration:
    def test_reginstration_with_valid_password(self, driver):
        name = 'Yarik'
        email = 'yarik@mail.ru'
        password = '123456'

        driver.find_element(By.XPATH, "//button[text()='Войти в аккаунт']").click()
        WebDriverWait(driver, timeout=5).until(EC.visibility_of_element_located((By.XPATH, "//h2[text()='Вход']")))

        driver.find_element(By.LINK_TEXT, 'Зарегистрироваться').click()

        driver.find_element(By.XPATH, "//label[text()='Имя']/following-sibling::*").send_keys(name)
        driver.find_element(By.XPATH, "//label[text()='Email']/following-sibling::*").send_keys(email)
        driver.find_element(By.XPATH, "//label[text()='Пароль']/following-sibling::*").send_keys(password)

        driver.find_element(By.XPATH, "//button[text()='Зарегистрироваться']").click()
        WebDriverWait(driver, timeout=5).until(EC.visibility_of_element_located((By.XPATH, "//h2[text()='Вход']")))

        assert "login" in driver.current_url

    def test_reginstration_with_invalid_password(self, driver):
        name = 'Yarik'
        email = 'yarik@mail.ru'
        password = '12345'

        driver.find_element(By.XPATH, "//button[text()='Войти в аккаунт']").click()
        WebDriverWait(driver, timeout=5).until(EC.visibility_of_element_located((By.XPATH, "//h2[text()='Вход']")))

        driver.find_element(By.LINK_TEXT, 'Зарегистрироваться').click()
        WebDriverWait(driver, timeout=5).until(EC.visibility_of_element_located((By.XPATH, "//h2[text()='Регистрация']")))

        driver.find_element(By.XPATH, "//label[text()='Имя']/following-sibling::*").send_keys(name)
        driver.find_element(By.XPATH, "//label[text()='Email']/following-sibling::*").send_keys(email)
        driver.find_element(By.XPATH, "//label[text()='Пароль']/following-sibling::*").send_keys(password)

        driver.find_element(By.XPATH, "//button[text()='Зарегистрироваться']").click()
        WebDriverWait(driver, timeout=5).until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Некорректный')]")))

        assert driver.find_element(By.XPATH, "//*[contains(text(), 'Некорректный')]").text == "Некорректный пароль"