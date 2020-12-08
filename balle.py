# Import des Librairies nécessaires, et des classes d'autres fichiers.
import tkinter as tk # Pour la gestion de Fenêtres.
from math import copysign, pi, sin, cos, atan2, sqrt # Import du module math et des différentes fonctions pour la gestion des collisions.
from random import random # Import du module random pour 'randomizer' la trajectoire de la balle à chaque collision.
import jeu # Pour la gestion du Jeu.

class Balle:
    '''
        Classe Balle visant à créer l'objet Balle pour le jeu 'casse brique'.
    '''
    
    def __init__(self,i_jeu) :
        '''
            Définition des variables du constructeur.
        '''
        self.jeu = i_jeu # Définit l'attribut jeu entrée dans le constructeur.
        self.rayon = 8 # Taille du rayon de la Balle.
        self.reset() # Reinitialise tout les paramètres de la Balle.
        self.graphics = self._dessiner() # Initie self.graphics avec la méthode locale _dessiner . 

    def _dessiner(self): 
        '''
             Fonction visant à créer le canevas de la Balle.
        '''
        #crée une balle située en x et y de rayon défini au dessus et de couleur blanche
        return self.jeu.canevas.create_oval(self.x-self.rayon, self.y-self.rayon, self.x+self.rayon, self.y+self.rayon, fill="#ffffff")
    
    def paint (self) :
        '''
            Fonction appelée depuis l'extèrieur visant à mettre a jour les coordonnées de la Balle et de la déplacer.
        '''
        xy_coords = self.jeu.canevas.coords(self.graphics)
        self.jeu.canevas.move(self.graphics,(self.x - self.rayon) - xy_coords[0], (self.y - self.rayon) - xy_coords[1])

    def deplacer(self) : 
        '''
            Fonction visant à déplacer la balle dans le canevas par rapport a la raquette.
        '''

        #-----------------------------Raquette-----------------------------#

        #Valeur de la collision avec la raquette.
        v_collision = self.jeu.raquette.collision(self) 
        if abs(v_collision) == 1 :  #Si la collision revoie 1
            self.vitesse_x = -1
            self.vitesse_y = 0.5
            self.vitesse_y = copysign(self.vitesse_y, v_collision)
            self.angle = atan2(self.vitesse_y, self.vitesse_x) 
            self.vitesse = sqrt((self.vitesse_y**2) + (self.vitesse_x**2))
        elif abs(v_collision) == 2 :  #Si la collision revoie 2
            self.vitesse_x = -0.5
            self.vitesse_y = 1
            self.vitesse_y = copysign(self.vitesse_y, v_collision)
            self.angle = atan2(self.vitesse_y, self.vitesse_x) 
            self.vitesse = sqrt((self.vitesse_y**2) + (self.vitesse_x**2))
        elif abs(v_collision) == 3 :  #Si la collision revoie 3
            self.vitesse_x = 0
            self.vitesse_y = 1
            self.vitesse_y = copysign(self.vitesse_y, v_collision)
            self.angle = atan2(self.vitesse_y, self.vitesse_x) 
            self.vitesse = sqrt((self.vitesse_y**2) + (self.vitesse_x**2))
        elif abs(v_collision) == 4 :  #Si la collision revoie 4
            self.vitesse_x = 0.5
            self.vitesse_y = 1
            self.vitesse_y = copysign(self.vitesse_y, v_collision)
            self.angle = atan2(self.vitesse_y, self.vitesse_x) 
            self.vitesse = sqrt((self.vitesse_y**2) + (self.vitesse_x**2))
        elif abs(v_collision) == 5 :  #Si la collision revoie 5
            self.vitesse_x = 1
            self.vitesse_y = 0.5
            self.vitesse_y = copysign(self.vitesse_y, v_collision)
            self.angle = atan2(self.vitesse_y, self.vitesse_x) 
            self.vitesse = sqrt((self.vitesse_y**2) + (self.vitesse_x**2))

        #-----------------------------Bords de la fenêtre-----------------------------#

        elif self.y - self.rayon <= 0 : #Si la balle touche le haut, ça inverse la vitesse en ordonnée
            self.vitesse_y = -(self.vitesse_y)
            self.angle = atan2(self.vitesse_y, self.vitesse_x) 
            self.vitesse = sqrt((self.vitesse_y**2) + (self.vitesse_x**2))
            
        elif self.jeu.hauteur_fenetre() <= (self.y + self.rayon) :
            if self.jeu.niveau.ground == False :
                self.jeu.lives.removeLife()
                if self.jeu.lives.getNbLives() == 0 :
                    self.jeu.stopGame()
                else :
                    self.x = self.jeu.raquette.x
                    self.y = self.jeu.raquette.y - ((self.jeu.raquette.hauteur / 2) + self.rayon)
            else : 
                self.vitesse_y = -(self.vitesse_y)
                self.angle = atan2(self.vitesse_y, self.vitesse_x) 
                self.vitesse = sqrt((self.vitesse_y**2) + (self.vitesse_x**2))
        elif self.jeu.largeur_fenetre() <= self.x + self.rayon or self.x - self.rayon <= 0 : #Si la balle touche la droite ou la gauche, ça inverse la vitesse en abscisse
            self.vitesse_x = -(self.vitesse_x)
            self.angle = atan2(self.vitesse_y, self.vitesse_x) 
            self.vitesse = sqrt((self.vitesse_y**2) + (self.vitesse_x**2))

        #----------------------------- Briques -----------------------------#
        else :
            v_collision_tuple = self.jeu.niveau.collision(self)  #Valeur de la collision avec les briques.
            if v_collision_tuple != None : # v_collision_tuple = (vitesse, angle, normalisationPos)
                # print(f"Balle (Avant):" )
                # print(f"  Vitesse {self.vitesse} -> ({self.vitesse_x},{self.vitesse_y})" )
                # print(f"  Angle {self.angle*180/pi}" )

                self.vitesse = v_collision_tuple[0]
                # print(f"{v_collision_tuple[0]}, Angle : {v_collision_tuple[1]*180/pi}" )

                #----------------------------- calcul angle de rebond  -----------------------------#

                # http://gycham.educanet2.ch/java/Rebonds.pdf inspiré de ce Document.
                
                # vecteur perpendiculaire à la paroi : Up
                # vecteur tangent à la paroi : Ut
                # vecteur vitesse initial de la balle : Vi
                # vecteur vitesse final de la balle : Vf
                # composante de v selon Up : Vp
                # composante de v selon Ut : Vt
                
                Vi = ( cos(self.angle), sin(self.angle))
                Ut = (-sin(v_collision_tuple[1]), cos(v_collision_tuple[1]))
                Up = (cos(v_collision_tuple[1]), sin(v_collision_tuple[1]))
                Vt = (Vi[0] * Ut[0]) + (Vi[1] * Ut[1])
                Vp = (Vi[0] * Up[0]) + (Vi[1] * Up[1])
                Vf = ((Vt * Ut[0]) + ((-Vp) * Up[0]),(Vt * Ut[1]) + ((-Vp) * Up[1]) )


                # print(f'VI = {Vi}, VF = {Vf}, UP = {Up}, VP= {Vp}, UT = {Ut}, VT = {Vt}')
                self.angle = (atan2(Vf[1], Vf[0]))
                self.angle += (( random() - 0.5 ) * 2) * (3 / 180 * pi)
                # print(f"{v_collision_tuple[0]}, Angle : {v_collision_tuple[1]*180/pi}" )

                self.speedCoords()
                # print(f"Balle (Après):" )
                # print(f"  Vitesse {self.vitesse} -> ({self.vitesse_x},{self.vitesse_y})" )
                # print(f"  Angle {self.angle*180/pi}" )

        self.setNewPosition()


    def limitPosition_x(self, x) :
        '''
            Fonction définissant la limite des coordonnées en abscisse de la Balle.
        '''
        r_position = x
        if x > self.jeu.largeur_fenetre() - self.rayon :
            r_position = self.jeu.largeur_fenetre() - self.rayon
        if x < self.rayon  :
            r_position = self.rayon 
        return r_position

    def limitPosition_y(self, y) :
        '''
            Fonction définissant la limite des coordonnées en ordonné de la Balle.
        '''
        r_position = y
        if y > self.jeu.largeur_fenetre() - self.rayon :
            r_position = self.jeu.largeur_fenetre() - self.rayon
        if y < self.rayon :
            r_position = self.rayon
        return r_position

    def setPosition_x(self, x) :
        '''
            Fonction visant à définir les coordonnées en abscisse de la Balle.
        '''
        self.x = self.limitPosition_x(x)

    def setPosition_y(self, y) :
        '''
            Fonction visant à définir les coordonnées en ordonné de la Balle.
        '''
        self.y = self.limitPosition_y(y)

    def reset (self) :
        '''
            Fonction réinitialisant tout les paramètres de la Balle.
        '''
        self.x = self.jeu.hauteur_fenetre() / 2 #Position x du Centre
        self.y = self.jeu.raquette.y - self.jeu.raquette.hauteur - self.rayon #Position y du Centre
        self.vitesse = 2
        self.angle = pi / 2
        self.speedCoords()

    def speedCoords (self) :
        '''
            Fonction définissant la vitesse en ordonné/abscisse de la Balle.
        '''
        self.vitesse_x = cos(self.angle) * self.vitesse
        self.vitesse_y = sin(self.angle) * self.vitesse

    def setNewPosition (self) :
        '''
            fonction redéfinissant les coordonnées de la Balle.
        '''
        self.setPosition_x(self.x + self.vitesse_x)
        self.setPosition_y(self.y - self.vitesse_y)
        # print(f'X : {self.x}, Y : {self.y}')