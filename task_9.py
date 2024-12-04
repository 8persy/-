import threading
import math


def calculate_factorial(n, results, key):
    try:
        if n < 0:
            raise ValueError("Факториал определен только для неотрицательных чисел.")
        results[key] = math.factorial(n)
    except Exception as e:
        results[key] = f"Ошибка при вычислении факториала: {e}"


def calculate_power(base, exponent, results, key):
    try:
        res = 1
        for i in range(exponent):
            res *= base
        results[key] = res
    except Exception as e:
        results[key] = f"Ошибка при возведении в степень: {e}"


def calculate_integration(func, a, b, results, key, n=1000):
    try:
        if a >= b:
            raise ValueError("Левая граница должна быть меньше правой.")
        h = (b - a) / n
        result = 0.5 * (func(a) + func(b))
        for i in range(1, n):
            result += func(a + i * h)
        results[key] = result * h
    except Exception as e:
        results[key] = f"Ошибка при интеграции: {e}"


def main():
    results = {}

    threads = [
        threading.Thread(target=calculate_factorial, args=(5, results, "Факториал")),
        threading.Thread(target=calculate_power, args=(2, 10, results, "Возведение в степень")),
        threading.Thread(target=calculate_integration, args=(math.sin, 0, math.pi, results, "Интеграция"))
    ]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    for task, result in results.items():
        print(f"{task}: {result}")


main()
