import sys
from PyQt5.QtWidgets import QApplication, QDialog, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt
from server.db.DB_manager import DBmanager
from client.api.User_api import get_login_user
base_manager = DBmanager("D:/PythonProjects/src/banda.db")


class RegistrationForm(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Registration Form')
        self.login_label = QLabel('Login:')
        self.login_input = QLineEdit()
        self.password_label = QLabel('Password:')
        self.password_input = QLineEdit()
        self.register_button = QPushButton('Register')
        layout = QVBoxLayout()
        layout.addWidget(self.login_label)
        layout.addWidget(self.login_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.register_button)
        self.setLayout(layout)
        self.register_button.clicked.connect(self.register)

    def register(self):
        login = self.login_input.text()
        password = self.password_input.text()
        if login and password:
            res = get_login_user(login, password)
            if not res:
                base_manager.execute("INSERT INTO user (login, password) VALUES (?, ?)", args=(login, password))
                print("Пользователь зарегистрирован успешно!")
            else:
                print("Пользователь с таким логином уже существует.")
        else:
            print("Введите логин и пароль")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = RegistrationForm()
    form.setWindowFlag(Qt.WindowCloseButtonHint)
    form.show()
    sys.exit(app.exec_())
