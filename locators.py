#  Авторизация

# Поле ввода почты
AUTH_INPUT_EMAIL = "//input[@name='name']"
# Поле ввода пароля
AUTH_INPUT_PWD = "//input[@name='Пароль']"
# Кнопка войти
AUTH_BTN_LOGIN = "//button[contains(text(), 'Войти')]"
# Ссылка восстановления пароля
AUTH_RECOVERY_HREF = "//a[contains(text(), 'Восстановить пароль')]"


# Тесты регистрации

# Поле ввода имени
REG_INPUT_NAME = "//input[@name='name']"
# Поле ввода пароля
REG_INPUT_PASSWORD = "//input[@name='Пароль']"
# Кнопка зарегистрироваться
REG_BTN_REG = "//button[contains(text(), 'Зарегистрироваться')]"
# Текст ошибки ввода пароля
REG_TEXT_ERROR_PWD = "//p[contains(@class, 'input__error')]"

# Тесты входа

# Кнопка войти в аккаунт
LOGIN_ENTER_BTN = "//button[contains(text(), 'Войти в аккаунт')]"
# Кнопка личный кабинет
LOGIN_ACCOUNT_BTN = "//p[contains(text(), 'Личный Кабинет')]"
#Кнопка войти на странице регистрации
LOGIN_REG_BTN = "//a[contains(text(), 'Войти')]"
#Кнопка войти на странице восстановления пароля
LOGIN_RECOVER_BTN = "//a[contains(text(), 'Войти')]"

# Тесты перехода в конструктор

# Ссылка "конструктор"
CONSTRUCTOR_BTN = "//p[contains(text(), 'Конструктор')]"
# Логотип
LOGO_BTN = "//div[@class='AppHeader_header__logo__2D0X2']/a"
# Заголовок конструктора
CONSTRUCTOR_HEADER = "//h1[@class='text text_type_main-large mb-5 mt-10']"

# Выход из аккаунта
EXIT_BTN = "//button[contains(text(), 'Выход')]"

# Тесты перехода к разделам «Булки», «Соусы», «Начинки»

# Родительский элемент
PARENT_ELEMENT = "./.."

# Кнопка перехода к Булкам
BREAD_BTN = "//span[contains(text(), 'Булки')]"
# Кнопка перехода к Соусам
SAUCES_BTN = "//span[contains(text(), 'Соусы')]"
# Кнопка перехода к Начинкам
TOPPINGS_BTN = "//span[contains(text(), 'Начинки')]"

# Заголовок "Булки"
BREAD_HEADER = "//h2[contains(text(), 'Булки')]"
# Заголовок "Соусы"
SAUCES_HEADER = "//h2[contains(text(), 'Соусы')]"
# Заголовок "Начинки"
TOPPINGS_HEADER = "//h2[contains(text(), 'Начинки')]"
