import random


class Monomes:
    def __init__(self):
        self.coefficient = 0
        self.degree = 0
        self.symbole = ""
        self.sign = "+"
        self.init_coefficient()
        self.init_degree()

    def init_coefficient(self):
        while self.coefficient == 0:
            self.coefficient = random.randint(-5, 9)
        if self.coefficient > 0:
            self.sign = "+"
        else:
            self.sign = "-"

    def init_degree(self):
        ran = random.random()
        if ran >= 0.5:
            self.degree = 1
            self.symbole = "x"
        else:
            self.degree = 0
            self.symbole = ""

    def monome_empty(self, coefficient, degree):
        self.coefficient = coefficient
        self.degree = degree
        if degree == 0:
            self.symbole = ""
        else:
            self.symbole = "X"
        if coefficient > 0:
            self.sign = "+"
        else:
            self.sign = "-"
