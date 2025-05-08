from PyQt5.QtWidgets import QApplication, QLabel, QWidget

app = QApplication([])
window = QWidget()
window.setWindowTitle('My PyQt App')
window.setGeometry(100, 100, 300, 200)

label = QLabel('Hello, PyQt!', parent=window)
label.move(100, 80)

window.show()
app.exec_()