# import allure
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
#
#
# class TestKinopoisk():
#     def __init__(self, driver):
#             self.driver = driver
#             self.driver.maximize_window()
#             self.driver.implicitly_wait(20)
#
#
#     @allure.step("Вводим имя {names}")
#     def poisk_film(self, names: str):
#         """
#            Поиск фильма по названию.
#            Можно указывать часть названия, если не помните полное.
#            Поиск будет произведён и вам откроется список фильмов
#            в которых будет присутствовать часть введённого названия.
#         """
#         poisk = self.driver.find_element(By.CSS_SELECTOR, 'input[name="kp_query"]')
#         poisk.send_keys(names, Keys.RETURN)
#
#     @allure.step("Проверка ввода в поисковую строку: '{text}'")
#     def input_name(self, text: str):
#         """
#            Здесь мы проверяем отображение в поисковой строке ввод:
#            букв, цифр, символов.
#            Открываться cсылки и куда-то переходить мы не должны.
#         """
#         poi = self.driver.find_element(By.CSS_SELECTOR, 'input[name="kp_query"]')
#         poi.send_keys(text)
#
#     @allure.step("Запустить трейлер для просмотра")
#     def play_trailer(self):
#         self.driver.find_element(By.CSS_SELECTOR, '[class="pic"]').click()
#         self.driver.find_element(By.CSS_SELECTOR, '[class="style_button__PNtXT styles_button__1_G0A styles_button_trailer__ORo93 style_buttonSize52__b5OBe style_buttonPrimary__ndPAb style_buttonDark__beFpy" name="Trailer" data-test-id="ContentActions_trailer">Трейлер</button>]').click()
#
#
#     @allure.step("Авторизуемся")
#     def avtorizacia(self, login: str, passwd: str):
#         self.driver.get('https://passport.yandex.ru/auth/add/login?origin=kinopoisk&retpath=https%3A%2F%2Fsso.passport.yandex.ru%2Fpush%3Fretpath%3Dhttps%253A%252F%252Fwww.kinopoisk.ru%252F%26uuid%3D8417c1ba-4e6f-4c76-8245-a8311802e466')    # noqa: E501
#         self.driver.find_element(By.ID, 'loginField').send_keys(login, Keys.RETURN)
#         self.driver.set_page_load_timeout(10)
#         self.driver.find_element(By.ID, 'passp-field-passwd').send_keys(passwd, Keys.RETURN)

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class TestKinopoisk:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://www.kinopoisk.ru/")

    @allure.step("Поиск фильма: {name}")
    def poisk_film(self, name):
        search_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[name="kp_query"]'))
        )
        search_input.send_keys(name + Keys.RETURN)

    def is_results_found(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "search_results"))
        ).is_displayed()

    @allure.step("Ввод текста в поисковую строку")
    def input_name(self, text):
        search_input = self.driver.find_element(By.CSS_SELECTOR, 'input[name="kp_query"]')
        search_input.clear()
        search_input.send_keys(text)

    def get_search_text(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'input[name="kp_query"]').get_attribute("value")

    @allure.step("Открытие страницы фильма")
    def open_film_page(self, film_name):
        self.poisk_film(film_name)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".name a[href*='/film/']"))
        ).click()

    @allure.step("Воспроизведение трейлера")
    def play_trailer(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.trailer"))
        ).click()

    def is_trailer_playing(self):
        return WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".trailer-video iframe"))
        ).is_displayed()

    @allure.step("Авторизация пользователя {login}")
    def avtorizacia(self, login, passwd):
        # Нажимаем кнопку "Войти с логином" на странице выбора типа авторизации
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-type=login]"))
        ).click()

        # Вводим логин
        login_field = WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located((By.ID, "passp-field-login"))
        )
        login_field.send_keys(login)
        login_field.send_keys(Keys.RETURN)

        # Вводим пароль
        passwd_field = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.ID, "passp-field-passwd"))
        )
        passwd_field.send_keys(passwd)
        passwd_field.send_keys(Keys.RETURN)

    # @allure.step("Авторизуемся")
    # def avtorizacia(self, login: str, passwd: str):
    #     self.driver.get('https://passport.yandex.ru/auth/add/login?origin=kinopoisk&retpath=https%3A%2F%2Fsso.passport.yandex.ru%2Fpush%3Fretpath%3Dhttps%253A%252F%252Fwww.kinopoisk.ru%252F%26uuid%3D8417c1ba-4e6f-4c76-8245-a8311802e466')    # noqa: E501
    #     self.driver.find_element(By.ID, 'data-type=login').send_keys(login, Keys.RETURN)
    #     self.driver.set_page_load_timeout(10)
    #     self.driver.find_element(By.ID, 'passp-field-passwd').send_keys(passwd, Keys.RETURN)

    def is_authorized(self):
        return WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid=header-user-button]"))
        ).is_displayed()
