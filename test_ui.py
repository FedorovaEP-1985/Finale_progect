import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from class_ui import testKinopoisk
from dotenv import load_dotenv
load_dotenv()


driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager
                          ().install()))
driver.get('https://www.kinopoisk.ru')
ui = testKinopoisk(driver)

@allure.suite("Кинопоиск UI")
@allure.epic("Кинопоиск онлайн UI")
@allure.title("Поиск фильма по названию")
def test_poisk():
    names = 'Блейд'
    ui.poisk_film(names)


@allure.suite("Кинопоиск UI")
@allure.epic("Кинопоиск онлайн UI")
@allure.title("Валидация поля поиска")
def test_search_validation():
    ui.input_name("Kati")


@allure.suite("Кинопоиск UI")
@allure.epic("Кинопоиск онлайн UI")
@allure.title("Воспроизведение трейлера")
def test_play():
    ui.play_trayler()


@allure.suite("Кинопоиск UI")
@allure.epic("Кинопоиск онлайн UI")
@allure.title("Авторизация")
def test_auth():
        login = "milashkaersh"
        passwd = "3541"
        ui.avtorizacia(login, passwd)
