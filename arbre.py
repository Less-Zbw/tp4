from noeud import Noeud

class arbre:
    
    def __init__(self, racine: Noeud):
        
        self.racine = racine
    
    def afficher(self):
        
        return self.racine.afficher() 