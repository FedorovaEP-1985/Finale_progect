import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from test_ui import driver


class TestKinopoisk():
    def __init__(self, driver):
            self.driver = driver
            self.driver.maximize_window()
            self.driver.implicitly_wait(20)


    @allure.step("Вводим имя {names}")
    def poisk_film(self, names: str):
        """
           Поиск фильма по названию.
           Можно указывать часть названия, если не помните полное.
           Поиск будет произведён и вам откроется список фильмов
           в которых будет присутствовать часть введённого названия.
        """
        poisk = self.driver.find_element(By.CSS_SELECTOR, 'input[name="kp_query"]')
        poisk.send_keys(names, Keys.RETURN)

    @allure.step("Проверка ввода в поисковую строку: '{text}'")
    def input_name(self, text: str):
        """
           Здесь мы проверяем отображение в поисковой строке ввод:
           букв, цифр, символов.
           Открываться cсылки и куда-то переходить мы не должны.
        """
        poi = self.driver.find_element(By.CSS_SELECTOR, 'input[name="kp_query"]')
        poi.send_keys(text)

    @allure.step("Запустить трейлер для просмотра")
    def play_trailer(self):
        self.driver.find_element(By.CSS_SELECTOR, '[class="pic"]').click()
        self.driver.find_element(By.CSS_SELECTOR, '[class="style_button__PNtXT styles_button__1_G0A styles_button_trailer__ORo93 style_buttonSize52__b5OBe style_buttonPrimary__ndPAb style_buttonDark__beFpy" name="Trailer" data-test-id="ContentActions_trailer">Трейлер</button>]').click()
        driver.quit()

    @allure.step("Авторизуемся")
    def avtorizacia(self, login: str, passwd: str):
        self.driver.get('https://passport.yandex.ru/auth/add/login?origin=kinopoisk&retpath=https%3A%2F%2Fsso.passport.yandex.ru%2Fpush%3Fretpath%3Dhttps%253A%252F%252Fwww.kinopoisk.ru%252F%26uuid%3D8417c1ba-4e6f-4c76-8245-a8311802e466')    # noqa: E501
        self.driver.find_element(By.ID, 'loginField').send_keys(login, Keys.RETURN)
        self.driver.set_page_load_timeout(10)
        self.driver.find_element(By.ID, 'passwordField').send_keys(passwd, Keys.RETURN)
        driver.quit()