from test import Chine
from Poly import Polynome
from noeud import Noeud
from arbre import Arbre
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
# Création des noeuds pour l'expression mul(3, sin(x))
mul_node = Noeud("mul")
trois_node = Noeud("3")
sin_node = Noeud("sin")
x_node = Noeud("x")

# Construction de l'arbre
sin_node.ajouter_enfant(x_node)
mul_node.ajouter_enfant(trois_node)
mul_node.ajouter_enfant(sin_node)

# Création de l'arbre et affichage
arbre = Arbre(mul_node)
arbre.afficher()