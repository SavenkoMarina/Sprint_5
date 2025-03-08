#  Авторизация

# Поле ввода почты
AUTH_INPUT_EMAIL = "//*[@id='root']/div/main/div/form/fieldset[1]/div/div/input"
# Поле ввода пароля
AUTH_INPUT_PWD = "//*[@id='root']/div/main/div/form/fieldset[2]/div/div/input"
# Кнопка войти
AUTH_BTN_LOGIN = "//*[@id='root']/div/main/div/form/button"


# Тесты регистрации

# Поле ввода имени
REG_INPUT_NAME = "//*[@id='root']/div/main/div/form/fieldset[1]/div/div/input"
# Поле ввода пароля
REG_INPUT_PASSWORD = "//*[@id='root']/div/main/div/form/fieldset[3]/div/div/input"
# Поле ввода почты
REG_INPUT_EMAIL = "//*[@id='root']/div/main/div/form/fieldset[2]/div/div/input"
# Кнопка зарегистрироваться
REG_BTN_REG = "//*[@id='root']/div/main/div/form/button"
# Текст ошибки ввода пароля
REG_TEXT_ERROR_PWD = "//*[@id='root']/div/main/div/form/fieldset[3]/div/p"

# Тесты входа

# Кнопка войти в аккаунт
LOGIN_ENTER_BTN = "// *[ @ id = 'root'] / div / main / section[2] / div / button"
# Кнопка личный кабинет
LOGIN_ACCOUNT_BTN = "//*[@id='root']/div/header/nav/a"
#Кнопка войти на странице регистрации
LOGIN_REG_BTN = "//*[@id='root']/div/main/div/div/p/a"
#Кнопка войти на странице восстановления пароля
LOGIN_RECOVER_BTN = "//*[@id='root']/div/main/div/div/p/a"

# Тесты перехода в контруктор

# Ссылка "конструктор"
CONSTRUCTOR_BTN = "//*[@id='root']/div/header/nav/ul/li[1]/a"
# Логотип
LOGO_BTN = "//*[@id='root']/div/header/nav/div/a"

# Выход из аккаунта
EXIT_BTN = "//*[@id='root']/div/main/div/nav/ul/li[3]/button"

# Тесты перехода к разделам «Булки», «Соусы», «Начинки»

# Кнопка перехода к Булкам
BREAD_BTN = "//*[@id='root']/div/main/section[1]/div[1]/div[1]/span"
# Кнопка перехода к Соусам
SAUCES_BTN = "//*[@id='root']/div/main/section[1]/div[1]/div[2]"
# Кнопка перехода к Начинкам
TOPPINGS_BTN = "//*[@id='root']/div/main/section[1]/div[1]/div[3]"

# Заголовок "Булки"
BREAD_HEADER = "//*[@id='root']/div/main/section[1]/div[2]/h2[1]"
# Заголовок "Соусы"
SAUCES_HEADER = "//*[@id='root']/div/main/section[1]/div[2]/h2[1]"
# Заголовок "Начинки"
TOPPINGS_HEADER = "//*[@id='root']/div/main/section[1]/div[2]/h2[1]"
