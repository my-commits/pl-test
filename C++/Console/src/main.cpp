#include <iostream>
#include <cstdlib>
#include <ctime>

int main() {
    std::setlocale(LC_ALL, "Russian");
    // Инициализация генератора случайных чисел
    std::srand(std::time(0));
    
    int minValue, maxValue;
    char choice;

    // Запрос диапазона от пользователя
    std::cout << "Введите минимальное значение диапазона: ";
    std::cin >> minValue;
    std::cout << "Введите максимальное значение диапазона: ";
    std::cin >> maxValue;

    do {
        // Генерация случайного числа в заданном диапазоне
        int randomNumber = minValue + std::rand() % (maxValue - minValue + 1);
        std::cout << "Сгенерированное число: " << randomNumber << std::endl;

        // Спрашиваем пользователя, хочет ли он сгенерировать еще одно число
        std::cout << "Хотите сгенерировать еще одно число? (y/n): ";
        std::cin >> choice;
    } while (choice == 'y' || choice == 'Y');

    std::cout << "Программа завершена." << std::endl;
    
    return 0;
}
