import sys
from PySide6.QtWidgets import QApplication

from inetrface_0 import WelcomeWindow
from interface_Login import *


def main():
    app = QApplication(sys.argv)
    window = WelcomeWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
