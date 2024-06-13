from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QMessageBox, QHBoxLayout
from PySide6.QtGui import QPixmap
import Play_interface
import conn
import interface_ini


class HangmanGameInterface(QWidget):
    def __init__(self, word, hints, user_data):
        super().__init__()

        self.wrong_guesses = set()
        upper_word = word.upper()
        self.word = list(upper_word)
        self.hints = hints
        self.user_data = user_data
        self.guessed_letters = set()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Hangman Play Interface')
        self.setGeometry(100, 100, 800, 500)
        self.setStyleSheet("background-color: #1C1678;")

        # Create GUI elements
        self.letters_layout = QVBoxLayout()

        cadre_widget = QWidget()
        cadre_layout = QVBoxLayout(cadre_widget)
        self.hangman_image_label = QLabel()

        pixmap = QPixmap("images/h1.png")
        self.hangman_image_label.setPixmap(pixmap)
        self.hangman_image_label.setAlignment(Qt.AlignCenter)
        cadre_layout.addWidget(self.hangman_image_label)

        self.word_label = QLabel("_ " * len(self.word))
        self.word_label.setAlignment(Qt.AlignCenter)
        cadre_layout.addWidget(self.word_label)

        # Create the hint button
        self.hint_button = QPushButton("Hint")
        self.hint_button.setStyleSheet("background-color: #4CAF50; color: white; font-size: 16px;")
        self.hint_button.clicked.connect(self.show_hint)
        cadre_layout.addWidget(self.hint_button)

        if self.is_hint_enabled():
            self.hint_button.show()
        else:
            self.hint_button.hide()

        # Create layout for rows of buttons
        letters_widget = QWidget()
        letters_layout = QVBoxLayout(letters_widget)
        letters_layout.setAlignment(Qt.AlignCenter)

        # Create letter buttons
        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        buttons = []
        for letter in letters:
            button = QPushButton(letter)
            button.setFixedWidth(40)
            button.setStyleSheet("background-color: black; color: white;")
            button.clicked.connect(lambda _, l=letter, b=button: self.guess_letter(l, b))
            buttons.append(button)

        # Divide buttons into rows
        rows = [buttons[i:i + 10] for i in range(0, len(buttons), 10)]

        # Add buttons
        for row in rows:
            row_layout = QHBoxLayout()
            for button in row:
                row_layout.addWidget(button)
            letters_layout.addLayout(row_layout)

        # Add widgets to layouts
        self.letters_layout.addWidget(cadre_widget)
        self.letters_layout.addWidget(letters_widget)

        # Set main layout
        self.setLayout(self.letters_layout)

    def guess_letter(self, letter, button):
        # print(self.user_data[2])

        if letter in self.guessed_letters or letter in self.wrong_guesses:
            return

        button.setEnabled(False)
        button.setText("")

        if letter in self.word:
            self.guessed_letters.add(letter)
        else:
            self.wrong_guesses.add(letter)

        # Update GUI elements based on guessed letter
        self.update_word_display()
        self.update_hangman_image()

        # Check win/lose condition
        if self.check_win_condition():
            self.handle_win()
        elif len(self.wrong_guesses) >= 6:
            self.handle_lose()

    def update_word_display(self):
        displayed_word = ""
        for char in self.word:
            if char in self.guessed_letters:
                displayed_word += char
            else:
                displayed_word += "_ "
        self.word_label.setText(displayed_word.strip())

    def update_hangman_image(self):
        num_wrong_guesses = len(self.wrong_guesses)
        if num_wrong_guesses == 0:
            return

        image_path = f"images/h{num_wrong_guesses + 1}.png"
        pixmap = QPixmap(image_path)
        self.hangman_image_label.setPixmap(pixmap)

    def check_win_condition(self):
        return all(char in self.guessed_letters for char in self.word)

    def handle_win(self):
        self.update_score()
        msgBox = QMessageBox()
        msgBox.setText("Congratulations !")
        msgBox.setInformativeText("You win! Do you want to play again?'")
        msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msgBox.setDefaultButton(QMessageBox.Yes)
        ret = msgBox.exec()
        if ret == QMessageBox.Yes:
            self.play_interface()
        else:
            self.choice_interface()

    def handle_lose(self):
        msgBox = QMessageBox()
        msgBox.setText("Game Over!")
        msgBox.setInformativeText('You have lost. Do you want to play again?')
        msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msgBox.setDefaultButton(QMessageBox.Yes)
        ret = msgBox.exec()

        if ret == QMessageBox.Yes:
            self.play_interface()
        else:
            self.choice_interface()

    def show_hint(self):
        if self.hints:
            hint_text = "".join(self.hints)  # Convert the list of hints to a single string
            QMessageBox.information(self, "Hint", hint_text)
        else:
            QMessageBox.warning(self, "No Hint", "Sorry, no hints available for this word.")

    def play_interface(self):
        self.login_window = Play_interface.PlayInterface(user_data=self.user_data)
        self.login_window.show()
        self.close()

    def choice_interface(self):
        self.login_window = interface_ini.InterfaceChoice(user_data=self.user_data)
        self.login_window.show()
        self.close()

    def update_score(self):
        cur = conn.connection.cursor()

        # Get the score for the user
        getScore = "SELECT score FROM laderboard WHERE idaccount = %s"
        cur.execute(getScore, (self.user_data[2],))
        scoreValue = cur.fetchone()
        # QMessageBox.warning(self, "out", f"{scoreValue}")

        if scoreValue:
            score = scoreValue[0] + 1  # Increment the score
            # QMessageBox.warning(self, "out", f"{score}")
            setScore = "UPDATE laderboard SET score = %s WHERE idaccount = %s"
            cur.execute(setScore, (score, self.user_data[2]))
            conn.connection.commit()
        else:
            insertScore = "INSERT INTO laderboard (idaccount, score) VALUES (%s, %s)"
            cur.execute(insertScore, (self.user_data[2], 1))
            conn.connection.commit()

    def is_hint_enabled(self):
        cur = conn.connection.cursor()
        sql = "SELECT hintenabled FROM settings WHERE idaccount = %s"
        cur.execute(sql, (self.user_data[2],))
        res = cur.fetchone()

        if res and res[0] == 1:
            return True
        else:
            return False