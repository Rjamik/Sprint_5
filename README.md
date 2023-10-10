Автотесты покрывают функционал:
•	Регистрация
•	Авторизация
•	Навигация по сервису
•	Выход из системы
Проект включает файлы:
•	conftest.py - файл конфигурации для автотестов
•	login.py - автотесты по авторизации
•	logout.py - автотесты по выходу из системы
•	navigation.py - автотесты по навигации
•	registration.py - автотесты по регистрации
Список автотестов:
•	Регистрация:
o	test_reginstration_with_valid_password - регистрация с валидным паролем
o	test_reginstration_with_invalid_password - регистрация с невалидным паролем
•	Авторизация:
o	test_login_using_the_login_to_account_button - авторизация через кнопку "Войти в аккаунт"
o	test_login_using_the_account_button - авторизация через кнопку "Личный кабинет"
o	test_login_in_registration_page - авторизация через кнопку в форме регистрации
o	test_login_in_recover_password_page - через кнопку в форме восстановления пароля
•	Навигация:
o	test_navigation_to_account - переход по клику на "Личный кабинет"
o	test_navigation_from_account_to_constructor - переход из личного кабинета в конструктор
o	test_navigation_from_account_to_constructor_use_click_logo - переход из личного кабинета в конструктор через нажатие на лого Stellar Burgers
o	test_navigation_through_components - переход по разделам "Булки", "Соусы", "Начинки"
•	Выход из системы:
o	test_logout_from_profile - выход из системы


