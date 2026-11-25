# библиотека для выполнения HTTP-запросов
import requests 

from config import PROXY_LIST_URL

def get_proxies():

    try:

        # Отправляем GET-запрос по указанному URL.
        response = requests.get(PROXY_LIST_URL,timeout=15)

        # Проверяем HTTP-статус ответа.
        # Если сервер вернул ошибку - вызовет исключение HTTPError
        response.raise_for_status()

        # response.text — текстовое содержимое ответа сервера, 
        # разбивая текст на список отдельных строк
        print (response.text.splitlines())

        # Возвращаем список прокси вызывающему коду.
        return response.text.splitlines()

    # Перехватываем большинство обычных исключений Python.
    except Exception:
        # поднимаем ошибку выше - откуда вызвали
        raise