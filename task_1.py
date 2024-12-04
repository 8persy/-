import threading
import time


def thread_task():
    thread_name = threading.current_thread().name
    print(f"Поток {thread_name} выполняется")
    time.sleep(1)  # Симуляция работы потока
    print(f"Поток {thread_name} завершён")


threads = []

for i in range(5):
    thread = threading.Thread(target=thread_task, name=f"Thread-{i+1}")
    threads.append(thread)

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

print("Все потоки завершены")
