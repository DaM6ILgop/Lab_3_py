import sys
import re
import os
from datetime import datetime

from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QLabel, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Поиск строк в файле")
        self.resize(800, 600)

        self.results = []
        self.log_filename = "script18.log"

        self.create_menu()
        self.create_statusbar()
        self.create_central_widget()

    def create_menu(self):
        menu_bar = self.menuBar()

        file_menu = menu_bar.addMenu("Файл")
        open_action = file_menu.addAction("Открыть...")
        open_action.triggered.connect(self.open_file)

        log_menu = menu_bar.addMenu("Лог")
        export_action = log_menu.addAction("Экспорт...")
        export_action.triggered.connect(self.export_results)
        add_to_log_action = log_menu.addAction("Добавить в лог")
        add_to_log_action.triggered.connect(self.add_to_log)
        view_log_action = log_menu.addAction("Просмотр")
        view_log_action.triggered.connect(self.view_log)

    def create_statusbar(self):
        self.statusbar = self.statusBar()
        self.statusbar.showMessage("")

    def create_central_widget(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

    def open_file(self):
        try:
            file_dialog = QFileDialog()
            file_path, _ = file_dialog.getOpenFileName(self, "Открыть файл", "", "Текстовые файлы (*.txt)")

            if file_path:
                self.process_file(file_path)
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Ошибка при открытии файла: {str(e)}")

    def process_file(self, file_path):
        try:
            with open(file_path, 'r') as file:
                text = file.read()

            pattern = r'[A-Z]:\\(?:[^\/:?"<>|\r\n]+\\)+[^\/:*?"<>|\r\n]+'
            matches = re.findall(pattern, text)

            datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.results.extend(matches)

            self.show_results()

            self.statusbar.showMessage(f"Обработан файл {file_path}", 10000)
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Ошибка при обработке файла: {str(e)}")

    def show_results(self):
        try:
            self.clear_results()

            for i, result in enumerate(self.results):
                result_label = QLabel(result)
                self.centralWidget().layout().addWidget(result_label)
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Ошибка при отображении результатов: {str(e)}")

    def clear_results(self):
        layout = self.centralWidget().layout()
        if layout:
            while layout.count():
                child = layout.takeAt(0)
                if child.widget():
                    child.widget().deleteLater()

    def export_results(self):
        if not self.results:
            return

        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getSaveFileName(self, "Экспорт результатов", "", "Текстовые файлы (*.txt)")

        if file_path:
            with open(file_path, 'w') as file:
                file.write("\n".join(self.results))

    def add_to_log(self):
        if not self.results:
            return

        with open(self.log_filename, 'a') as file:
            file.write("\n".join(self.results))

    def view_log(self):
        if self.results:
            reply = QMessageBox.question(self, "Просмотр лога", "Вы действительно хотите открыть лог? Данные последних поисков будут потеряны!",
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.No:
                return

        if not os.path.exists(self.log_filename):
            QMessageBox.information(self, "Файл лога не найден", "Файл лога не найден. Файл будет создан автоматически.", QMessageBox.Ok)
        else:
            with open(self.log_filename, 'r') as file:
                self.results = file.read().splitlines()

                self.show_results()

                self.statusbar.showMessage("Открыт лог")



app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()