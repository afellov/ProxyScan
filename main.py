from concurrent.futures import ThreadPoolExecutor, as_completed

from config import MAX_WORKERS
from services.proxy_loader import get_proxies
from services.proxy_checker import check_proxy


def main():
    proxies = get_proxies()

    # Проверяем, что список не пустой
    if not proxies:
        print("Список прокси пуст")
        return

    # Получаем первую прокси из списка
    proxy = proxies[0]

    print(f"Проверяем прокси: {proxy}")


    # Передаём прокси в нашу функцию
    result = check_proxy(proxy)


    for proxy in proxies:
        print(check_proxy(proxy))


    # if not proxies:
    #     print("Не удалось загрузить список прокси")
    #     return

    # print(f"Загружено прокси: {len(proxies)}")

    # working_proxies = []

    # with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:

    #     futures = {
    #         executor.submit(check_proxy, proxy): proxy
    #         for proxy in proxies
    #     }

    #     for future in as_completed(futures):
    #         proxy = futures[future]
    #         result = future.result()

    #         if result is not None:
    #             ip, elapsed_time = result

    #             working_proxies.append(proxy)

    #             print(
    #                 f"[OK] {proxy} | "
    #                 f"IP: {ip} | "
    #                 f"Время: {elapsed_time} сек."
    #             )

    #         else:
    #             print(f"[FAIL] {proxy}")

    # print(f"\nВсего проверено: {len(proxies)}")
    # print(f"Рабочих прокси: {len(working_proxies)}")


if __name__ == "__main__":
    main()