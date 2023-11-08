class Question:
    def init(self, qw, ans, vrong1, vrong2, vrong3):
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