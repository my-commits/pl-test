import tkinter as tk
from tkinter import messagebox
import random

def generate_random_number():
    try:
        min_value = int(min_entry.get())
        max_value = int(max_entry.get())
        
        if min_value > max_value:
            messagebox.showerror("Ошибка", "Минимальное значение не может быть больше максимального!")
        else:
            random_number = random.randint(min_value, max_value)
            result_label.config(text=f"Случайное число: {random_number}")
    except ValueError:
        messagebox.showerror("Ошибка", "Введите корректные целые числа!")

# Создание главного окна
root = tk.Tk()
root.title("Генератор случайных чисел")

# Создание элементов интерфейса
min_label = tk.Label(root, text="Минимум:")
min_label.pack()

min_entry = tk.Entry(root)
min_entry.pack()
min_entry.insert(0, "1")  # Устанавливаем начальное значение

max_label = tk.Label(root, text="Максимум:")
max_label.pack()

max_entry = tk.Entry(root)
max_entry.pack()
max_entry.insert(0, "100")  # Устанавливаем начальное значение

generate_button = tk.Button(root, text="Сгенерировать", command=generate_random_number)
generate_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

# Запуск главного цикла программы
root.mainloop()
