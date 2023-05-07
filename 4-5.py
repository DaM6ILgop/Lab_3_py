import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton, QLabel, QCheckBox, QMessageBox



class StringFormatter:
    @staticmethod
    def replace_digits_with_asterisk(string):
        return ''.join('*' if char.isdigit() else char for char in string)



    @staticmethod
    def insert_spaces(string):
        return ' '.join(string)



    @staticmethod
    def sort_words(string):
        words = string.split()
        sorted_words = sorted(words, key=lambda word: (len(word), word))
        return ' '.join(sorted_words)



    @staticmethod
    def remove_words_less_than_n(string, n):
        words = string.split()
        filtered_words = [word for word in words if len(word) >= n]
        return ' '.join(filtered_words)



class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Окно с текстовым полем")
        self.setGeometry(700, 400, 500, 300)

        # Создание подписи для текстового поля
        self.label = QLabel("Текстовое поле:", self)
        self.label.setGeometry(20, 20, 100, 30)

        # Создание текстового поля
        self.text_entry = QLineEdit(self)
        self.text_entry.setGeometry(130, 20, 350, 30)

        # Создание чекбоксов и меток
        self.checkbox1 = QCheckBox("Удалить слова размером меньше", self)
        self.checkbox1.setGeometry(20, 70, 350, 30)
        self.label2 = QLabel("n букв:", self)
        self.label2.setGeometry(20, 100, 60, 30)

        # Создание текстового поля для удаления слова размером n
        self.text_N_word = QLineEdit(self)
        self.text_N_word.setGeometry(70, 100, 40, 30)

        self.checkbox2 = QCheckBox("Заменить все цифры на *", self)
        self.checkbox2.setGeometry(20, 130, 350, 30)
        self.checkbox3 = QCheckBox("Вставить по пробелу между символами", self)
        self.checkbox3.setGeometry(20, 160, 350, 30)
        self.checkbox4 = QCheckBox("Сортировать слова в строке", self)
        self.checkbox4.setGeometry(20, 190, 350, 30)

        # Установка обработчиков событий для чекбоксов
        self.checkbox1.stateChanged.connect(self.handle_checkbox1)
        self.checkbox2.stateChanged.connect(self.handle_checkbox2)
        self.checkbox3.stateChanged.connect(self.handle_checkbox3)
        self.checkbox4.stateChanged.connect(self.handle_checkbox4)

        # Создание кнопки для обнуления текстовых полей
        self.button = QPushButton("Сбросить", self)
        self.button.setGeometry(20, 230, 100, 30)
        # Вызов сброса значений чекбоксов
        self.button.clicked.connect(self.false_checkboxes)



    def handle_checkbox1(self, state):
        if state == 2:  # Проверка, что чекбокс включен (True)
            n_text = self.text_N_word.text()  # Получение текста из поля длины слова
            if not n_text:  # Проверка, что поле длины слова не пустое
                QMessageBox.warning(self, "Внимание", "Поле длины слова пусто")
                return

            n = int(n_text)  # Получение числа минимальной длины слова из текстового поля
            text = self.text_entry.text()  # Получение текста из текстового поля
            formatted_text = StringFormatter.remove_words_less_than_n(text, n)  # Форматирование текста
            self.text_entry.setText(formatted_text)  # Установка отформатированного текста обратно в текстовое поле



    def handle_checkbox2(self, state):
        if state == 2:  # Проверка, что чекбокс включен (True)
            self.original_text = self.text_entry.text()  # Сохранение оригинального значения текста
            text = self.original_text
            formatted_text = StringFormatter.replace_digits_with_asterisk(text)  # Форматирование текста
            self.text_entry.setText(formatted_text)  # Установка отформатированного текста обратно в текстовое поле
        else:  # Если чекбокс выключен (False)
            if hasattr(self, 'original_text'):  # Проверка, что сохранено оригинальное значение текста
                self.text_entry.setText(self.original_text)  # Восстановление оригинального значения текста
                del self.original_text  # Удаление сохраненного оригинального значения



    def handle_checkbox3(self, state):
        if state == 2:  # Проверка, что чекбокс включен (True)
            self.original_text = self.text_entry.text()  # Сохранение оригинального значения текста
            text = self.original_text
            formatted_text = StringFormatter.insert_spaces(text)  # Форматирование текста
            self.text_entry.setText(formatted_text)  # Установка отформатированного текста обратно в текстовое поле
        else:  # Если чекбокс выключен (False)
            if hasattr(self, 'original_text'):  # Проверка, что сохранено оригинальное значение текста
                self.text_entry.setText(self.original_text)  # Восстановление оригинального значения текста
                del self.original_text  # Удаление сохраненного оригинального значения



    def handle_checkbox4(self, state):
        if state == 2:  # Проверка, что чекбокс включен (True)
            self.original_text_checkbox4 = self.text_entry.text()  # Сохранение оригинального значения текста для checkbox4
            text = self.original_text_checkbox4
            formatted_text = StringFormatter.sort_words(text)  # Форматирование текста
            self.text_entry.setText(formatted_text)  # Установка отформатированного текста обратно в текстовое поле
        else:  # Если чекбокс выключен (False)
            if hasattr(self,
                       'original_text_checkbox4'):  # Проверка, что сохранено оригинальное значение текста для checkbox4
                self.text_entry.setText(
                    self.original_text_checkbox4)  # Восстановление оригинального значения текста для checkbox4
                del self.original_text_checkbox4  # Удаление сохраненного оригинального значения для checkbox4



    def false_checkboxes(self):
        self.checkbox1.setChecked(False)
        self.checkbox2.setChecked(False)
        self.checkbox3.setChecked(False)
        self.checkbox4.setChecked(False)



app = QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec())