import pytest
import requests
from config import Config
from test_data import TestData
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def movie_data():
    return {
        "id": TestData.MOVIE_ID,
        "title": TestData.MOVIE_TITLE,
        "year": TestData.MOVIE_YEAR
    }

@pytest.fixture
def api_headers():
    return {"X-API-KEY": Config.API_KEY}

@pytest.fixture()
def driver():
    options = webdriver.ChromeOptions()
    if Config.HEADLESS:
        options.add_argument('--headless')

    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager(
        ).install()))
    driver.maximize_window()
    driver.implicitly_wait(15)
    yield driver
    driver.quit()

    @pytest.fixture
    def api_url():
        return requests.Session()  # или ваша базовая URL