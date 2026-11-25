# модуль для измерения времени
import time

import requests

from config import CHECK_URL, CHECKER_TIMEOUT


# Функция принимает строку с прокси в формате IP:PORT.
# Возвращает либо кортеж (IP-адрес, время ответа), либо None.
def check_proxy(proxy_string: str) -> tuple[str, float] | None:

    # Добавляем протокол SOCKS5 к адресу прокси.
    socks = f"socks5://{proxy_string}"

    # Создаём словарь настроек прокси.
    proxies_dict = {
        "http": socks,
        "https": socks,
    }

    try:

        # Запоминаем показание таймера перед выполнением запроса.
        start_time = time.perf_counter()

        # Отправляем GET-запрос через проверяемую прокси.
        response = requests.get(
            CHECK_URL,                  # Адрес проверочного сервера
            timeout=CHECKER_TIMEOUT,
            proxies=proxies_dict        # Настройки используемой прокси
        )

        # Проверяем HTTP-статус ответа.
        response.raise_for_status()

        # Таким образом получаем продолжительность запроса.
        elapsed_time = time.perf_counter() - start_time

        # Возвращаем кортеж из двух элементов:
        # ('27.112.79.97', 2.365) - example
        print(response.text.strip(), round(elapsed_time, 3))
        return response.text.strip(), round(elapsed_time, 3)

    # Перехватываем исключения библиотеки requests
    except requests.exceptions.RequestException:
        return None