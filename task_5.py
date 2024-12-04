import threading
import time
from heapq import merge


def sort_subarray(subarray, results, thread_name):
    print(f"{thread_name}: Сортировка подмассива {subarray}")
    sorted_subarray = sorted(subarray)
    results.append(sorted_subarray)
    print(f"{thread_name}: Результат сортировки {sorted_subarray}")


def main():
    numbers = [38, 27, 43, 3, 9, 82, 10, 45, 15, 72, 20, 99]
    print(f"Исходный массив: {numbers}")

    num_threads = int(input("Введите количество потоков: "))
    t1 = time.time()

    step = len(numbers) // num_threads
    subarrays = [
        numbers[i * step: (i + 1) * step] if i != num_threads - 1 else numbers[i * step:]
        for i in range(num_threads)
    ]

    threads = []
    results = []

    for i, subarray in enumerate(subarrays):
        thread_name = f"Thread-{i + 1}"
        thread = threading.Thread(target=sort_subarray, args=(subarray, results, thread_name))
        threads.append(thread)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print(f"Отсортированные части: {results}")
    sorted_array = list(merge(*results))
    print(f"Итоговый отсортированный массив: {sorted_array}")
    t2 = time.time()
    print(t2 - t1)


main()
