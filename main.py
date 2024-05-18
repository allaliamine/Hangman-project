import sys
from PySide6.QtWidgets import QApplication
from interface import *

def main():
    app = QApplication(sys.argv)
    window = SingupWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
