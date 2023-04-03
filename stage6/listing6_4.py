""" Листинг 6.4 Исполнители пула процессов."""
import time
from concurrent.futures import ProcessPoolExecutor


def count(count_to: int) -> int:
    start = time.time()
    counter = 0
    while counter < count_to:
        counter += 1

    end = time.time()
    print(f"Закончен подсчёт до {count_to} за время {end - start}")
    return counter


if __name__ == "__main__":
    with ProcessPoolExecutor() as process_pool:
        numbers = [100000000, 1, 22, 5, 3, ]
        for result in process_pool.map(count, numbers):
            print(result)
