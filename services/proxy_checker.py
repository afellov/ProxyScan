# Проверка работоспособности и скорости

import requests

from config import CHECK_URL, CHECKER_TIMEOUT

def check_proxy(proxy_string: str) -> str | None :

    # обрабатываем ошибки сети (если будут)

    try:
        socks = f"socks5://{proxy_string}"

        proxies_dict = {
            "http": socks,
            "https": socks,
        }

        # пытаемся получить ответ с сервера
        response = requests.get(CHECK_URL, timeout=CHECKER_TIMEOUT, proxies=proxies_dict)

        response.raise_for_status()
            
        return response.text
    
    # обрабатывааем ошибки, не связанные с сетью
    except requests.exceptions.RequestException as e:
        print(e)
        return None
