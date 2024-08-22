import random

def generate_random_number(min_value, max_value):
    return random.randint(min_value, max_value)

def main():
    while True:
        try:
            # Ввод диапазона чисел
            min_value = int(input("Введите минимальное значение диапазона: "))
            max_value = int(input("Введите максимальное значение диапазона: "))

            if min_value > max_value:
                print("Ошибка: минимальное значение не может быть больше максимального!")
                continue

            # Ожидание команды для генерации случайного числа
            input("Нажмите Enter для генерации случайного числа...")

            # Генерация и вывод случайного числа
            random_number = generate_random_number(min_value, max_value)
            print(f"Сгенерировано случайное число: {random_number}\n")

            # Повтор программы
            repeat = input("Хотите сгенерировать ещё одно число? (да/нет): ").lower()
            if repeat != 'да':
                break

        except ValueError:
            print("Ошибка: введите допустимые целые числа для диапазона!")

if __name__ == "__main__":
    main()
