import requests
import allure


BASE_URL = "https://www.kinopoisk.ru/"
API_URL = "https://api.kinopoisk.dev/v1.4/"
SEARCH_QUERY = "Побег из Шоушенка"
MOVIE_TITLE = "Побег из Шоушенка"
MOVIE_YEAR = "1994"
INVALID_SEARCH_QUERY = "12345"

 # API
API_KEY = "ZGYV669-58WM2EQ-G5DSZE7-M8Y2JV9"
MOVIE_ID = 326
PERSON_NAME = "2286874"



@allure.title("Получение информации о фильме")
def test_get_movie_info():
    url = f"{API_URL}movie/{MOVIE_ID}"
    headers = {"X-API-KEY": API_KEY}

    response = requests.get(url, headers=headers)
    assert response.status_code == 200
    assert response.json()["id"] == MOVIE_ID

@allure.title("Проверка неверного API ключа")
def test_invalid_api_key():
    url = f"{API_URL}movie/{MOVIE_ID}"
    headers = {"X-API-KEY": "invalid_key"}

    response = requests.get(url, headers=headers)
    assert response.status_code == 401

@allure.title("Получение списка топ фильмов")
def test_get_top_movies():
    url = f"{API_URL}movie"
    params = {"top": "TOP_250_BEST_FILMS"}
    headers = {"X-API-KEY": API_KEY}
    response = requests.get(url, params=params, headers=headers)
    assert response.status_code == 200
    assert len(response.json()["docs"]) > 0

@allure.title("Поиск несуществующего фильма")
def test_search_nonexistent_movie():
    url = f"{API_URL}movie/search?page=1&limit=10&query={INVALID_SEARCH_QUERY}"
    headers = {"X-API-KEY": API_KEY}
    response = requests.get(url, headers=headers)
    assert response.status_code == 200


@allure.title("Получение информации о персонаже")
def test_get_person_info():
    url = f"{API_URL}person"
    params = {"id": PERSON_NAME}
    headers = {"X-API-KEY": API_KEY}
    response = requests.get(url, params=params, headers=headers)
    assert response.status_code == 200
    assert response.json()['docs'][0]['name'] == 'Александр Петров'