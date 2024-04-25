BANKBANKBANKBANKBANKBANKBANKBANKBANKBANKBANKBANKBANKBANKBANKBANKBANKBANKBANKBANKBANKBANKBANKBANKBANKBANKBANKBANKBANKBANKBANKBANKBANKBANKBANKBANKBANKBANKBANKBANK
import random

class Bank:
    def __init__(self): # Здесь создается атрибут users, который будет словарем для хранения информации о пользователях. 
        self.users = {} # Ключом будет номер карты, а значением словарь с пин-кодом и балансом пользователя.

    def luhn_algorithm(self, card_number): # реализация алгоритма луна
        def luhn_digit(n): # внутр функция которая преобразует 1 цифру по алгоритму
            n *= 2
            return n - 9 if n > 9 else n

        digits = [int(x) for x in str(card_number)] # преобразует номер карты в список цифр
        odd_digits = digits[-1::-2] # Эти две строки разделяют цифры номера карты на нечетные и четные позиции
        even_digits = digits[-2::-2]
        total = sum(odd_digits + list(map(luhn_digit, even_digits))) # вычисляется общая сумма всех цифр после применения алгоритма Луна к четным позициям
        return (10 - (total % 10)) % 10 # вычисляет контрольную цифру по алгоритму Луна

    def create_card_number(self): # генерация номера карты
        while True: # создается номер карты, начинающийся с префикса "400000", за которым следуют 10 случайных цифр.
            card_number = "400000" + ''.join([str(random.randint(0, 9)) for _ in range(10)])
            check_digit = self.luhn_algorithm(card_number) # Добавляется контрольная цифра к сгенерированному номеру карты
            card_number += str(check_digit)
            
            if card_number not in self.users: # Проверяется, не зарегистрирован ли уже такой номер карты. Если нет, номер возвращается
                return card_number

    def register_user(self): # регистрация пользователя в системе банка
        card_number = self.create_card_number() # Генерируется номер карты, запрашивается пин-код и устанавливается начальный баланс пользователя.
        pin_code = input("Введите Pin-code: ")
        balance = 0

        self.users[card_number] = {"pin_code": pin_code, "balance": balance} # Информация о пользователе добавляется в словарь users, и выводится сообщение о успешной регистрации.
        print(f"Пользователь зарегистрирован. Номер карты: {card_number}")

    def login_user(self): # вход в систему
        card_number = input("Введите номер карты: ")
        pin_code = input("Введите Pin-code: ")

        if card_number in self.users and self.users[card_number]["pin_code"] == pin_code: # Проверяется, существует ли такой пользователь и совпадает ли введенный пин-код с сохраненным в системе
            print("Вход выполнен успешно.")
            return card_number
        else:
            print("Неверный номер карты или Pin-code.")
            return None

    def menu(self, card_number): # отображение меню
        while True: # беск. цикл для отображения меню
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

if __name__ == "__main__": # Эта строка проверяет, запущен ли скрипт напрямую, а не импортирован как модуль
    bank = Bank() # создание экземп класса банк

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

DATETIMEDATETIMEDATETIMEDATETIMEDATETIMEDATETIMEDATETIMEDATETIMEDATETIMEDATETIMEDATETIMEDATETIMEDATETIMEDATETIMEDATETIMEDATETIMEDATETIMEDATETIMEDATETIMEDATETIMEDATETIMEDATETIMEDATETIMEDATETIME

from datetime import datetime, timedelta

def add_time(start_time, duration, day=None): #  объявление функции add_time, которая принимает три аргумента: start_time (начальное время), duration (продолжительность времени) и опциональный аргумент day (день недели).
    try:
        # Преобразование времени начала в формат datetime
        start_time = datetime.strptime(start_time, '%I:%M %p') # Преобразует start_time из строки в объект datetime с помощью метода strptime, используя заданный формат времени.
        
        # Преобразование временного отрезка в timedelta
        hours, minutes = map(int, duration.split(':')) # Разбивает duration на часы и минуты, преобразует их в целые числа и
        duration = timedelta(hours=hours, minutes=minutes) # создаёт объект timedelta для представления продолжительности времени.
        
        # Сложение времени начала и временного отрезка
        end_time = start_time + duration # Добавляет продолжительность времени duration к start_time для получения end_time.
        
        # Добавление дня недели, если передан
        if day: # Если передан day, добавляет соответствующее количество дней к end_time.
            days = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']
            day_index = days.index(day.lower())
            end_time += timedelta(days=day_index)
        
        # Форматирование и вывод результата
        end_time_str = end_time.strftime('%I:%M %p') # Преобразует end_time обратно в строку с заданным форматом времени.
        
        # Определение дня недели и добавление информации о дне
        day_str = '' # Определяет день недели и добавляет информацию о дне к day_str.
        if day:
            day_str = end_time.strftime('%A')
            days_diff = (end_time.date() - start_time.date()).days
            if days_diff == 0:
                day_str += f', {day.capitalize()}'
            elif days_diff == 1:
                day_str = f'{day_str}, следующий день'
            else:
                day_str = f'{day_str}, {days_diff} дня(ей) позже'
        
        return f'{end_time_str}, {day_str}' if day else end_time_str # Возвращает end_time_str и day_str в форматированном виде, если указан day, иначе только end_time_str
    except Exception as e: # Обрабатывает исключения, возвращая сообщение об ошибке
        return f"Ошибка: {e}"

# Запрос входных данных у пользователя
start_time = input("Введите начальное время (например, 3:00 PM): ")
duration = input("Введите временной отрезок (например, 3:10): ")
day = input("Введите день недели (опционально): ")

# Вызов функции и вывод результата
result = add_time(start_time, duration, day)
print(result)
