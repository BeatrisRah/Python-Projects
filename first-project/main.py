from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QGridLayout, QPushButton, QWidget, QLineEdit,QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
import ast
import operator

icon_path = 'C:/Users/Betty/Documents/Py_Projects/images/note_icon.png'

operators = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.USub: operator.neg
}

class MainWIndow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('To do')
        self.setGeometry(100, 100, 600, 700)
        self.setWindowIcon(QIcon(icon_path))
        self.inputBox = '';
        self.inputs = []
        
        self.initUI()


    def initUI(self):
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.main_layout = QVBoxLayout()
        self.central_widget.setLayout(self.main_layout)
        self.central_widget.setStyleSheet('background-color: #282c34;')

        self.line_edit = QLineEdit()
        self.line_edit.setFixedSize(500, 100)
        self.line_edit.setStyleSheet('padding: 8px; color: white; font-size: 16px;')
        self.main_layout.addWidget(self.line_edit, alignment=Qt.AlignmentFlag.AlignCenter)

        self.initButtons()


    def initButtons(self):
        buttons = [
            { 'name': 'C', 'fun': self.clear_inputBox },
            { 'name': '7', 'fun': lambda: self.add_inputBox('7')},
            { 'name': '8', 'fun': lambda: self.add_inputBox('8') },
            { 'name': '9', 'fun': lambda: self.add_inputBox('9') },
            { 'name': '÷', 'fun': lambda: self.on_operation('/') },
            { 'name': '4', 'fun': lambda: self.add_inputBox('4') },
            { 'name': '5', 'fun': lambda: self.add_inputBox('5') },
            { 'name': '6', 'fun': lambda: self.add_inputBox('6') },
            { 'name': '×', 'fun': lambda: self.on_operation('*') },
            { 'name': '1', 'fun': lambda: self.add_inputBox('1') },
            { 'name': '2', 'fun': lambda: self.add_inputBox('2') },
            { 'name': '3', 'fun': lambda: self.add_inputBox('3') },
            { 'name': '+', 'fun': lambda: self.on_operation('+') },
            { 'name': '-', 'fun': lambda: self.on_operation('-') },
            { 'name': '=', 'fun': lambda: self.calculate() },
            { 'name': '0', 'fun': lambda: self.add_inputBox('0') },
            # { 'name': '×', 'fun': lambda: self.add_inputBox('-') },

        ]

        grid = QGridLayout()
        # self.central_widget.setLayout(grid)


        for index, btn in enumerate(buttons):
            row = index // 4 
            col = index % 4
            button = QPushButton(btn['name'], self.central_widget)
            button.clicked.connect(btn['fun'])
            button.setFixedSize(120, 120)
            button.setStyleSheet('background-color: #4b515e; color: white; font-size: 16px; font-weight: bold;')
            grid.addWidget(button, row, col)
        
        self.main_layout.addLayout(grid)

    def on_operation(self, method):

        if(self.is_input_empty()): return
        self.inputs.append(self.inputBox)
        self.inputs.append(method) #! Edje case if user clicks operator but doen't add a new number
        self.clear_inputBox()

    def calculate(self):
        if(self.is_input_empty()): return
        self.inputs.append(self.inputBox)

        def _eval(node):
            if isinstance(node, ast.Expression):
                return _eval(node.body)
            elif isinstance(node, ast.BinOp):
                return operators[type(node.op)](_eval(node.left), _eval(node.right))
            elif isinstance(node, ast.UnaryOp):
                return operators[type(node.op)](_eval(node.operand))
            elif isinstance(node, ast.Num):  # Python <3.8
                return node.n
            elif isinstance(node, ast.Constant):  # Python 3.8+
                return node.value
            else:
                raise TypeError(f"Unsupported type: {type(node)}")
            
        stringCalc = ' '.join(self.inputs)
        parsed = ast.parse(stringCalc, mode='eval')

        self.clear_inputBox()
        self.line_edit.setText(str(_eval(parsed.body)))
        self.inputs.clear()

    def add_inputBox(self, input):
        self.inputBox += input
        self.line_edit.setText(self.inputBox)

    def clear_inputBox(self):
        self.inputBox = ''
        self.line_edit.clear()
    
    def is_input_empty(self):
        return True if self.inputBox == '' else False
        





def main():
    app = QApplication([])
    window = MainWIndow()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()