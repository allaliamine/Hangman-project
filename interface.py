import sys
from PySide6.QtWidgets import *
from PySide6.QtGui import QPixmap
import conn
import inetrface_0
import interface_Login


class SingupWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Main Widget and Layout
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QHBoxLayout(main_widget)
        self.setGeometry(100, 100, 800, 500)
        self.setWindowTitle("Sign In")

        # Set the background image
        self.background_label = QLabel(self)
        pixmap = QPixmap("images/bg_image.jpeg")  # Provide the correct path to your background image
        self.background_label.setPixmap(pixmap)
        self.background_label.setGeometry(0, 0, 800, 500)
        self.background_label.setScaledContents(True)
        self.background_label.lower()

        # Create a vertical layout for the form
        form_layout = QVBoxLayout()
        form_layout.setContentsMargins(2, 2, 10, 10)

        # Function to add widget with label
        def add_widget_with_label(layout, widget, label_text,color):
            vbox = QVBoxLayout()
            label = QLabel(label_text)
            label.setStyleSheet("color: {};".format(color))
            vbox.addWidget(label)
            vbox.addWidget(widget)
            layout.addLayout(vbox)

        # Create username and password input fields
        self.name_input = QLineEdit()
        self.username_input = QLineEdit()
        self.password_input = QLineEdit()
        self.confirm_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        self.confirm_input.setEchoMode(QLineEdit.Password)

        # Set width of input fields
        self.username_input.setFixedWidth(350)
        self.password_input.setFixedWidth(350)
        self.name_input.setFixedWidth(350)
        self.confirm_input.setFixedWidth(350)

        input_style = "background-color: #E8E9EB; color: black; font-size: 20px; border-radius:10px; padding: 10px;"
        self.name_input.setStyleSheet(input_style)
        self.username_input.setStyleSheet(input_style)
        self.password_input.setStyleSheet(input_style)
        self.confirm_input.setStyleSheet(input_style)

        # Add the input fields with labels to the form layout
        add_widget_with_label(form_layout, self.name_input, "Name:", "black")
        add_widget_with_label(form_layout, self.username_input, "Username:", "black")
        add_widget_with_label(form_layout, self.password_input, "Password:", "black")
        add_widget_with_label(form_layout, self.confirm_input, "Confirm Password:", "black")

        # Add a submit button
        submit_button = QPushButton("Sign In")
        submit_button.setMaximumWidth(350)  # Set width of the button
        form_layout.addWidget(submit_button)

        submit_button.setStyleSheet(
            "background-color: black; color: white ; border-radius:10px; padding: 10px ; height : 20px;")

        # Connect the button to a function (e.g., for processing the sign-in)
        submit_button.clicked.connect(self.sign_up)

        # Add the exit button
        self.exit_button = QPushButton("Exit")
        self.exit_button.setStyleSheet(
            "background-color: red; color: white; font-size: 20px; border-radius: 10px; padding: 5px;"
        )
        self.exit_button.setFixedWidth(350)
        self.exit_button.clicked.connect(self.exit)

        # Add the exit button under the submit button
        form_layout.addWidget(self.exit_button)

        # Add a spacer item to push the form layout to the right
        main_layout.addSpacerItem(QSpacerItem(30, 10, QSizePolicy.Expanding, QSizePolicy.Minimum))
        main_layout.addLayout(form_layout)

    def sign_up(self):
        name = self.name_input.text()
        username = self.username_input.text()
        password = self.password_input.text()
        confirm = self.confirm_input.text()

        if confirm == password:
            try:
                cur = conn.connection.cursor()

                # Check if the username already exists
                sql0 = "SELECT * FROM account WHERE username = %s"
                params0 = (username,)
                cur.execute(sql0, params0)
                isExist = cur.fetchall()

                if isExist:
                    QMessageBox.information(self, "Username",
                                            "Username already exists, please provide another username")
                    return

                # inert the new account
                sql = "INSERT INTO account (username, password, name, role) VALUES (%s, %s, %s, %s)"
                params = (username, password, name, 1)
                cur.execute(sql, params)
                conn.connection.commit()

                # Retrieve the new account's ID
                sql2 = "SELECT idaccount FROM account WHERE username = %s AND password = %s"
                params2 = (username, password)
                cur.execute(sql2, params2)
                res = cur.fetchone()  # Use fetchone() as only one result is expected

                if res:
                    value = int(res[0])
                    # QMessageBox.information(self, "Account success", f"Account ID: {value}!")

                    # Insert into settings
                    sql3 = "INSERT INTO settings (idaccount, hintenabled) VALUES (%s, %s)"
                    insert_params = (value, 1)
                    cur.execute(sql3, insert_params)
                    conn.connection.commit()

                    QMessageBox.information(self, "Account success",
                                            f"Your account is successfully created, {name}!")
                    self.go_to_login()
                else:
                    QMessageBox.critical(self, "Error", "Failed to retrieve the new account ID.")

            except Exception as e:
                conn.connection.rollback()  # Rollback transaction on error
                QMessageBox.critical(self, "Error", f"An error occurred: {e}")
        else:
            QMessageBox.critical(self, "Error", "Your passwords do not match.")

    def go_to_login(self):
        self.login_window = interface_Login.LoginWindow()
        self.login_window.show()
        self.close()

    def exit(self):
        self.login_window = inetrface_0.WelcomeWindow()
        self.login_window.show()
        self.close()

# # Run the application
# app = QApplication(sys.argv)
# window = SingupWindow()
# window.show()
# sys.exit(app.exec())