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
        r_ans += 1
        self.count_v += 1
    def v_ans(self):



qw1 = Question("Скільки ніг у риби?", "a. 0", "b. 1", "c. 2", "d. 4")
qw2 = Question("Який птах може літити задом на перед?", "a. колібрі", "b. чайка", "c. фазан", "d.")
qw3 = Question("Скільки ніг у риби?", "a. як горіх", "b.", "c.", "d.")
qw4 = Question("Скільки ніг у риби?", "a. 0", "b. 1", "c. 2", "d. 4")
qw_list = list()