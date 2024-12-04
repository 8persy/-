import threading
import time
import random


class ParkingLot:
    def __init__(self, capacity):
        self.capacity = capacity
        self.lock = threading.Lock()
        self.available_spaces = capacity

    def park_car(self, car_id):
        with self.lock:
            if self.available_spaces > 0:
                self.available_spaces -= 1
                print(f"Автомобиль {car_id} припаркован. Свободных мест: {self.available_spaces}/{self.capacity}")
                return True
            else:
                print(f"Автомобиль {car_id} не смог припарковаться. Нет свободных мест.")
                return False

    def leave_car(self, car_id):
        with self.lock:
            self.available_spaces += 1
            print(f"Автомобиль {car_id} уехал. Свободных мест: {self.available_spaces}/{self.capacity}")


def car_behavior(parking_lot, car_id):
    parked = parking_lot.park_car(car_id)
    if parked:
        parking_time = random.randint(1, 5)
        time.sleep(parking_time)
        parking_lot.leave_car(car_id)


def simulate_parking_lot(capacity, num_cars):
    parking_lot = ParkingLot(capacity)

    threads = []
    for car_id in range(1, num_cars + 1):
        arrival_time = random.uniform(0.1, 3.0)
        time.sleep(arrival_time)

        thread = threading.Thread(target=car_behavior, args=(parking_lot, car_id))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("Симуляция завершена.")


simulate_parking_lot(capacity=5, num_cars=10)
