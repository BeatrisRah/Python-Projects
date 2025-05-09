from PyQt5.QtWidgets import QApplication, QLabel, QWidget
from PyQt5.QtGui import QIcon

app = QApplication([])
window = QWidget()
window.setWindowTitle('To do')
window.setGeometry(100, 100, 600, 500)

icon_path = 'C:/Users/Betty/Documents/Py_Projects/images/note_icon.png'
window.setWindowIcon(QIcon(icon_path))

label = QLabel('Hello, PyQt!', parent=window)
label.move(100, 80)

def main():
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()