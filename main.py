from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QLabel, QPushButton, QLineEdit
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QVBoxLayout
import json

last_entry = []


def get_definition():
    with open("data.json", "r") as f:
        data = json.load(f)
        try:
            for i in data[text_entry.displayText().lower()]:
                result_field.setText(i)
                window.setFixedWidth(400)
                window.setFixedHeight(210)
                last_entry.append(text_entry.displayText())
        except KeyError:
            result_field.setText("Invalid Entry")


def clear_text():
    text_entry.setText("")
    result_field.setText("Enter a word!")
    window.setFixedWidth(261)
    window.setFixedHeight(150)


def close_window():
    app.quit()


app = QApplication([])
window = QWidget()
window.setWindowTitle("Dictionary by C.P.")
layout1 = QVBoxLayout()
window.setLayout(layout1)
layout2 = QHBoxLayout()
layout1.addLayout(layout2)
layout3 = QHBoxLayout()
layout1.addLayout(layout3)


text_entry = QLineEdit()
text_entry.returnPressed.connect(get_definition)
layout2.addWidget(text_entry)

definition_btn = QPushButton("Definition")
definition_btn.clicked.connect(get_definition)
layout2.addWidget(definition_btn)

exit_btn = QPushButton("Exit")
exit_btn.clicked.connect(close_window)
layout3.addWidget(exit_btn)

clear_btn = QPushButton("Clear")
clear_btn.clicked.connect(clear_text)
layout3.addWidget(clear_btn)


result_field = QLabel("Welcome! Enter a word to begin!!")
result_field.setWordWrap(True)
layout1.addWidget(result_field)

window.show()
app.exec()
