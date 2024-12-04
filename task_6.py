import threading
import time
import random


class BankAccount:
    def __init__(self, balance):
        self.balance = balance
        self.lock = threading.Lock()

    def withdraw(self, amount, client_name):
        with self.lock:
            print(f"{client_name} пытается снять {amount}...")
            if self.balance >= amount:
                time.sleep(random.uniform(0.1, 0.5))
                self.balance -= amount
                print(f"{client_name} успешно снял {amount}. Остаток: {self.balance}")
            else:
                print(f"{client_name} не может снять {amount}. Недостаточно средств! Остаток: {self.balance}")


def atm_client(account, client_name):
    amount = random.randint(1, 10000)
    account.withdraw(amount, client_name)


def main():
    initial_balance = 10000
    account = BankAccount(initial_balance)

    clients = []
    num_clients = 5
    for i in range(num_clients):
        client_name = f"Клиент-{i + 1}"
        client_thread = threading.Thread(target=atm_client, args=(account, client_name))
        clients.append(client_thread)

    for client in clients:
        client.start()

    for client in clients:
        client.join()

    print(f"\nВсе операции завершены. Итоговый остаток на счёте: {account.balance}")


main()
