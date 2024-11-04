import sys

from PyQt6.QtWidgets import QWidget, QApplication, QDialog

from layout import Ui_Dialog


class Zadanie(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.show()



if __name__ == '__main__' :
    app = QApplication(sys.argv)
    window = Zadanie()
    sys.exit(app.exec())