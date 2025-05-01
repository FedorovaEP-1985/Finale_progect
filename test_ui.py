# import allure
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager
# from class_ui import TestKinopoisk
# from config import Config
# from dotenv import load_dotenv
# load_dotenv()
#
# driver = webdriver.Chrome(
#         service=ChromeService(ChromeDriverManager(
#         ).install()))
# driver.maximize_window()
# driver.implicitly_wait(10)
# driver.get("https://www.kinopoisk.ru/")
# ui=TestKinopoisk
#
# @allure.suite("Кинопоиск UI")
# @allure.epic("Кинопоиск онлайн UI")
# @allure.title("Поиск фильма по названию")
# def test_poisk():
#     names = 'Три кота'
#     ui.poisk_film(names)
#
#
# @allure.suite("Кинопоиск UI")
# @allure.epic("Кинопоиск онлайн UI")
# @allure.title("Валидация поля поиска")
# def test_input_name():
#     ui.input_name("Sloum")
#
# @allure.suite("Кинопоиск UI")
# @allure.epic("Кинопоиск онлайн UI")
# @allure.title("Воспроизведение трейлера")
# def test_play():
#     ui.play_trailer()
#
# @allure.suite("Кинопоиск UI")
# @allure.epic("Кинопоиск онлайн UI")
# @allure.title("Авторизация")
# def test_auth():
#     login = "milashkaersh"
#     passwd = "3541"
#     ui.avtorizacia(login, passwd)

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from class_ui import TestKinopoisk


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@pytest.fixture()
def kp(driver):
    return TestKinopoisk(driver)

@allure.suite("Кинопоиск UI")
@allure.epic("Кинопоиск онлайн UI")
@allure.title("Поиск фильма по названию")
def test_poisk(kp):
    names = 'Три кота'
    kp.poisk_film(names)
    # Проверка наличия результатов поиска
    assert kp.is_results_found(), "Фильмы не найдены"

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
    kp.is_trailer_playing()


@allure.suite("Кинопоиск UI")
@allure.epic("Кинопоиск онлайн UI")
@allure.title("Авторизация")
def test_auth(kp):
    login = "milashkaersh"
    passwd = "3541"
    kp.avtorizacia(login, passwd)
    # Проверка успешной авторизации
    assert kp.is_authorized(), "Авторизация не удалась"

def test_open_film_page(kp):
    kp.open_film_page()
