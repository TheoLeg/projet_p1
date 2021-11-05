from typing import Iterator
from src.collecte import Collecte
from src.ressource import Ressource
from src.traitement import Traitement

une_collecte = Collecte(["http://math.univ-angers.fr", "http://www.univ-angers.fr"])  # collecte composée de 2 ressources
une_collecte.run()                # récupére les ressources et en extrait le texte pertinent

tab = une_collecte.content()


tr = Traitement()

tr.load(tab)

tr.run()

tr_basique = tr.show()[0]

for i in range(10):

    mot = list(tr_basique)[i]


    occurence = tr_basique[mot]
    
    print(f"la fréquence dapparition du terme {mot} est : {100*occurence/len(tr.result[0])}")