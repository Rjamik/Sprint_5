from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class TestLogin:
    def test_login_using_the_login_to_account_button(self, driver):
        email = 'user321@mail.ru'
        password = 'parol321'

        driver.find_element(By.XPATH, "//button[text()='Войти в аккаунт']").click()

        driver.find_element(By.XPATH, "//input[@name='name']").send_keys(email)
        driver.find_element(By.XPATH, "//input[@name='Пароль']").send_keys(password)
        driver.find_element(By.XPATH, "//button[text()='Войти']").click()

        WebDriverWait(driver, timeout=5).until(EC.visibility_of_element_located((By.XPATH, "//h1[text()='Соберите бургер']")))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    def test_login_using_the_account_button(self, driver):
        email = 'user321@mail.ru'
        password = 'parol321'

        WebDriverWait(driver, timeout=5).until(EC.visibility_of_element_located((By.XPATH, "//h1[text()='Соберите бургер']")))

        driver.find_element(By.XPATH, "//*[contains(@href,'/account')]").click()

        driver.find_element(By.XPATH, "//input[@name='name']").send_keys(email)
        driver.find_element(By.XPATH, "//input[@name='Пароль']").send_keys(password)
        driver.find_element(By.XPATH, "//button[text()='Войти']").click()

        WebDriverWait(driver, timeout=5).until(EC.visibility_of_element_located((By.XPATH, "//h1[text()='Соберите бургер']")))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'


    def test_login_in_registration_page(self, driver):
        email = 'user321@mail.ru'
        password = 'parol321'

        driver.find_element(By.XPATH, "//button[text()='Войти в аккаунт']").click()
        WebDriverWait(driver, timeout=5).until(EC.visibility_of_element_located((By.XPATH, "//h2[text()='Вход']")))

        driver.find_element(By.LINK_TEXT, 'Зарегистрироваться').click()
        WebDriverWait(driver, timeout=5).until(EC.visibility_of_element_located((By.XPATH, "//h2[text()='Регистрация']")))

        driver.find_element(By.LINK_TEXT, 'Войти').click()
        WebDriverWait(driver, timeout=5).until(EC.visibility_of_element_located((By.XPATH, "//h2[text()='Вход']")))

        driver.find_element(By.XPATH, "//input[@name='name']").send_keys(email)
        driver.find_element(By.XPATH, "//input[@name='Пароль']").send_keys(password)
        driver.find_element(By.XPATH, "//button[text()='Войти']").click()

        WebDriverWait(driver, timeout=5).until(EC.visibility_of_element_located((By.XPATH, "//h1[text()='Соберите бургер']")))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'


    def test_login_in_recover_password_page(self, driver):
        email = 'user321@mail.ru'
        password = 'parol321'

        driver.find_element(By.XPATH, "//button[text()='Войти в аккаунт']").click()
        WebDriverWait(driver, timeout=5).until(EC.visibility_of_element_located((By.XPATH, "//h2[text()='Вход']")))

        driver.find_element(By.LINK_TEXT, 'Восстановить пароль').click()
        WebDriverWait(driver, timeout=5).until(EC.visibility_of_element_located((By.XPATH, "//h2[text()='Восстановление пароля']")))

        driver.find_element(By.LINK_TEXT, 'Войти').click()
        WebDriverWait(driver, timeout=5).until(EC.visibility_of_element_located((By.XPATH, "//h2[text()='Вход']")))

        driver.find_element(By.XPATH, "//input[@name='name']").send_keys(email)
        driver.find_element(By.XPATH, "//input[@name='Пароль']").send_keys(password)
        driver.find_element(By.XPATH, "//button[text()='Войти']").click()

        WebDriverWait(driver, timeout=5).until(EC.visibility_of_element_located((By.XPATH, "//h1[text()='Соберите бургер']")))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
