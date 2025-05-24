from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QTimer, QDateTime
from ui_timer_widget import Ui_Form


class TimerWidget(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Test Promotimer')
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.start_button.clicked.connect(self.start_timer)
        self.end_time = QDateTime.currentDateTime().addSecs(60 * 60)

    def start_timer(self):
        self.timer.start(1000)
        self.update_time()

    def update_time(self):
        now =QDateTime.currentDateTime()
        remaining = now.secsTo(self.end_time)

        if(remaining <= 0):
            self.clear_timer()
        else:
            hours = remaining // 3600
            min = (remaining % 3600) // 60
            sec = remaining % 60
            self.timer_input.setText(f'{hours:02}:{min:02}:{sec:02}')
    
    def clear_timer(self):
        self.timer.stop()
