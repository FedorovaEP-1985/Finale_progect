import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Основные настройки
    BASE_URL = "https://www.kinopoisk.ru/"
    API_URL = "https://api.kinopoisk.dev/v1.4"
    
    # Данные для авторизации
    LOGIN = os.getenv('KP_LOGIN', 'milashkaersh')
    PASSWORD = os.getenv('KP_PASSWORD', '3541')
    
    # API ключ
    API_KEY = os.getenv('KP_API_KEY', 'ZGYV669-58WM2EQ-G5DSZE7-M8Y2JV9')
    
    # Настройки cookies
    @staticmethod
    def get_cookies():
        cookie_string = os.getenv('COOKIE_STRING', '')
        if not cookie_string:
            return []
            
        cookies = []
        parts = cookie_string.split('.')
        if len(parts) >= 4:
            cookies.append({
                'name': 'session_cookie',
                'value': cookie_string,
                'path': '/',
                'domain': '.kinopoisk.ru'
            })
        return cookies
    HEADLESS = os.getenv('HEADLESS', 'false').lower() == 'true'
