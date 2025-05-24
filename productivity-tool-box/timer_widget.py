from PySide6.QtWidgets import QWidget
from ui_timer_widget import Ui_Form


class TimerWidget(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Test Promotimer')