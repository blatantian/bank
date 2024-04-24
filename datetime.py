from datetime import datetime, timedelta

def add_time(start_time, duration, day=None):
    try:
        # Преобразование времени начала в формат datetime
        start_time = datetime.strptime(start_time, '%I:%M %p')
        
        # Преобразование временного отрезка в timedelta
        hours, minutes = map(int, duration.split(':'))
        duration = timedelta(hours=hours, minutes=minutes)
        
        # Сложение времени начала и временного отрезка
        end_time = start_time + duration
        
        # Добавление дня недели, если передан
        if day:
            days = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']
            day_index = days.index(day.lower())
            end_time += timedelta(days=day_index)
        
        # Форматирование и вывод результата
        end_time_str = end_time.strftime('%I:%M %p')
        
        # Определение дня недели и добавление информации о дне
        day_str = ''
        if day:
            day_str = end_time.strftime('%A')
            days_diff = (end_time.date() - start_time.date()).days
            if days_diff == 0:
                day_str += f', {day.capitalize()}'
            elif days_diff == 1:
                day_str = f'{day_str}, следующий день'
            else:
                day_str = f'{day_str}, {days_diff} дня(ей) позже'
        
        return f'{end_time_str}, {day_str}' if day else end_time_str
    except Exception as e:
        return f"Ошибка: {e}"

# Запрос входных данных у пользователя
start_time = input("Введите начальное время (например, 3:00 PM): ")
duration = input("Введите временной отрезок (например, 3:10): ")
day = input("Введите день недели (опционально): ")

# Вызов функции и вывод результата
result = add_time(start_time, duration, day)
print(result)
