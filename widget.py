from PySide6.QtWidgets import QWidget, QLineEdit, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QComboBox, QDateEdit
from todo import Todo
from datetime import date

class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.todo = Todo()
        self.setWindowTitle('Todo App')

        taskLabel = QLabel('Task : ')
        self.task_input = QLineEdit()
        priorityLabel = QLabel('Priority : ')
        self.priority_input = QComboBox()
        self.priority_input.addItems(['1','2','3'])
        dateLabel = QLabel('Date : ')
        self.date_input = QDateEdit()
        self.date_input.setDate(date.today())

        addButton = QPushButton('Add')
        addButton.clicked.connect(self.add_button_clicked)
        resetButton = QPushButton('Reset')
        resetButton.clicked.connect(self.resetTodo)

        self.task_show_label = QLabel('Tasks Here...')

        h_layout = QHBoxLayout()
        h_layout.addWidget(priorityLabel)
        h_layout.addWidget(self.priority_input)
        h_layout.addWidget(taskLabel)
        h_layout.addWidget(self.task_input)
        h_layout.addWidget(dateLabel)
        h_layout.addWidget(self.date_input)

        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout)
        v_layout.addWidget(addButton)
        v_layout.addWidget(resetButton)
        v_layout.addWidget(self.task_show_label)

        self.setLayout(v_layout)
    
    def resetDefault(self):
        self.task_input.setText('')
        self.date_input.setDate(date.today())
        self.priority_input.setCurrentIndex(0)
        pass
    def resetTodo(self):
        self.todo.reset()
        self.resetDefault()
        self.task_show_label.setText('')
        pass
    def add_button_clicked(self):
        self.todo.add(
            task = self.task_input.text(),
            priority = int(self.priority_input.currentText()),
            date = self.date_input.text()
            )
        self.task_show_label.setText(self.todo.getIncompleteTasks())
        # Reset to default
        self.resetDefault()