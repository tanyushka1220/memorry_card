from PyQt5.QtWidgets import (QWidget,QLabel,QPushButton,
                            QSpinBox, QGroupBox, QButtonGroup, 
                            QRadioButton, QVBoxLayout, QHBoxLayout)
from PyQt5.QtCore import Qt

test_win = QWidget()
test_win.resize(600,500)
test_win.move(300,300)
test_win.setWindowTitle("MEMORRY CARD")

btn_mune = QPushButton("Menu")
btn_rest = QPushButton("Rest")
time_rest = QSpinBox()
time_rest.setValue(30)
lbl_rest = QLabel("minutes")

lbl_qw = QLabel("question")

box_ans = QGroupBox()
box_ans.setTitle("Answer")
rbn_list = list()
rbn_group = QButtonGroup()
for i in range(4):
    rbt = QRadioButton("a")
    rbn_group.addButton(rbt)
    rbn_list.append(rbt)

box_result = QGroupBox()
box_result.setTitle("Result")
lbl_ans = QLabel("ans")
lbl_result = QLabel("result")

btn_check = QPushButton("Check")

main_line = QVBoxLayout()
line_h1 = QHBoxLayout()
line_h2 = QHBoxLayout()
line_h3 = QHBoxLayout()
line_h4 = QHBoxLayout()

line_h1.addWidget(btn_mune)
line_h1.addStretch(3)
line_h1.addWidget(btn_rest)
line_h1.addWidget(time_rest)
line_h1.addWidget(lbl_rest)

line_h2.addWidget(lbl_qw, alignment= Qt.AlignCenter)



line_h3.addWidget(box_result)
box_result.hide()
line_h3.addWidget(box_ans)

line_h4.addStretch(2)
line_h4.addWidget(btn_check)
line_h4.addStretch(2)

#block result
line_V1 = QVBoxLayout()
line_V1.addWidget(lbl_ans, alignment=Qt.AlignLeft)
line_V1.addWidget(lbl_result, alignment=Qt.AlignCenter)
box_result.setLayout(line_V1)

#block ans
line_V2 = QVBoxLayout()
line_V3 = QVBoxLayout()
line_h5 = QHBoxLayout()
line_V2.addWidget(rbn_list[0])
line_V2.addWidget(rbn_list[1])
line_V3.addWidget(rbn_list[2])
line_V3.addWidget(rbn_list[3])
line_h5.addLayout(line_V2)
line_h5.addLayout(line_V3)
box_ans.setLayout(line_h5)

main_line.addLayout(line_h1)
main_line.addLayout(line_h2)
main_line.addLayout(line_h3)
main_line.addLayout(line_h4)

test_win.setLayout(main_line)