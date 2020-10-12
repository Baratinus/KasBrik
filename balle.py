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
        self.vitesse_y = 2 #Vitesse sur l'axe y
        self.objet = 0 #initialisation de la variable local objet

    def dessiner(self): #Créer la balle dans le canevas
        #crée une balle située en x et y de rayon défini au dessus et de couleur blanche
        self.objet = self.jeu.canevas.create_oval(self.x, self.y, self.x+self.rayon*2, self.y+self.rayon*2, fill="#ffffff")
        return None

    def deplacer(self): #Bouger la balle dans le canevas pour la raquette
        #-----------------------------Raquette-----------------------------#
        if self.jeu.raquette.collision(self.x+self.rayon) == 1 and self.y-self.rayon*2 >= 485 and self.y-self.rayon*2 <= 505 : #Si la collision revoie 1
            self.vitesse_y = -1
            self.vitesse_x = -2
            self.jeu.canevas.move(self.objet,self.vitesse_x,self.vitesse_y)
        elif self.jeu.raquette.collision(self.x+self.rayon) == 2 and self.y-self.rayon*2 >= 485 and self.y-self.rayon*2 <= 505 : #Si la collision revoie 2
            self.vitesse_y = -2
            self.vitesse_x = -1
            self.jeu.canevas.move(self.objet,self.vitesse_x,self.vitesse_y)
        elif self.jeu.raquette.collision(self.x+self.rayon) == 3 and self.y-self.rayon*2 >= 485 and self.y-self.rayon*2 <= 505 : #Si la collision revoie 3
            self.vitesse_y = -2
            self.vitesse_x = 0
            self.jeu.canevas.move(self.objet,self.vitesse_x,self.vitesse_y)
        elif self.jeu.raquette.collision(self.x+self.rayon) == 4 and self.y-self.rayon*2 >= 485 and self.y-self.rayon*2 <= 505 : #Si la collision revoie 4
            self.vitesse_y = -2
            self.vitesse_x = 1
            self.jeu.canevas.move(self.objet,self.vitesse_x,self.vitesse_y)
        elif self.jeu.raquette.collision(self.x+self.rayon) == 5 and self.y-self.rayon*2 >= 485 and self.y-self.rayon*2 <= 505 : #Si la collision revoie 5
            self.vitesse_y = -1
            self.vitesse_x = 2
            self.jeu.canevas.move(self.objet,self.vitesse_x,self.vitesse_y)
        #-----------------------------Bords de la fenêtre-----------------------------#
        elif self.jeu.hauteur_fenetre <= self.y + self.rayon*2 or self.y <= 0 : #Si la balle touche le haut ou le bas, ça inverse la vitesse en ordonnée
            self.vitesse_y = -(self.vitesse_y)
            self.jeu.canevas.move(self.objet,self.vitesse_x,self.vitesse_y)
        elif self.jeu.largeur_fenetre <= self.x + self.rayon*2 or self.x <= 0 : #Si la balle touche la droite ou la gauche, ça inverse la vitesse en abscisse
            self.vitesse_x = -(self.vitesse_x)
            self.jeu.canevas.move(self.objet,self.vitesse_x,self.vitesse_y)
        #-----------------------------Sinon suit la trajectoire-----------------------------#
        else:
            self.jeu.canevas.move(self.objet,self.vitesse_x,self.vitesse_y)
        self.x += self.vitesse_x
        self.y += self.vitesse_y
        # print(self.x,self.y,self.x + self.rayon*2,self.y-self.rayon*2,self.jeu.raquette.collision(self.x+self.rayon))
        return None