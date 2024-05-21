import sys
from PySide6.QtWidgets import QApplication
from interface_Login import *


def main():
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
