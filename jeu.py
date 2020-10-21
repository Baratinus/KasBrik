from balle import Balle
from raquette import Raquette
import tkinter as tk

def verifierTouche(fonction):

        def fonction_modifiee(self, touche):
            if touche.keysym in self.touche_possible:
                return fonction(self, touche)

        return fonction_modifiee

class Jeu :
    def __init__(self,fenetre,largeur_fenetre:int,hauteur_fenetre:int):
        self.fenetre = fenetre

        self.largeur_fenetre = largeur_fenetre
        self.hauteur_fenetre = hauteur_fenetre

        self.canevas = tk.Canvas(fenetre,width=self.largeur_fenetre,height=self.hauteur_fenetre)

        self.raquette = Raquette(self)
        self.balle = Balle(self)

        self.touche_possible = ["q","d"]
        self.touche_pressee = {}

        # Premier affichage des objets !! temporaire
        self.balle.dessiner()
        self.raquette.image

    def miseAJour(self):
        # Vérification si une touche est appuyer et exécuter l'action
        if self.touche_pressee.get("q") :
            self.raquette.aller_Gauche()
        if self.touche_pressee.get("d") :
            self.raquette.aller_Droite() 

        # Déplacement de la balle
        self.balle.deplacer()

        # mise à jour du canevas sur la surface
        self.canevas.pack()

    @verifierTouche
    def toucheAppuyee(self,touche):
        """Si une touche est apuyée

        Args:
            touche (tkinter.Event): touche préssée
        """
        touche = touche.keysym
        self.touche_pressee[touche] = True

    @verifierTouche
    def toucheRelachee(self,touche):
        """Si une touche est relachée

        Args:
            touche (tkinter.Event): touche relachée
        """
        touche = touche.keysym
        self.touche_pressee[touche] = False