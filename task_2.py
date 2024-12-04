import threading
import time


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def find_primes_in_range(start, end, result, thread_name):
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    print(f"{thread_name}: Найдено {len(primes)} простых чисел")
    result.extend(primes)


def main():
    start_range = 1
    end_range = 1000
    num_threads = 4
    threads = []
    results = []

    step = (end_range - start_range + 1) // num_threads

    for i in range(num_threads):
        start = start_range + i * step
        end = start + step - 1 if i != num_threads - 1 else end_range
        thread_name = f"Thread-{i + 1}"
        thread_result = []
        thread = threading.Thread(target=find_primes_in_range, args=(start, end, thread_result, thread_name))
        threads.append(thread)
        results.append(thread_result)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    all_primes = []
    for result in results:
        all_primes.extend(result)

    print(f"Все простые числа в диапазоне от {start_range} до {end_range}:")
    print(sorted(all_primes), '\n',  len(all_primes))


t1 = time.time()
main()
t2 = time.time()

print(t2 - t1)
