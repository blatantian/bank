import random

class Bank:
    def __init__(self):
        self.users = {}

    def luhn_algorithm(self, card_number):
        def luhn_digit(n):
            n *= 2
            return n - 9 if n > 9 else n

        digits = [int(x) for x in str(card_number)]
        odd_digits = digits[-1::-2]
        even_digits = digits[-2::-2]
        total = sum(odd_digits + list(map(luhn_digit, even_digits)))
        return (10 - (total % 10)) % 10

    def create_card_number(self):
        while True:
            card_number = "400000" + ''.join([str(random.randint(0, 9)) for _ in range(10)])
            check_digit = self.luhn_algorithm(card_number)
            card_number += str(check_digit)
            
            if card_number not in self.users:
                return card_number

    def register_user(self):
        card_number = self.create_card_number()
        pin_code = input("Введите Pin-code: ")
        balance = 0

        self.users[card_number] = {"pin_code": pin_code, "balance": balance}
        print(f"Пользователь зарегистрирован. Номер карты: {card_number}")

    def login_user(self):
        card_number = input("Введите номер карты: ")
        pin_code = input("Введите Pin-code: ")

        if card_number in self.users and self.users[card_number]["pin_code"] == pin_code:
            print("Вход выполнен успешно.")
            return card_number
        else:
            print("Неверный номер карты или Pin-code.")
            return None

    def menu(self, card_number):
        while True:
            print("\nМеню:")
            print("1. Просмотр баланса")
            print("2. Добавить средства")
            print("3. Снять средства")
            print("4. Выйти")
            
            choice = input("Выберите действие: ")

            if choice == "1":
                print(f"Баланс: {self.users[card_number]['balance']}")

            elif choice == "2":
                amount = float(input("Введите сумму для пополнения: "))
                self.users[card_number]['balance'] += amount
                print("Средства добавлены успешно.")

            elif choice == "3":
                amount = float(input("Введите сумму для снятия: "))
                if amount > self.users[card_number]['balance']:
                    print("Недостаточно средств.")
                else:
                    self.users[card_number]['balance'] -= amount
                    print("Средства сняты успешно.")

            elif choice == "4":
                break

if __name__ == "__main__":
    bank = Bank()

    while True:
        print("\nПомойка")
        print("1. Регистрация")
        print("2. Вход")
        print("3. Выход")

        action = input("Выберите действие: ")

        if action == "1":
            bank.register_user()

        elif action == "2":
            card_number = bank.login_user()
            if card_number:
                bank.menu(card_number)

        elif action == "3":
            break

        else:
            print("Неверный выбор. Попробуйте еще раз.")
