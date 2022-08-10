# For developping
from ui_builder import qtui_to_py
qtui_to_py('qt_ui/MainWindow.ui', 'main_window')

import os
import sys

from PyQt5.QtWidgets import QMainWindow, QApplication


from main_window import Ui_MainWindow


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()

        self.ui.setupUi(self)
        self.setFixedSize(self.size())


if __name__ == '__main__':


    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
