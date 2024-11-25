from noeud import Noeud

class Arbre:
    def __init__(self, racine: Noeud):
        if not isinstance(racine, Noeud):
            raise TypeError("La racine doit être une instance de Noeud")
        self.__racine = racine

    @property
    def racine(self) -> Noeud:
        return self.__racine

    @racine.setter
    def racine(self, nouvelle_racine: Noeud):
        if not isinstance(nouvelle_racine, Noeud):
            raise TypeError("La racine doit être une instance de Noeud")
        self.__racine = nouvelle_racine

    def afficher(self):
        print(self.__racine.afficher())