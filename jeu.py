from balle import Balle
from raquette import Raquette
import tkinter as tk

class Jeu:
    def __init__(self,fenetre):
        self.fenetre = fenetre

        self.largeur_fenetre = 600
        self.hauteur_fenetre = 600

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
        
        self.canevas.pack()
        

    def toucheAppuyee(self,touche):
        touche = touche.keysym

        self.touche_pressee[touche] = True

    def toucheRelachee(self,touche):
        touche = touche.keysym

        self.touche_pressee[touche] = False