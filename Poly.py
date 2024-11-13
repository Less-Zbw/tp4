class Polynome:
    def __init__(self, coefficients):
        
        self.coefficients = coefficients

    def evaluate(self, x):
        
        result = 0
        for i, coef in enumerate(self.coefficients):
            result += coef * (x ** i)
        return result

    def __str__(self):
        
        terms = []
        for i, coef in enumerate(self.coefficients):
            if coef != 0:
                if i == 0:
                    terms.append(f"{coef}")
                elif i == 1:
                    terms.append(f"{coef}x")
                else:
                    terms.append(f"{coef}x^{i}")
        return " + ".join(terms).replace("+ -", "- ")  