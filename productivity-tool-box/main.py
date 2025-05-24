from PySide6 import QtWidgets
from timer_widget import TimerWidget
import sys

app = QtWidgets.QApplication(sys.argv)

window = TimerWidget()
window.show()

app.exec()