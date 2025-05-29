from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QTimer, QDateTime
from ui_timer_widget import Ui_Form


class TimerWidget(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Test Promotimer')
        self.inint_styling()
        self.init_timer()
        self.init_btns()
        

    
    def init_timer(self):
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)

        # ** Set up variables
        self.isTimerOn = False
        self.duration= 20 
        self.small_break = 15 #TODO Change later
        self.long_breal = 10

        self.session_count = 0
        self.session_mode = 'Work'
        
        self.remaining_secs = self.duration
        self.start_button.clicked.connect(self.toggle_timer)
        self.end_time = None
        self.update_time()


    def toggle_timer(self):
        if not self.isTimerOn:
            self.timer.start(1000)
            self.start_button.setText('Pause')
            self.isTimerOn = True
        else:
            self.timer.stop()
            self.start_button.setText('Start')
            self.isTimerOn = False

        self.update_time()
        

    def update_time(self):
        if self.isTimerOn:
            self.remaining_secs -= 1
        if self.remaining_secs <= 0:

            if self.session_mode == 'Work':
                self.session_count += 1
                if self.session_count % 2 == 0:
                    self.session_mode = 'Long Break'
                    self.remaining_secs = self.long_breal
                else:
                    self.session_mode = 'Small Break'
                    self.remaining_secs = self.small_break
            else:
                self.session_mode = 'Work'
                self.remaining_secs = self.duration
            
            self.clear_timer()
        else:
            min = (self.remaining_secs % 3600) // 60
            sec = self.remaining_secs % 60
            self.timer_input.setText(f'{min:02}:{sec:02}')
    
    def clear_timer(self):
        self.isTimerOn = False
        self.timer.stop()
        self.timer_running = False
        self.end_time = None
        # self.remaining_secs = self.duration
        self.start_button.setText('Start')
        self.update_time()

    def inint_styling(self):
        self.timer_input.setObjectName('timer-input')
        self.label_2.setObjectName('task-label')
        self.current_task_input.setObjectName('task-input')

        with open('style.qss', 'r') as f:
            _style =  f.read()
            self.setStyleSheet(_style)

    def init_btns(self):
        self.restart_button.clicked.connect(self.clear_timer)
