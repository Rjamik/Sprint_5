from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class TestLogout:
    def test_logout_from_profile(self, driver):
        email = 'user321@mail.ru'
        password = 'parol321'

        driver.find_element(By.XPATH, "//button[text()='Войти в аккаунт']").click()

        driver.find_element(By.XPATH, "//input[@name='name']").send_keys(email)
        driver.find_element(By.XPATH, "//input[@name='Пароль']").send_keys(password)
        driver.find_element(By.XPATH, "//button[text()='Войти']").click()

        WebDriverWait(driver, timeout=5).until(EC.visibility_of_element_located((By.XPATH, "//h1[text()='Соберите бургер']")))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

        driver.find_element(By.XPATH, "//*[contains(@href,'/account')]").click()
        WebDriverWait(driver, timeout=5).until(EC.visibility_of_element_located((By.XPATH, "//a[text()='Профиль']")))

        assert "profile" in driver.current_url

        driver.find_element(By.XPATH, "//button[text()='Выход']").click()
        WebDriverWait(driver, timeout=5).until(EC.visibility_of_element_located((By.XPATH, "//h2[text()='Вход']")))

        assert "login" in driver.current_url