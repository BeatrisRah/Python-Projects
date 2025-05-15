from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QGridLayout, QPushButton, QWidget
from PyQt5.QtGui import QIcon

icon_path = 'C:/Users/Betty/Documents/Py_Projects/images/note_icon.png'


class MainWIndow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('To do')
        self.setGeometry(100, 100, 600, 700)
        self.setWindowIcon(QIcon(icon_path))
        self.initUI()

        self.input = '';

    def initUI(self):
        self.central_widget = QWidget(self)  # ✅ fixed typo
        self.setCentralWidget(self.central_widget)
        self.initButtons()


    def initButtons(self):
        buttons = [
            { 'name': 'C', 'fun': self.on_click },
            { 'name': '7', 'fun': lambda: self.add_input('7')},
            { 'name': '8', 'fun': lambda: self.add_input('8') },
            { 'name': '9', 'fun': lambda: self.add_input('9') },
            { 'name': '÷', 'fun': lambda: self.add_input('/') },
            { 'name': '4', 'fun': lambda: self.add_input('4') },
            { 'name': '5', 'fun': lambda: self.add_input('5') },
            { 'name': '6', 'fun': lambda: self.add_input('6') },
            { 'name': '×', 'fun': lambda: self.add_input('*') },
            { 'name': '1', 'fun': lambda: self.add_input('1') },
            { 'name': '2', 'fun': lambda: self.add_input('2') },
            { 'name': '3', 'fun': lambda: self.add_input('3') },
            { 'name': '-', 'fun': lambda: self.add_input('+') },
            { 'name': '0', 'fun': lambda: self.add_input('0') },
            # { 'name': '×', 'fun': lambda: self.add_input('-') },

        ]

        grid = QGridLayout()
        self.central_widget.setLayout(grid)  

        for index, btn in enumerate(buttons):
            row = index // 4 
            col = index % 4
            button = QPushButton(btn['name'], self.central_widget)
            button.clicked.connect(btn['fun'])
            button.setFixedSize(120, 120)
            grid.addWidget(button, row, col)


    def on_click(self):
        print('i was clicked')
    def add_input(self, input):
        self.input += input





def main():
    app = QApplication([])
    window = MainWIndow()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()