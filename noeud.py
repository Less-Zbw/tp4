class Noeud:
    
    def __init__(self, nom: str):
        
        self.nom = nom
        self.enfants = []
    
    def ajouter_enfant(self, noeud):

        self.enfants.append(noeud)    

    def afficher(self):
        
        if not self.enfants:
            return self.nom  
        else:
            enfants_expr = ", ".join(enfant.afficher() for enfant in self.enfants)
            return f"{self.nom}({enfants_expr})"    