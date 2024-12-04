import threading
from math import factorial


def fibonacci(n):
    if n <= 1:
        return n
    a = 1
    b = 1
    for i in range(n):
        a = b
        b = b + a
    return b


def compute_function(nums, results, thread_name, func):
    thread_results = {}
    for num in nums:
        thread_results[num] = func(num)
        print(f"{thread_name}: {func.__name__}({num}) = {thread_results[num]}")
    results.append(thread_results)


def main():
    print("Выберите функцию для вычисления:")
    print("1. Факториал")
    print("2. Числа Фибоначчи")
    choice = int(input("Введите номер функции (1 или 2): "))

    func = factorial if choice == 1 else fibonacci

    numbers = list(map(int, input("Введите числа через пробел: ").split()))

    num_threads = int(input("Введите количество потоков: "))

    threads = []
    results = []
    step = len(numbers) // num_threads
    for i in range(num_threads):
        start = i * step
        end = (i + 1) * step if i != num_threads - 1 else len(numbers)
        thread_name = f"Thread-{i + 1}"
        thread = threading.Thread(
            target=compute_function,
            args=(numbers[start:end], results, thread_name, func),
        )
        threads.append(thread)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    final_results = {}
    for result in results:
        final_results.update(result)

    print("\nИтоги вычислений:")
    for num, res in sorted(final_results.items()):
        print(f"{func.__name__}({num}) = {res}")


main()
