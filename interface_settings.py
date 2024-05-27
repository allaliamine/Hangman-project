from PySide6.QtWidgets import *
from PySide6.QtCore import Qt

import conn
import interface_ini


class ChangePasswordWindow(QMainWindow):
    def __init__(self, user_data):
        super().__init__()

        self.user_data = user_data
        self.setWindowTitle("Change Password Interface")
        self.setGeometry(100, 100, 800, 500)
        self.setStyleSheet("background-color: #1C1678;")

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Main layout for the central widget
        main_layout = QVBoxLayout(self.central_widget)
        main_layout.setAlignment(Qt.AlignCenter)

        # Group box to contain the form elements
        self.group_box = QGroupBox()
        self.group_box.setStyleSheet("font-size: 20px; background-color: white; border-radius: 10px;")
        self.group_box.setFixedSize(400, 400)  # Adjust size as needed

        group_box_layout = QVBoxLayout()
        group_box_layout.setAlignment(Qt.AlignCenter)

        # Add title
        self.title = QLabel("Change Password")
        self.title.setStyleSheet("color: black; font-size: 30px;")
        self.title.setFixedHeight(60)
        self.title.setAlignment(Qt.AlignCenter)
        group_box_layout.addWidget(self.title)

        # Add new password label and input
        self.new_password_label = QLabel("New Password:")
        self.new_password_label.setStyleSheet("color: black; font-size: 20px; margin: 10px;")
        self.new_password_label.setFixedHeight(50)
        self.new_password_input = QLineEdit()
        self.new_password_input.setStyleSheet(
            "border-radius: 10px; padding: 5px; background-color: #E8E9EB; color: black")
        self.new_password_input.setFixedWidth(350)
        self.new_password_input.setFixedHeight(40)
        self.new_password_input.setEchoMode(QLineEdit.Password)
        group_box_layout.addWidget(self.new_password_label)
        group_box_layout.addWidget(self.new_password_input)

        # Add confirm password label and input
        self.confirm_password_label = QLabel("Confirm Password:")
        self.confirm_password_label.setStyleSheet("color: black; font-size: 20px; margin: 10px;")
        self.confirm_password_label.setFixedHeight(50)
        self.confirm_password_input = QLineEdit()
        self.confirm_password_input.setStyleSheet(
            "border-radius: 10px; padding: 5px; background-color: #E8E9EB; color: black")
        self.confirm_password_input.setFixedWidth(350)
        self.confirm_password_input.setFixedHeight(40)
        self.confirm_password_input.setEchoMode(QLineEdit.Password)
        group_box_layout.addWidget(self.confirm_password_label)
        group_box_layout.addWidget(self.confirm_password_input)

        # Add checkbox for hint enabled
        self.hint_enabled_checkbox = QCheckBox("Hint Enabled")
        self.hint_enabled_checkbox.setStyleSheet("color: black; font-size: 20px; margin: 10px;")
        self.hint_enabled_checkbox.setFixedHeight(50)
        group_box_layout.addWidget(self.hint_enabled_checkbox, alignment=Qt.AlignLeft)


        if self.user_data[1] == 1:
            self.hint_enabled_checkbox.setChecked(True)
        else:
            self.hint_enabled_checkbox.setChecked(False)

        # Add save button
        self.save_button = QPushButton("Save")
        self.save_button.setStyleSheet(
            "background-color: black; color: white; font-size: 20px; border-radius: 10px; padding: 10px;")
        self.save_button.setFixedWidth(350)
        self.save_button.clicked.connect(self.save_changes)
        group_box_layout.addWidget(self.save_button, alignment=Qt.AlignCenter)


        #retout button
        self.back_button = QPushButton("Go Back")
        self.back_button.setStyleSheet(
            "background-color: red; color: white; font-size: 20px; border-radius: 10px; padding: 5px;")
        self.back_button.setFixedWidth(350)
        self.back_button.clicked.connect(self.choice_interface)
        group_box_layout.addWidget(self.back_button, alignment=Qt.AlignCenter)


        # Set the layout for the group box
        self.group_box.setLayout(group_box_layout)

        # Add the group box to the main layout
        main_layout.addWidget(self.group_box)

    def save_changes(self):
        new_password = self.new_password_input.text()
        confirm_password = self.confirm_password_input.text()
        hint_enabled = 1 if self.hint_enabled_checkbox.isChecked() else 0

        # Check if the new password is empty
        if not new_password:
            # Only update the hint if the password is empty
            try:
                cur = conn.connection.cursor()
                sql2 = "UPDATE settings SET hintenabled = %s WHERE idaccount = %s"
                params2 = (hint_enabled, self.user_data[2])
                cur.execute(sql2, params2)
                conn.connection.commit()
                QMessageBox.information(self, "Success", "Hint updated successfully.")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"An error occurred: {e}")
            return

        # If the password is not empty, proceed with password validation and update
        if new_password != confirm_password:
            QMessageBox.warning(self, "Error", "Passwords do not match.")
            return

        try:
            cur = conn.connection.cursor()
            sql = "UPDATE account SET password = %s WHERE idaccount = %s"
            sql2 = "UPDATE settings SET hintenabled = %s WHERE idaccount = %s"
            params = (new_password, self.user_data[2])
            params2 = (hint_enabled, self.user_data[2])
            cur.execute(sql, params)
            cur.execute(sql2, params2)
            conn.connection.commit()
            QMessageBox.information(self, "Success", "Password and hint changed successfully.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred: {e}")

    def choice_interface(self):
        self.login_window = interface_ini.InterfaceChoice(user_data=self.user_data)
        self.login_window.show()
        self.close()