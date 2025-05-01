import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from class_ui import TestKinopoisk


@pytest.mark.usefixtures("driver")
@pytest.fixture()
def kp(driver):
    return TestKinopoisk(driver)

@allure.suite("Кинопоиск UI")
@allure.epic("Кинопоиск онлайн UI")
@allure.title("Поиск фильма по названию")
def test_poisk(kp):
    name = 'Три кота'
    kp.poisk_film(name)

@allure.suite("Кинопоиск UI")
@allure.epic("Кинопоиск онлайн UI")
@allure.title("Валидация поля поиска")
def test_input_name(kp):
    kp.input_name("Sloum")
    # Проверка введённого текста
    assert kp.get_search_text() == "Sloum", "Текст в поле не совпадает"

@allure.suite("Кинопоиск UI")
@allure.epic("Кинопоиск онлайн UI")
@allure.title("Воспроизведение трейлера")
def test_play(kp):
    kp.open_film_page("Три кота")  # Метод для открытия страницы фильма
    kp.play_trailer()


@allure.suite("Кинопоиск UI")
@allure.epic("Кинопоиск онлайн UI")
@allure.title("Авторизация")
@allure.title("Авторизация")
def test_auth(kp):
    kp.avtorizacia(login='milashkaersh', passwd='3541')
