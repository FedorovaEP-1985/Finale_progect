import requests
import allure
from config import Config
from test_data import TestData
from dotenv import load_dotenv
load_dotenv()


@allure.title("Получение информации о фильме")
def test_get_movie_info():
    url = f"{Config.API_URL}movie/{TestData.MOVIE_ID}"
    headers = {"X-API-KEY": Config.API_KEY}

    response = requests.get(
        url, headers=headers)
    assert response.status_code == 200
    assert response.json()["id"] == TestData.MOVIE_ID

@allure.title("Проверка неверного API ключа")
def test_invalid_api_key():
    url = f"{Config.API_URL}movie/{TestData.MOVIE_ID}"
    headers = {"X-API-KEY": "invalid_key"}

    response = requests.get(
        url, headers=headers)
    assert response.status_code == 401

@allure.title("Получение списка топ фильмов")
def test_get_top_movies():
    url = f"{Config.API_URL}movie"
    params = {"top": "TOP_250_BEST_FILMS"}
    headers = {"X-API-KEY": Config.API_KEY}
    response = requests.get(
        url, params=params, headers=headers)
    assert response.status_code == 200
    assert len(response.json()["docs"]) > 0

@allure.title("Поиск несуществующего фильма")
def test_search_nonexistent_movie():
    url = (f"{Config.API_URL}"
           f"movie/search?page=1&limit=10&query"
           f"={TestData.INVALID_SEARCH_QUERY}")
    headers = {"X-API-KEY": Config.API_KEY}
    response = requests.get(url, headers=headers)
    assert response.status_code == 200


@allure.title("Получение информации о персонаже")
def test_get_person_info():
    url = f"{Config.API_URL}person"
    params = {"id": TestData.PERSON_NAME}
    headers = {"X-API-KEY": Config.API_KEY}
    response = requests.get(url, params=params, headers=headers)
    assert response.status_code == 200
    assert (response.json()['docs'][0]['name']
            == 'Александр Петров')
