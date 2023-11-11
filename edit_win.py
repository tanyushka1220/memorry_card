from PyQt5.QtWidgets import (QLabel,QLineEdit, QGridLayout)
from PyQt5.QtCore import Qt
from data import MyWidget, MyPushButton, MyLabel, MyLineEdit


edit_win = MyWidget()

#edit_win.resize(600,500)
#edit_win.setWindowTitle("MUNE")
#edit_win.move(300,300)

lbl_qw_edit = QLabel("Question question")
lbl_ans_edit = QLabel("Right answer text")
lbl_wr1_edit = QLabel("Wrong answer 1 question")
lbl_wr2_edit = QLabel("Wrong answer 2 text")
lbl_wr3_edit = QLabel("Wrong answer 3 question")

edit_qw = MyLineEdit()
edit_ans = MyLineEdit()
edit_wrong1 = MyLineEdit()
edit_wrong2 = MyLineEdit()
edit_wrong3 = MyLineEdit()

btn_add_qw = MyPushButton("Add question")
btn_clear = MyPushButton("Clear")

lbl_stat = MyLabel("Statistic")
lbl_count = QLabel("Count of answers")
lbl_count_right = QLabel("Count of right answers")
lbl_good = QLabel("Good %")

btn_back = MyPushButton("Back")

grid = QGridLayout()
grid.addWidget(lbl_qw_edit, 0,0)
grid.addWidget(edit_qw, 0,1)

grid.addWidget(lbl_ans_edit, 1,0)
grid.addWidget(edit_ans, 1,1)

grid.addWidget(lbl_wr1_edit, 2,0)
grid.addWidget(edit_wrong1, 2,1)

grid.addWidget(lbl_wr2_edit, 3,0)
grid.addWidget(edit_wrong2, 3,1)

grid.addWidget(lbl_wr3_edit, 4,0)
grid.addWidget(edit_wrong3, 4,1)

grid.addWidget(btn_add_qw, 5,0)
grid.addWidget(btn_clear, 5,1)

grid.addWidget(lbl_stat, 6,0)
grid.addWidget(lbl_count, 7,0)
grid.addWidget(lbl_count_right, 8,0)
grid.addWidget(lbl_good,9,0)

grid.addWidget(btn_back, 10 ,0,2,0)

edit_win.setLayout(grid)
edit_win.hide()