import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from class_ui import TestKinopoisk
from config import Config
from dotenv import load_dotenv
load_dotenv()


@pytest.fixture(scope='function')
def driver():
    options = webdriver.ChromeOptions()
    if Config.HEADLESS:
        options.add_argument('--headless')

    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager(
        ).install()))
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


ui=TestKinopoisk

@allure.suite("Кинопоиск UI")
@allure.epic("Кинопоиск онлайн UI")
@allure.title("Поиск фильма по названию")
def test_poisk():
    names = 'Побег из Шоушенка'
    ui.poisk_film(names)


@allure.suite("Кинопоиск UI")
@allure.epic("Кинопоиск онлайн UI")
@allure.title("Валидация поля поиска")
def test_input_name():
    ui.input_name("Kati")

@allure.suite("Кинопоиск UI")
@allure.epic("Кинопоиск онлайн UI")
@allure.title("Воспроизведение трейлера")
def test_play():
    ui.play_trailer()

@allure.suite("Кинопоиск UI")
@allure.epic("Кинопоиск онлайн UI")
@allure.title("Авторизация")
def test_auth():
    login = "milashkaersh"
    passwd = "3541"
    ui.avtorizacia(login, passwd)
