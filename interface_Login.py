import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, \
    QMessageBox, QGroupBox
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt

import conn


class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Login")
        self.setGeometry(100, 100, 800, 500)

        # Add central widget
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Main layout
        main_layout = QVBoxLayout(self.central_widget)

        # Add background label
        self.background_label = QLabel(self)
        pixmap = QPixmap("./bg_image.jpeg")  # Provide the path to your background image
        self.background_label.setPixmap(pixmap)
        self.background_label.setGeometry(0, 0, 800, 500)
        self.background_label.setScaledContents(True)
        self.background_label.lower()

        # Create a group box for the login form
        self.group_box = QGroupBox("Login")
        self.group_box.setStyleSheet("font-size: 20px; background-color: white; border-radius: 10px;")
        group_box_layout = QVBoxLayout()

        #add title
        title_layout = QVBoxLayout()
        self.title = QLabel("Sign in")
        self.title.setStyleSheet("color: black; font-size: 30px;")
        self.title.setFixedHeight(60)
        title_layout.addWidget(self.title)


        # Add username label and input
        username_layout = QVBoxLayout()
        self.username_label = QLabel("Username:")
        self.username_label.setStyleSheet("color: black; font-size: 20px; margin: 10px;")
        self.username_label.setFixedHeight(50)
        self.username_input = QLineEdit()
        self.username_input.setStyleSheet("border-radius: 10px; padding: 5px; background-color: #E8E9EB; color: black")
        self.username_input.setFixedWidth(350)
        self.username_input.setFixedHeight(40)
        username_layout.addWidget(self.username_label)
        username_layout.addWidget(self.username_input)

        # Add password label and input
        password_layout = QVBoxLayout()
        self.password_label = QLabel("Password:")
        self.password_label.setStyleSheet("color: black; font-size: 20px; margin: 10px;")
        self.password_label.setFixedHeight(50)
        self.password_input = QLineEdit()
        self.password_input.setStyleSheet("border-radius: 10px; padding: 5px; background-color: #E8E9EB; color: black")
        self.password_input.setFixedWidth(350)
        self.password_input.setFixedHeight(40)
        self.password_input.setEchoMode(QLineEdit.Password)
        password_layout.addWidget(self.password_label)
        password_layout.addWidget(self.password_input)

        # Add login button
        self.login_button = QPushButton("Login")
        self.login_button.setStyleSheet("background-color: black; color: white; font-size: 20px; border-radius: 10px; padding: 10px;")
        self.login_button.setFixedWidth(350)
        self.login_button.clicked.connect(self.login)

        # Add layouts to group box layout
        group_box_layout.addLayout(title_layout)
        group_box_layout.addLayout(username_layout)
        group_box_layout.addLayout(password_layout)
        group_box_layout.addWidget(self.login_button, alignment=Qt.AlignRight)

        self.group_box.setLayout(group_box_layout)
        main_layout.addWidget(self.group_box, alignment=Qt.AlignRight)

    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()
        try:
            cur = conn.connection.cursor()
            sql = "SELECT * FROM account WHERE username = %s AND password = %s"
            params = (username, password)
            cur.execute(sql, params)
            res = cur.fetchall()

            if res:
                QMessageBox.information(self, "Login Successful", f"Welcome, {username}!")
            else:
                QMessageBox.warning(self, "Login Failed", "Incorrect username or password.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred: {e}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_window = LoginWindow()
    login_window.show()
    sys.exit(app.exec())
