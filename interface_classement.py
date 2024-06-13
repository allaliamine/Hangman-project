import sys
from PySide6.QtWidgets import *
from PySide6.QtGui import QPixmap, QFont, QColor
from PySide6.QtCore import Qt
import conn
import interface_ini


class ClassementtWindow(QMainWindow):
    def __init__(self, user_data):
        super().__init__()

        self.user_data = user_data
        self.setWindowTitle("Game Leaderboard")
        self.setGeometry(100, 100, 800, 500)
        self.setStyleSheet("background-color:#1C1678")

        # Create a QLabel for the top title "Leaderboard"
        self.title_label = QLabel("Leaderboard", self)
        self.title_label.setFont(QFont("Arial", 24, QFont.Bold))
        self.title_label.setStyleSheet("color: #EEF7FF")
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.setGeometry(200, 10, 400, 50)

        # Create a QTableWidget to display the leaderboard
        self.leaderboard_table = QTableWidget(self)
        self.leaderboard_table.setGeometry(50, 80, 500, 200)
        self.leaderboard_table.setColumnCount(3)
        self.leaderboard_table.setHorizontalHeaderLabels(["Player ID", "UserName", "Score"])


        # Style the header
        header = self.leaderboard_table.horizontalHeader()
        header.setFont(QFont("Arial", 12, QFont.Bold))
        header.setStyleSheet("color: #003285; background-color: #3333A3;")
        header.setDefaultAlignment(Qt.AlignCenter)

        # Style the rows
        self.leaderboard_table.setStyleSheet(
            "QTableWidget::item { color: #EEF7FF; }"
            "QTableWidget::item:selected { background-color: #4C4CB3; }"
            "QHeaderView::section { background-color: #3333A3; color: #EEF7FF; }"
        )
        self.leaderboard_table.setAlternatingRowColors(True)
        self.leaderboard_table.setStyleSheet("alternate-background-color: #2C2C99; background-color: #1C1678;")

        # Disable editing
        self.leaderboard_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.leaderboard_table.setSelectionBehavior(QTableWidget.SelectRows)

        # Create the go back button
        self.back_button = QPushButton("Go Back")
        self.back_button.setStyleSheet(
            "background-color: red; color: white; font-size: 20px; border-radius: 10px; padding: 5px;"
        )
        self.back_button.setFixedWidth(300)
        self.back_button.clicked.connect(self.choice_interface)

        # Set up the layout
        layout = QVBoxLayout()
        layout.addWidget(self.title_label)
        layout.addWidget(self.leaderboard_table)
        layout.addWidget(self.back_button, alignment=Qt.AlignCenter)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Populate the table with data from the database
        self.load_leaderboard_data()

    def load_leaderboard_data(self):
        cur = conn.connection.cursor()
        sql = "SELECT l.idaccount, a.name, l.score FROM laderboard l JOIN account a ON l.idaccount = a.idaccount ORDER BY score DESC"
        cur.execute(sql)
        res = cur.fetchall()

        self.leaderboard_table.setRowCount(len(res))

        for row_num, row_data in enumerate(res):
            self.leaderboard_table.setItem(row_num, 0, QTableWidgetItem(str(row_data[0])))
            self.leaderboard_table.setItem(row_num, 1, QTableWidgetItem(row_data[1]))
            self.leaderboard_table.setItem(row_num, 2, QTableWidgetItem(str(row_data[2])))

        self.leaderboard_table.setColumnWidth(0, 220)
        self.leaderboard_table.setColumnWidth(1, 220)
        self.leaderboard_table.setColumnWidth(2, 200)

    def choice_interface(self):
        self.login_window = interface_ini.InterfaceChoice(user_data=self.user_data)
        self.login_window.show()
        self.close()

