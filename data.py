class Question:
    def __init__(self, qw, ans, vrong1, vrong2, vrong3):
        self.qw = qw
        self.ans = ans 
        self.vrong1 = vrong1
        self.vrong2 = vrong2 
        self.vrong3 = vrong3
        self.count = 0
        self.count_v = 0
    def r_ans(self):
        self.count += 1
        self.count_v += 1
    def v_ans(self):
        self.count += 1



qw1 = Question("Скільки ніг у риби?", "0", "1", "2", "4")
qw2 = Question("Який птах може літити задом на перед?", "колібрі", "чайка", "фазан", "курка ")
qw3 = Question("Який мозок у страуса?", "як горіх", "як у людини", "як у тигра", "як у земноводних")
qw4 = Question("скільки зірок на небі?", "більше перечислиного", "міліарда", "триліард", "мільйон")
qw_list = [qw1,qw2,qw3,qw4]


#my class widgets
from PyQt5.QtWidgets import (QWidget,QLabel,QPushButton,
                            QSpinBox, QGroupBox, QRadioButton)

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet('''
                            background-color: rgb(189, 248, 189);
                            color: DarkGreen;
                            font-family: Cambria, Cochin, Georgia, Times, 'Times New Roman', serif;
                            font-size: 15px;
                            font-weight: 100;
                            font-style: italic;
                           ''')
        
class MyPushButton(QPushButton):
    def __init__(self, text):
        super().__init__(text)
        self.setStyleSheet('''
                            QPushButton{
                            border: 5px outset DarkGreen;
                            border-bottom: 8px outset DarkGreen;
                            border-right: 8px outset DarkGreen;
                            border-radius: 13px;
                            padding: 5px;
                            }
                           QPushButton:pressed{
                           border: 5px inset DarkGreen;
                           border-bottom: 8px inset DarkGreen;
                           border-right: 8px inset DarkGreen;
                           background-color: rgb(106, 170, 106);
                           color: rgb(2, 155, 2);
                           }
                           ''')

class MyLabel(QLabel):
    def __init__(self, text):
        super().__init__(text)
        self.setStyleSheet('''
                            font-size: 26px;
                            ''')
        
class MySpinBox(QSpinBox):
    def __init__(self):
        super().__init__()
        self.setStyleSheet('''
                            border: 3px outset DarkGreen;
                            ''')