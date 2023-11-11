from PyQt5.QtWidgets import QApplication, QMessageBox
app = QApplication([])
from main_win import*
from data import qw_list,Question, MyMessageBox
from random import shuffle, choice
from edit_win import*


choice_ans = ""
qw = ""

def stat():
    count = 0
    count_r = 0
    good = 0
    for q in qw_list:
        count += q.count
        count_r += q.count_v
    if count != 0:
        good = count_r/count*100
    else:
        good = 0
    lbl_count.setText(f"Count of answers: {count}")
    lbl_count_right.setText(f"Count of right answers: {count_r}")
    lbl_good.setText(f"Count of good answers: {good}")

def new_qw():
    global qw
    qw_text = lbl_qw.text()  
    qw = choice(qw_list)
    while qw_text == qw.qw:
        qw = choice(qw_list)
    answers = [qw.ans, qw.vrong1, qw.vrong2, qw.vrong3]
    shuffle(answers)
    lbl_qw.setText(qw.qw)
    for i in range(4):
        rbn_list[i].setText(answers[i])

def nul_ans():
    global choice_ans
    choice_ans = ""
    rbn_group.setExclusive(False)
    for i in range(4):
        rbn_list[i].setChecked(False)
    rbn_group.setExclusive(True)

def check_ans():
    if btn_check.text() == "Check":
        if choice_ans == "":
            mess = MyMessageBox("Text")
            #mess.setText("Text")
            #mess.show()
            #mess.exec()
        else:
            if choice_ans == qw.ans:
                lbl_result.setText("Great!") 
                qw.r_ans()
            else:
                lbl_result.setText("No!")
                qw.v_ans()
            lbl_ans.setText(qw.ans)
            btn_check.setText("Next")
            box_ans.hide()
            box_result.show()
    else:
        new_qw()
        nul_ans()
        btn_check.setText("Check")
        box_ans.show()
        box_result.hide()

def clear():
    edit_qw.clear()
    edit_ans.clear()
    edit_wrong1.clear()
    edit_wrong2.clear()
    edit_wrong3.clear()

def add_qw():
    qw_text = edit_qw.text()
    ans_text = edit_ans.text()
    wr1_text = edit_wrong1.text()
    wr2_text = edit_wrong2.text()
    wr3_text = edit_wrong3.text()
    if qw_text != "" and ans_text != "" and wr1_text != "" and wr2_text != "" and wr3_text != "":
        q = Question(qw_text, ans_text, wr1_text, wr2_text, wr3_text)
        qw_list.append(q)
        clear()
        mes = MyMessageBox("New question add to list")
    else:
        mes = MyMessageBox("Not all information is written!")

def click_ans(rbn):
    global choice_ans
    choice_ans = rbn.text()

new_qw()    
def show_menu():
    stat()
    test_win.hide()
    edit_win.show()
    
def show_test():
    test_win.show()
    edit_win.hide()

rbn_group.buttonClicked.connect(click_ans)
btn_check.clicked.connect(check_ans)
btn_mune.clicked.connect(show_menu)
btn_back.clicked.connect(show_test)
btn_add_qw.clicked.connect(add_qw)
btn_clear.clicked.connect(clear)

test_win.show()
app.exec()