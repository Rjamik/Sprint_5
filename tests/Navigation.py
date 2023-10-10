from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class TestNavigation:
    def test_navigation_to_account(self, driver):
        driver.find_element(By.XPATH, "//*[contains(@href,'/account')]").click()

        assert "login" in driver.current_url

    def test_navigation_from_account_to_constructor(self, driver):
        driver.find_element(By.XPATH, "//*[contains(@href,'/account')]").click()
        WebDriverWait(driver, timeout=5).until(EC.visibility_of_element_located((By.XPATH, "//h2[text()='Вход']")))

        assert "login" in driver.current_url

        driver.find_element(By.XPATH, "//a[contains(@href,'/')]").click()
        WebDriverWait(driver, timeout=5).until(EC.visibility_of_element_located((By.XPATH, "//h1[text()='Соберите бургер']")))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    def test_navigation_from_account_to_constructor_use_click_logo(self, driver):
        driver.find_element(By.XPATH, "//*[contains(@href,'/account')]").click()
        WebDriverWait(driver, timeout=5).until(EC.visibility_of_element_located((By.XPATH, "//h2[text()='Вход']")))

        assert "login" in driver.current_url

        driver.find_element(By.CLASS_NAME, 'AppHeader_header__logo__2D0X2').click()
        WebDriverWait(driver, timeout=5).until(EC.visibility_of_element_located((By.XPATH, "//h1[text()='Соберите бургер']")))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    def test_navigation_through_components(self, driver):
        components = driver.find_elements(By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG')]")

        driver.find_element(By.XPATH, "//div[@style='display: flex;']").click()

        components[0].click()
        WebDriverWait(driver, timeout=5).until(EC.visibility_of_element_located((By.XPATH, "//h2[text()='Булки']")))

        current_scroll_position = driver.execute_script("return document.querySelector('.BurgerIngredients_ingredients__menuContainer__Xu3Mo').scrollTop")
        old_scroll_position = current_scroll_position

        components[1].click()
        WebDriverWait(driver, timeout=5).until(EC.visibility_of_element_located((By.XPATH, "//h2[text()='Соусы']")))

        current_scroll_position = driver.execute_script("return document.querySelector('.BurgerIngredients_ingredients__menuContainer__Xu3Mo').scrollTop")
        assert current_scroll_position != old_scroll_position
        old_scroll_position = current_scroll_position

        components[2].click()
        WebDriverWait(driver, timeout=5).until(EC.visibility_of_element_located((By.XPATH, "//h2[text()='Начинки']")))

        current_scroll_position = driver.execute_script("return document.querySelector('.BurgerIngredients_ingredients__menuContainer__Xu3Mo').scrollTop")
        assert current_scroll_position != old_scroll_position
