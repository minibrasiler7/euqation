import math
import random
import monôme

class Polynomes:
    def __init__(self):
        self.number_terme = random.randint(2, 6)
        self.expression = []
        self.init_expression()


    def init_expression(self):
        for i in range(self.number_terme):
            self.expression.append(monôme.Monomes())

    def display_expression(self):
        chaine_expression = ""
        for i in range(self.number_terme):
            if i == 0 and self.expression[i].sign == "+":
                chaine_expression += str(int(self.expression[i].coefficient)) + self.expression[i].symbole
            else:
                chaine_expression += self.expression[i].sign + str(int(math.fabs(self.expression[i].coefficient))) + self.expression[i].symbole
        return chaine_expression



