from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QComboBox, QLabel, QPushButton, QMessageBox, QGroupBox
from PySide6.QtGui import Qt
import conn
import interface_ini


class PlayInterface(QMainWindow):
    def __init__(self, user_data):
        super().__init__()

        self.user_data = user_data
        self.setWindowTitle('Hangman Play Interface')
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

        # Create the difficulty level dropdown
        self.difficulty_label = QLabel("Select Difficulty:")
        self.difficulty_label.setStyleSheet("color: black;")
        self.difficulty_dropdown = QComboBox()
        self.difficulty_dropdown.setStyleSheet("background-color: black; color: white;")
        self.difficulty_dropdown.setFixedWidth(350)
        self.difficulty_dropdown.setFixedHeight(40)
        self.difficulty_dropdown.addItems(["easy", "medium", "hard"])

        # Create the topics dropdown
        self.topics_label = QLabel("Select Topic:")
        self.topics_label.setStyleSheet("color: black;")
        self.topics_dropdown = QComboBox()
        self.topics_dropdown.setStyleSheet("background-color: black; border-radius: 10px;")
        self.topics_dropdown.setFixedWidth(350)
        self.topics_dropdown.setFixedHeight(40)
        self.topics_dropdown.addItems(self.get_topics())

        # Create the play button
        self.play_button = QPushButton("Play")
        self.play_button.setStyleSheet(
            "background-color: black; color: white; font-size: 20px; border-radius: 10px; padding: 10px;")
        self.play_button.setFixedWidth(350)


        # create go back button
        self.back_button = QPushButton("Go Back")
        self.back_button.setStyleSheet(
            "background-color: red; color: white; font-size: 20px; border-radius: 10px; padding: 5px;")
        self.back_button.setFixedWidth(350)
        self.back_button.clicked.connect(self.choice_interface)

        # Add widgets to the group box layout
        group_box_layout.addWidget(self.difficulty_label)
        group_box_layout.addWidget(self.difficulty_dropdown)
        group_box_layout.addWidget(self.topics_label)
        group_box_layout.addWidget(self.topics_dropdown)
        group_box_layout.addWidget(self.play_button)
        group_box_layout.addWidget(self.back_button)

        # Set the layout for the group box
        self.group_box.setLayout(group_box_layout)

        # Add the group box to the main layout
        main_layout.addWidget(self.group_box)

    def get_topics(self):
        # Assuming conn provides a function to get topics from the database
        try:
            cur = conn.connection.cursor()
            cur.execute("SELECT * FROM topic")
            result = cur.fetchall()
            topics = [row[1] for row in result]
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred: {e}")
            topics = []

        return topics

    def choice_interface(self):
        self.login_window = interface_ini.InterfaceChoice(user_data=self.user_data)
        self.login_window.show()
        self.close()