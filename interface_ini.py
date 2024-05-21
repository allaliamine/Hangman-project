from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QPushButton, QGroupBox
from PySide6.QtGui import Qt

import Play_interface
import interface_Login
import interface_classement
import interface_settings


class InterfaceChoice(QMainWindow):
    def __init__(self, user_data):
        super().__init__()

        self.user_data = user_data
        self.setWindowTitle('Hangman choice Interface')
        self.setGeometry(100, 100, 800, 500)
        self.setStyleSheet("background-color: #1C1678;")

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Main layout for the central widget
        main_layout = QVBoxLayout(self.central_widget)
        main_layout.setAlignment(Qt.AlignCenter)

        # Group box to contain the dropdowns and buttons
        self.group_box = QGroupBox()
        self.group_box.setStyleSheet("font-size: 20px; background-color: white; border-radius: 10px;")
        self.group_box.setFixedSize(400, 300)  # Adjust size as needed

        group_box_layout = QVBoxLayout()
        group_box_layout.setAlignment(Qt.AlignCenter)

        # Create the play button
        self.play_button = QPushButton("Play")
        self.play_button.setStyleSheet(
            "background-color: black; color: white; font-size: 20px; border-radius: 10px; padding: 10px;")
        self.play_button.setFixedWidth(350)
        # execute action when hitting the button
        self.play_button.clicked.connect(self.play)

        # create the classement button
        self.classement_button = QPushButton("Classement")
        self.classement_button.setStyleSheet(
            "background-color: black; color: white; font-size: 20px; border-radius: 10px; padding: 10px;")
        self.classement_button.setFixedWidth(350)
        self.classement_button.clicked.connect(self.classement)

        # create the Settings button
        self.Settings_button = QPushButton("Settings")
        self.Settings_button.setStyleSheet(
            "background-color: black; color: white; font-size: 20px; border-radius: 10px; padding: 10px;")
        self.Settings_button.setFixedWidth(350)
        self.Settings_button.clicked.connect(self.settings)

        # exit button
        self.exit_button = QPushButton("Exit")
        self.exit_button.setStyleSheet(
            "background-color: red; color: white; font-size: 20px; border-radius: 10px; padding: 5px;")
        self.exit_button.setFixedWidth(350)
        self.exit_button.clicked.connect(self.exit)

        # Add widgets to the group box layout
        group_box_layout.addWidget(self.play_button)
        group_box_layout.addWidget(self.classement_button)
        group_box_layout.addWidget(self.Settings_button)
        group_box_layout.addWidget(self.exit_button)

        # Set the layout for the group box
        self.group_box.setLayout(group_box_layout)

        # Add the group box to the main layout
        main_layout.addWidget(self.group_box)

    def play(self):
        self.login_window = Play_interface.PlayInterface(user_data=self.user_data)
        self.login_window.show()
        self.close()

    def settings(self):

        self.login_window = interface_settings.ChangePasswordWindow(user_data=self.user_data)
        self.login_window.show()
        self.close()

    def exit(self):

        self.login_window = interface_Login.LoginWindow()
        self.login_window.show()
        self.close()

    def classement(self):
        self.login_window = interface_classement.ClassementtWindow(user_data=self.user_data)
        self.login_window.show()
        self.close()

