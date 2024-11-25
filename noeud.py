class Noeud:
    def __init__(self, nom: str):
        self.__nom = nom
        self.__enfants = []

    @property
    def nom(self) -> str:
        return self.__nom

    @property
    def enfants(self) -> list:
        return self.__enfants

    def ajouter_enfant(self, noeud: 'Noeud'):
        if not isinstance(noeud, Noeud):
            raise TypeError("L'enfant doit être une instance de Noeud")
        if noeud in self.__lister_descendants():
            raise ValueError("Ajout impossible: création d'un cycle détecté dans l'arbre")
        self.__enfants.append(noeud)

    def __lister_descendants(self) -> list:
        descendants = []
        for enfant in self.__enfants:
            descendants.append(enfant)
            descendants.extend(enfant.__lister_descendants())
        return descendants

    def afficher(self):
        if not self.__enfants:
            return self.__nom
        else:
            enfants_expr = ", ".join(enfant.afficher() for enfant in self.__enfants)
            return f"{self.__nom}({enfants_expr})"    