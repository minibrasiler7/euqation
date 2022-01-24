class Solver:
    def __init__(self, coeff_degre_0, coeff_degree_x):
        self.coeff_degree_0 = coeff_degre_0
        self.coeff_degree_x = coeff_degree_x
        self.equation_reduite = self.reduction()

    def reduction(self):
        coeff_0_reduct = []
        somme = 0
        coeff_x_reduct = []
        for i in range(len(self.coeff_degree_0[0])):
            somme += self.coeff_degree_0[0][i]
        coeff_0_reduct.append(somme)
        somme = 0
        for i in range(len(self.coeff_degree_0[1])):
            somme += self.coeff_degree_0[1][i]
        coeff_0_reduct.append(somme)
        somme = 0
        for i in range(len(self.coeff_degree_x[0])):
            somme += self.coeff_degree_x[0][i]
        coeff_x_reduct.append(somme)
        somme = 0
        for i in range(len(self.coeff_degree_x[1])):
            somme += self.coeff_degree_x[1][i]
        coeff_x_reduct.append(somme)

        return [[coeff_x_reduct[0], coeff_0_reduct[0]], [coeff_x_reduct[1], coeff_0_reduct[1]]]

    def trier_variable_constante(self):
        new_eq = []
        new_eq.append(self.equation_reduite[0][0]-self.equation_reduite[1][0])
        new_eq.append(self.equation_reduite[1][1]-self.equation_reduite[0][1])
        print(new_eq)
        return new_eq
    def find_solution(self):
        eq = self.trier_variable_constante()
        result = ""
        if eq[0] == 0 and eq[1] == 0:
            result = "{\mathbb{R}}"
        elif eq[0] == 0 and eq[1]!= 0:
            result = "{\O}"
        else:
            if (eq[1]/eq[0]) % 1 == 0:
                result = "{"+str(eq[1]/eq[0])+"}"
            else:
                result = f"\\frac{{{eq[1]}}}{{{eq[0]}}}"

        result = "x = " + result
        return result


    def display_equation_trier(self):
        equation = self.trier_variable_constante()
        chaine = ""
        if equation[0]!= 0:
            chaine += str(equation[0]) + "x = " + str(equation[1])
        else:
            chaine += str(equation[0]) + " = " + str(equation[1])
        return chaine


    def display_equation(self):
        chaine = ""
        for i in range(2):
            if i == 0 and self.equation_reduite[0][i] != 0:
                chaine += str(self.equation_reduite[0][i])+"x"
            else:
                if self.equation_reduite[0][i] > 0:
                    if self.equation_reduite[0][0] != 0:
                        chaine += "+" + str(self.equation_reduite[0][i])
                    else:
                        chaine += str(self.equation_reduite[0][i])

                elif self.equation_reduite[0][i] < 0:
                    chaine += str(self.equation_reduite[0][i])

        chaine += "="

        for i in range(2):
            if i == 0 and self.equation_reduite[1][i] != 0:
                chaine += str(self.equation_reduite[1][i])+"x"
            else:
                if self.equation_reduite[1][i] > 0:
                    if self.equation_reduite[1][0] != 0:
                        chaine += "+" + str(self.equation_reduite[1][i])
                    else:
                        chaine += str(self.equation_reduite[1][i])
                elif self.equation_reduite[1][i] < 0:
                    chaine += str(self.equation_reduite[1][i])
        return chaine










