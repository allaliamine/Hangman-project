import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QLabel, QFrame
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
from interface_Login import *
import conn 
from interface import *


class WelcomeWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Main Widget and Layout
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QHBoxLayout(main_widget)
        self.setGeometry(100, 100, 800, 500)
        self.setWindowTitle("Hangman")

        # Set the background image
        self.background_label = QLabel(self)
        pixmap = QPixmap("images/photo1.png")  # Provide the correct path to your background image
        self.background_label.setPixmap(pixmap)
        self.background_label.setGeometry(0, 0, 800, 500)
        self.background_label.setScaledContents(True)
        self.background_label.lower()

        
        welcome_title = QLabel("Hangman-Game")
        welcome_title.setAlignment(Qt.AlignCenter)
        welcome_title.setStyleSheet("font-size: 25px; color: black; background-color : none ;")


        # Create buttons
        Sign_button = QPushButton("Sign up ")
        login_button = QPushButton("Log in ")

        # Set maximum width for buttons
        Sign_button.setMaximumWidth(350) 
        login_button.setMaximumWidth(350) 

        # Create a QVBoxLayout for the buttons
        
        button_layout = QVBoxLayout()
        button_layout.addWidget(welcome_title)
        button_layout.addWidget(Sign_button)
        button_layout.addWidget(login_button)
        button_layout.setAlignment(Qt.AlignCenter)  
        button_layout.setSpacing(10)  

        # Create a QFrame to act as the box with a background color
        button_frame = QFrame()
        button_frame.setLayout(button_layout)
        button_frame.setStyleSheet("background-color: rgba(255, 255, 255, 200); border-radius: 10px;")
        button_frame.setFixedWidth(400)
        button_frame.setFixedHeight(200)

        # Create a main layout to center the button_frame
        main_layout.addWidget(button_frame)
        main_layout.setAlignment(Qt.AlignCenter)

        # Set button styles
        Sign_button.setStyleSheet(
            "background-color: #1C1678 ; color: white; border-radius: 10px; font-size: 20px; padding: 10px; height: 27px; width: 300px;")
        login_button.setStyleSheet(
        
            "background-color:#1C1678; color: white; border-radius: 10px; padding: 10px; font-size: 20px; height: 27px;")

        Sign_button.clicked.connect(self.sign_up)
        login_button.clicked.connect(self.login)

    def  sign_up(self) :
        self.Sing_up_Window = SingupWindow()
        self.Sing_up_Window.show()

          
    def login(self):
        self.login_window = LoginWindow()
        self.login_window.show()
   



app = QApplication(sys.argv)
window = WelcomeWindow() 
window.show()
sys.exit(app.exec())
