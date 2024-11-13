from test import Chine
from Poly import Polynome
from noeud import Noeud
from arbre import arbre
#c = Chine()
#c.afficher()

""""
if __name__ == "__main__":
    #p(x) = 1 - 1x - 2x^2 + 2x^3 - 3x^4
    coefficients = [1, -1, -2, 2, -3]
    p = Polynome(coefficients)

    # print
    print("polynome p(x):", p)

    # test
    x_values = [1, 2]
    for x in x_values:
        print(f"p({x}) = {p.evaluate(x)}")
"""
racine = Noeud("mul")
noeud_3 = Noeud("3")
noeud_sin = Noeud("sin")
noeud_x = Noeud("x")

noeud_sin.ajouter_enfant(noeud_x)  
racine.ajouter_enfant(noeud_3)    
racine.ajouter_enfant(noeud_sin) 

arbre = arbre(racine)

print(arbre.afficher())  