from polynôme import Polynomes

class Equation:

    def __init__(self):
        self.membre_gauche = Polynomes()
        self.membre_droite = Polynomes()
        self.symbol = "="

    def display_equation(self):
        chaine = self.membre_gauche.display_expression() +" "+self.symbol +" "+ self.membre_droite.display_expression()
        return chaine

    def coefficient_degre(self, degree):
        coeff = []
        coeff.append([])
        for i in range(len(self.membre_gauche.expression)):
            if self.membre_gauche.expression[i].degree == degree:
                coeff[0].append(self.membre_gauche.expression[i].coefficient)
        coeff.append([])
        for j in range(len(self.membre_droite.expression)):
            if self.membre_droite.expression[j].degree == degree:
                coeff[1].append(self.membre_droite.expression[j].coefficient)
        return coeff







