import tkinter as tk
import jeu

class Balle:
    """
    Balle
    """
    
    def __init__(self,jeu):
        self.jeu = jeu #OSKOUR
        self.x = 295 #Position x du coin supérieur gauche de la balle
        self.y = 200 #Position y du coin supérieur gauche de la balle
        self.rayon = 10 #Taille de la balle
        self.vitesse_x = 0 #Vitesse sur l'axe x
        self.vitesse_y = -1 #Vitesse sur l'axe y
        self.objet = 0

    def dessiner(self): #Créer la balle dans le canevas
        #crée une balle située en x et y de rayon défini au dessus et de couleur blanche
        self.objet = self.jeu.canevas.create_oval(self.x, self.y, self.x+self.rayon, self.y+self.rayon, fill="#ffffff")
        return None

    def deplacer(self): #Bouger la balle dans le canevas
        if self.jeu.raquette.valeur_collision == 0:
            self.jeu.canevas.move(self.jeu.balle,self.vitesse_x,self.vitesse_y)
        elif self.jeu.raquette.valeur_collision == 1:
            self.vitesse_x = -1
            self.vitesse_y = -2
            self.jeu.canevas.move(self.jeu.balle,self.vitesse_x,self.vitesse_y)
        elif self.jeu.raquette.valeur_collision == 2:
            self.vitesse_x = -2
            self.vitesse_y = -1
            self.jeu.canevas.move(self.jeu.balle,self.vitesse_x,self.vitesse_y)
        elif self.jeu.raquette.valeur_collision == 3:
            self.vitesse_x = -2
            self.vitesse_y = 0
            self.jeu.canevas.move(self.jeu.balle,self.vitesse_x,self.vitesse_y)
        elif self.jeu.raquette.valeur_collision == 4:
            self.vitesse_x = -2
            self.vitesse_y = 1
            self.jeu.canevas.move(self.jeu.balle,self.vitesse_x,self.vitesse_y)
        elif self.jeu.raquette.valeur_collision == 5:
            self.vitesse_x = -1
            self.vitesse_y = 2
            self.jeu.canevas.move(self.jeu.balle,self.vitesse_x,self.vitesse_y)
        return None