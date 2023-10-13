from selenium.webdriver.common.by import By

class Locators:
   loginButton = (By.XPATH, "//button[text()='Войти в аккаунт']")  # Кнопка 'Войти в аккаунт'
   emailField = (By.XPATH, "//input[@name='name']")  # Поле 'Email'
   passwordField = (By.XPATH, "//input[@name='Пароль']")  # Поле 'Пароль'
   enterButton = (By.XPATH, "//button[text()='Войти']")  # Кнопка 'Войти'
   makeBurgerText = (By.XPATH, "//h1[text()='Соберите бургер']")  # Заголовок 'Соберите бургер'
   profileButton = (By.XPATH, "//*[contains(@href,'/account')]")  # Кнопка 'Личный кабинет'
   enterLink = (By.XPATH, "//h2[text()='Вход']")  # Ссылка с надписью 'Вход'
   registrationLink = (By.XPATH, "//h2[text()='Регистрация']")  # Ссылка с надписью 'Регистрация'
   recoverPasswordLink = (By.XPATH, "//h2[text()='Восстановление пароля']")  # Ссылка с надписью 'Восстановление пароля'
   profileLink = (By.XPATH, "//a[text()='Профиль']")  # Ссылка с надписью 'Профиль'
   logoutButton = (By.XPATH, "//button[text()='Выход']")  # Кнопка 'Выход'
   StellaBurgerLogo = (By.CLASS_NAME, 'AppHeader_header__logo__2D0X2')  # Лого Stella Burger
   tabComponents = (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG')]")  # Табы компонентов "Булки", "Соусы", "Начинки
   tabsBlock = (By.XPATH, "//div[@style='display: flex;']")  # Блок, включающий названия разделов "Булки", "Соусы", "Начинки"
   tabAreaBuns = (By.XPATH, "//h2[text()='Булки']")  # Название раздела 'Булки' в области, которая имеет скролл
   tabAreaSauces = (By.XPATH, "//h2[text()='Соусы']")  # Название раздела 'Соусы' в области, которая имеет скролл
   tabAreaFillings = (By.XPATH, "//h2[text()='Начинки']")  # Название раздела 'Начинки' в области, которая имеет скролл
   tabScroll = ('.BurgerIngredients_ingredients__menuContainer__Xu3Mo')  # скролл в области с компонентами для сборки бургера
   registrationNameField = (By.XPATH, "//label[text()='Имя']/following-sibling::*")  # Поле 'Имя'
   registrationEmailField = (By.XPATH, "//label[text()='Email']/following-sibling::*")  # Поле 'Email'
   registrationPasswordField = (By.XPATH, "//label[text()='Пароль']/following-sibling::*")  # Поле 'Пароль'
   registerButton = (By.XPATH, "//button[text()='Зарегистрироваться']")  # Кнопка 'Зарегистрироваться'
   incorrectPasswordText = (By.XPATH, "//*[contains(text(), 'Некорректный')]")  # Надпись 'Некорректный пароль'
   constructorButton = (By.XPATH, "//a[contains(@href,'/')]")  # Кнопка 'Конструктор'