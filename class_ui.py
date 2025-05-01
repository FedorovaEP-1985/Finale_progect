import allure
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys


class TestKinopoisk:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://www.kinopoisk.ru/")

    @allure.step("Поиск фильма: {name}")
    def poisk_film(self, name):
        """
                 Поиск фильма по названию.
                 Можно указывать часть названия, если не помните полное.
                 Поиск будет произведён и вам откроется список фильмов
                в которых будет присутствовать часть введённого названия.
            """
        search_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[name="kp_query"]'))
        )
        search_input.send_keys(name + Keys.RETURN)


    @allure.step("Ввод текста в поисковую строку")
    def input_name(self, text):
        """
            Здесь мы проверяем отображение в поисковой строке ввод:
            букв, цифр, символов.
            Открываться cсылки и куда-то переходить мы не должны.
        """
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
        try:
            # Ожидаем загрузки страницы фильма
            WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='film-details-page']"))
            )

            # Кликаем на кнопку "Трейлер"
            WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='trailer-button']"))
            ).click()

            # Проверяем, что плеер трейлера появился
            WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".trailer-player iframe"))
            )

        except TimeoutException as e:
            allure.attach(
                self.driver.get_screenshot_as_png(),
                name="trailer_timeout",
                attachment_type=allure.attachment_type.PNG
            )
            pytest.fail(f"Трейлер не запустился: {str(e)}")

    @allure.step("Запустить трейлер для просмотра")
    def play_trailers(self):
        self.driver.find_element(By.CSS_SELECTOR, '[class="pic"]').click()
        self.driver.find_element(By.CSS_SELECTOR, '[class="style_button__PNtXT styles_button__1_G0A styles_button_trailer__ORo93 style_buttonSize52__b5OBe style_buttonPrimary__ndPAb style_buttonDark__beFpy" name="Trailer" data-test-id="ContentActions_trailer">Трейлер</button>]').click()

    @allure.step("Авторизуемся")
    def avtorizacia(self, login: str, passwd: str):
        self.driver.get(
            'https://passport.yandex.ru/auth/add/login?origin=kinopoisk&retpath=https%3A%2F%2Fsso.passport.yandex.ru%2Fpush%3Fretpath%3Dhttps%253A%252F%252Fwww.kinopoisk.ru%252F%26uuid%3D8417c1ba-4e6f-4c76-8245-a8311802e466')  # noqa: E501
        self.driver.find_element(By.CSS_SELECTOR, 'input[data-t="field:input-login"]').send_keys(login,
                                                                                                  Keys.RETURN)
        self.driver.set_page_load_timeout(10)
        self.driver.find_element(By.CSS_SELECTOR, 'input[data-t="field:input-passwd"]').send_keys(passwd,
                                                                                                   Keys.RETURN)
