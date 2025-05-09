from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QWidget, QPushButton
from PyQt5.QtGui import QIcon

icon_path = 'C:/Users/Betty/Documents/Py_Projects/images/note_icon.png'


class MainWIndow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('To do')
        self.setGeometry(100, 100, 600, 500)
        self.setWindowIcon(QIcon(icon_path))
        self.initUI()

    def initUI(self):
        self.initButtons()
        # cental_widget = QWidget()
        # self.setCentralWidget(cental_widget)


    def initButtons(self):
        buttons = [
            { 'name': 'C', 'fun': self.on_click }
        ]

        def createButton(btn):
            button = QPushButton(btn['name'], self)
            button.clicked.connect(self.on_click)
        
        for btn in buttons:
            createButton(btn)

        return

    def on_click(self):
        print('i was clicked')



def main():
    app = QApplication([])
    window = MainWIndow()
    label = QLabel('Hello, PyQt!', parent=window)
    label.move(100, 80)
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()