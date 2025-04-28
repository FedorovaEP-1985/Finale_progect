import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from class_ui import TestKinopoisk
from dotenv import load_dotenv
load_dotenv()


driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager
                          ().install()))
driver.get('https://www.kinopoisk.ru')
ui = TestKinopoisk(driver)


@allure.suite("Кинопоиск UI")
@allure.epic("Кинопоиск онлайн UI")
@allure.title("Поиск фильма по названию")
def test_poisk():
    names = 'Побег из Шоушенка'
    ui.poisk_film(names)
    driver.quit()


@allure.suite("Кинопоиск UI")
@allure.epic("Кинопоиск онлайн UI")
@allure.title("Валидация поля поиска")
def test_input_name():
    ui.input_name("Kati")
    driver.quit()

@allure.suite("Кинопоиск UI")
@allure.epic("Кинопоиск онлайн UI")
@allure.title("Воспроизведение трейлера")
def test_play():
    ui.play_trailer()
    driver.quit()

@allure.suite("Кинопоиск UI")
@allure.epic("Кинопоиск онлайн UI")
@allure.title("Авторизация")
def test_auth():
    login = "milashkaersh"
    passwd = "3541"
    ui.avtorizacia(login, passwd)
    driver.quit()
