from balle import Balle
from raquette import Raquette
import tkinter as tk

class Jeu:
    def __init__(self,fenetre,largeur_fenetre:int,hauteur_fenetre:int):
        self.fenetre = fenetre

        self.largeur_fenetre = largeur_fenetre
        self.hauteur_fenetre = hauteur_fenetre

        self.canevas = tk.Canvas(fenetre,width=self.largeur_fenetre,height=self.hauteur_fenetre)

        self.raquette = Raquette(self)
        self.balle = Balle(self)

        self.touche_possible = ["q","d"]
        self.touche_pressee = {}

    def miseAJour(self):
        # partie temporaire
        if self.balle.objet != 0:
            self.canevas.delete(self.balle.objet)
        self.balle.dessiner()
        self.raquette.image
        
        # Vérification si une touche est appuyer et exécuter l'action
        # if self.touche_pressee.get("q"):
		# 	self.raquette.deplacementGuache()
		# if self.touche_pressee.get("d"):
		# 	self.raquette.deplacementDroite()

        self.canevas.pack()

    def verfierTouche(self, fonction):

        def fonction_modifiee(self, touche):
            if touche.keysym in self.touche_possible:
                return fonction(self, touche)

        return fonction_modifiee

    @verfierTouche
    def toucheAppuyee(self,touche):
        """Si une touche est apuyée

        Args:
            touche (tkinter.Event): touche préssée
        """
        touche = touche.keysym
        self.touche_pressee[touche] = True

    @verfierTouche
    def toucheRelachee(self,touche):
        """Si une touche est relachée

        Args:
            touche (tkinter.Event): touche relachée
        """
        touche = touche.keysym
        self.touche_pressee[touche] = False