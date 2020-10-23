import tkinter as tk
from math import copysign
import jeu

class Balle:
    """
    Balle
    """
    
    def __init__(self,jeu) :
        self.jeu = jeu #OSKOUR
        self.rayon = 10 #Taille de la balle
        self.reset()
        self.graphics = self._dessiner() #initialisation de la variable local objet

    def _dessiner(self): #Créer la balle dans le canevas
        #crée une balle située en x et y de rayon défini au dessus et de couleur blanche
        return self.jeu.canevas.create_oval(self.x-self.rayon, self.y-self.rayon, self.x+self.rayon, self.y+self.rayon, fill="#ffffff")
    
    def paint (self) :  #Appelée depuis l'extèrieur
        xy_coords = self.jeu.canevas.coords(self.graphics)
        self.jeu.canevas.move(self.graphics,(self.x - self.rayon) - xy_coords[0], (self.y - self.rayon) - xy_coords[1])

    def deplacer(self) : #Bouger la balle dans le canevas pour la raquette
        #-----------------------------Raquette-----------------------------#
        #Valeur de la collision avec la raquette.
        v_collision = self.jeu.raquette.collision(self) 
        #Valeur de la collision avec les briques.
        v_collision += self.jeu.niveau.collision(self)
        if abs(v_collision) == 1 :  #Si la collision revoie 1
            self.vitesse_x = -2
            self.vitesse_y = -1
            self.vitesse_y = -copysign(self.vitesse_y, v_collision)
        elif abs(v_collision) == 2 :  #Si la collision revoie 2
            self.vitesse_x = -1
            self.vitesse_y = -2
            self.vitesse_y = -copysign(self.vitesse_y, v_collision)
        elif abs(v_collision) == 3 :  #Si la collision revoie 3
            self.vitesse_x = 0
            self.vitesse_y = -2
            self.vitesse_y = -copysign(self.vitesse_y, v_collision)
        elif abs(v_collision) == 4 :  #Si la collision revoie 4
            self.vitesse_x = 1
            self.vitesse_y = -2
            self.vitesse_y = -copysign(self.vitesse_y, v_collision)
        elif abs(v_collision) == 5 :  #Si la collision revoie 5
            self.vitesse_x = 2
            self.vitesse_y = -1
            self.vitesse_y = -copysign(self.vitesse_y, v_collision)
        #-----------------------------Bords de la fenêtre-----------------------------#
        elif self.y - self.rayon <= 0 : #Si la balle touche le haut, ça inverse la vitesse en ordonnée
            self.vitesse_y = -(self.vitesse_y)
            
        elif self.jeu.hauteur_fenetre() <= (self.y + self.rayon) and self.jeu.niveau.ground == False :
            self.jeu.lives.removeLife()
            if self.jeu.lives.getNbLives() == 0 :
                self.jeu.stopGame()
            else :
                self.x = self.jeu.raquette.x
                self.y = self.jeu.raquette.y - ((self.jeu.raquette.hauteur / 2) + self.rayon)

        elif self.jeu.largeur_fenetre() <= self.x + self.rayon or self.x - self.rayon <= 0 : #Si la balle touche la droite ou la gauche, ça inverse la vitesse en abscisse
            self.vitesse_x = -(self.vitesse_x)


        self.setPosition_x(self.x + self.vitesse_x)
        self.setPosition_y(self.y + self.vitesse_y)

    def limitPosition_x(self, x) :
        r_position = x
        if x > self.jeu.largeur_fenetre() - self.rayon :
            r_position = self.jeu.largeur_fenetre() - self.rayon
        if x < self.rayon  :
            r_position = self.rayon 
        return r_position

    def limitPosition_y(self, y) :
        r_position = y
        if y > self.jeu.largeur_fenetre() - self.rayon :
            r_position = self.jeu.largeur_fenetre() - self.rayon
        if y < self.rayon :
            r_position = self.rayon
        return r_position

    def setPosition_x(self, x) :
        self.x = self.limitPosition_x(x)

    def setPosition_y(self, y) :
        self.y = self.limitPosition_y(y)

    def reset (self) :

        self.x = self.jeu.hauteur_fenetre() / 2 #Position x du Centre
        self.y = self.jeu.raquette.y - self.jeu.raquette.hauteur - self.rayon #Position y du Centre
        self.vitesse_x = 0 #Vitesse sur l'axe x
        self.vitesse_y = 2 #Vitesse sur l'axe y