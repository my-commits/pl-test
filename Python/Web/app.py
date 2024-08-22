from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    random_number = None
    min_value = 1
    max_value = 100

    if request.method == "POST":
        try:
            # Получаем значения диапазона от пользователя
            min_value = int(request.form.get("min_value", 1))
            max_value = int(request.form.get("max_value", 100))

            if min_value <= max_value:
                random_number = random.randint(min_value, max_value)
            else:
                random_number = "Ошибка: минимальное значение не может быть больше максимального!"
        except ValueError:
            random_number = "Ошибка: введите допустимые целые числа для диапазона!"

    return render_template("index.html", random_number=random_number, min_value=min_value, max_value=max_value)

if __name__ == "__main__":
    app.run(debug=True)
