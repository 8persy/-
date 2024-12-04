import threading
from math import prod


def partial_factorial(start, end, result, thread_name):
    partial_result = prod(range(start, end + 1)) if start <= end else 1
    print(f"{thread_name}: Вычислено произведение от {start} до {end} = {partial_result}")
    result.append(partial_result)


def main():
    number = 10
    num_threads = 4
    threads = []
    results = []

    step = number // num_threads
    for i in range(num_threads):
        start = i * step + 1
        end = (i + 1) * step if i != num_threads - 1 else number
        thread_name = f"Thread-{i + 1}"
        thread_result = []
        thread = threading.Thread(target=partial_factorial, args=(start, end, thread_result, thread_name))
        threads.append(thread)
        results.append(thread_result)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    total_result = prod([result[0] for result in results])
    print(f"Факториал числа {number} = {total_result}")


main()
