import random
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup

class RandomNumberGeneratorApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Поля ввода для минимального и максимального значений
        self.min_input = TextInput(text='1', multiline=False, hint_text="Минимум", input_filter='int')
        self.max_input = TextInput(text='100', multiline=False, hint_text="Максимум", input_filter='int')

        # Кнопка для генерации случайного числа
        self.generate_button = Button(text="Сгенерировать", size_hint=(1, 0.3))
        self.generate_button.bind(on_press=self.generate_random_number)

        # Метка для отображения результата
        self.result_label = Label(text="Случайное число будет здесь", font_size='20sp')

        # Добавляем элементы на экран
        self.layout.add_widget(self.min_input)
        self.layout.add_widget(self.max_input)
        self.layout.add_widget(self.generate_button)
        self.layout.add_widget(self.result_label)

        return self.layout

    def generate_random_number(self, instance):
        try:
            # Получение минимального и максимального значений
            min_value = int(self.min_input.text)
            max_value = int(self.max_input.text)

            if min_value > max_value:
                self.show_error("Минимальное значение не может быть больше максимального!")
            else:
                random_number = random.randint(min_value, max_value)
                self.result_label.text = f"Случайное число: {random_number}"
        except ValueError:
            self.show_error("Введите корректные целые числа!")

    def show_error(self, message):
        popup = Popup(title='Ошибка', content=Label(text=message), size_hint=(0.8, 0.4))
        popup.open()

# Запуск приложения
if __name__ == '__main__':
    RandomNumberGeneratorApp().run()
