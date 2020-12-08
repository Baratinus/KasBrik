# Import des Librairies nécessaires, et des classes d'autres fichiers.
from balle import Balle # Pour la gestion de la Balle dans Raquette.

class Raquette :
    '''
        classe Raquette visant a créer l'objet Raquette pour le jeu 'casse Brique'.
    '''

    def __init__ (self, i_jeu) :
        '''
            Fonction d'initialisation avec comme paramètre self et jeu.
        '''

        self.jeu = i_jeu # Définit l'attribut jeu entrée dans le constructeur.
        self.largeur = 45 # Définit une largeur à la Raquette.
        self.hauteur = 20 # Définit une hauteur à la Raquette.
        self.vitesse = 15 # Définit une vitesse de déplacement de la Raquette.
        self.reset() # Réinitialisation de la position de la Raquette.
        self.graphics = self._dessiner() # Initie self.graphics avec la méthode locale _dessiner .


    def _dessiner (self) : # Appellée Seulement dans la Classe.
        '''
            Fonction visant à dessiner le raquette afin de la stocker dans graphics.
        '''
        
        return self.jeu.canevas.create_rectangle(self.x - self.largeur / 2, self.y - self.hauteur / 2, self.x + self.largeur / 2, self.y + self.hauteur / 2, fill = "red") # Retourne un rectangle rouge.

    def paint (self) :  # Appellée depuis l'extèrieur.
        '''
            Fonction qui gère la mise a jour de l'affichage.
        '''
        if self.update == True : # Si une animation est en cours, alors :
            xy_coords = self.jeu.canevas.coords(self.graphics) # Récupère les coordonnées de la Raquette. x1, y1 en haut à gauche et x2, y2 en bas à droite.
            self.jeu.canevas.move(self.graphics, (self.x - self.largeur / 2) - xy_coords[0] , (self.y - self.hauteur / 2) - xy_coords[1] ) # Déplace la position de la Raquette Par rapport aux coordonnées Initiales.
            self.update = False # Passe l'état de l'animation à Inactive. (Puisqu'elle est finie)

    def limitPosition(self, x) :
        '''
            Fonction qui a pour but de garder la Raquette dans la fenêtre.
        '''
        r_position = x # Valeur qui sera retournée en abscisses (En ordonné, la raquette ne bouge pas)
        if x > self.jeu.largeur_fenetre() - self.largeur / 2 : # Si la valeur en abscisses de la Raquette est supèrieure à la largeur de la fenêtre moins la moitiée de la sienne , alors :
            r_position = self.jeu.largeur_fenetre() - self.largeur / 2 # La valeur qui sera retournée est la valeur maximale que la Raquette peut atteindre sans dépacer le bord de la fenêtre à Droite.
        if x < self.largeur / 2 : # Si la valeur en abscisses de la Raquette est infèrieure à sa propre moitiée.
            r_position = self.largeur / 2 # La valeur qui sera retourné est la valeur maximale que la Raquette peutatteindre au bord de la fenêtre Gauche. 
        return r_position # Retourne la valeur de x.

    def setPosition(self, x) :
        '''
            Fonction visant à définir les coordonnées en abscisse de la Raquette.
        '''
        self.x = self.limitPosition(x) # Définit les coordonnées
        self.update = True # Passe l'état de l'animation à Active.

    def setPositionEnter(self, x) :
        '''
            Fonction permettant de maintenir la Raquette à sa position lors de l'entré de la souris de la fenêtre de jeu.
        '''
        x_position = -1 # Définition de la valeur par défaut.
        if x > self.jeu.largeur_fenetre() / 2 : # Si la valeur en abscisse de la souris est supèrieure à la moitié de la largeur de la fenêtre alors :
            x_position = self.jeu.largeur_fenetre() # la position de la raquette est défini comme étant le bord de la fenêtre Droite.
        else : # Sinon :
            x_position = 0 # la position de la raquette est défini comme étant le bord de la fenêtre Gauche.
        self.setPosition(x_position) # Définit les coordonnées en abscise de la raquette aux coordonnée 'x_position'.

    def setPositionLeave(self, x) :
        '''
            Fonction permettant de maintenir la Raquette à sa position lors de la sortie de la souris de la fenêtre de jeu.
        '''
        x_position = -1 # Définition de la valeur par défaut.
        if x > self.jeu.largeur_fenetre() / 2 :  # Si la valeur en abscisse de la souris est supèrieure à la moitié de la largeur de la fenêtre alors :
            x_position = self.jeu.largeur_fenetre() # la position de la raquette est défini comme étant le bord de la fenêtre Droite.
        else : # Sinon :
            x_position = 0 # la position de la raquette est défini comme étant le bord de la fenêtre Gauche.
        self.setPosition(x_position) # Définit les coordonnées en abscise de la raquette aux coordonnée 'x_position'.

    def goRight (self) :
        '''
            Fonction visant a se faire déplacer la Raquette vers la Droite.
        '''
        self.setPosition(self.x + self.vitesse) # Défini les nouvelles coordonnées de la Raquette en additionnant ses coordonnées et sa vitesse (en pixels).

    def goLeft (self) :
        '''
            Fonction visant a se faire déplacer la Raquette vers la Gauche.
        '''
        self.setPosition(self.x - self.vitesse) # Défini les nouvelles coordonnées de la Raquette en soutrayant sa vitesse (en pixels) de ses coordonnés en abscisse actuels.

    def collision (self, balle) -> int :
        '''
            Fonction visant retourner une valeur de collision à la Balle sur la Raquette. Ex : [12345] <-- Raquette et ses valeurs de collision.
        '''
        r_collison = 0 # Valeur par défaut de la valeur de retour.
        
        # La Balle a-t-elle touchée la Raquette ?
        if balle.x > self.x - self.largeur / 2 - balle.rayon and balle.x < self.x + self.largeur / 2 + balle.rayon : # Si les coordonnées en abscisse de la Balle (intervalle) sont comprise dans celle de la Raquette (intervalle), Alors :
            if balle.y > self.y - self.hauteur / 2 - balle.rayon and balle.y <= self.y + self.hauteur / 2 : # Si la Balle arrive par le dessus de la Raquette, Alors :
                r_collison = 1 + 5 / (self.largeur + 2 * balle.rayon) * (balle.x - self.x + self.largeur / 2 + balle.rayon) # La valeur de collision est défini entre [1;5] suivant les différentes valeurs.
            elif balle.y < self.y + self.hauteur / 2 + balle.rayon and balle.y >= self.y - self.hauteur / 2 : # Si la Balle arrive par le dessous de la Raquette, Alors :
                r_collison = (-(1 + 5 / (self.largeur + 2 * balle.rayon) * (balle.x - self.x + self.largeur / 2 + balle.rayon))) # La valeur de collision est défini entre [1;5] suivant les différentes valeurs.
        return int(r_collison) # Retour de la valeure de Collision. [1;5]

    def reset (self) :
        '''
            Fonction permettant de réinitialiser les coordonnées de la raquette.
        '''

        self.x = self.jeu.largeur_fenetre() / 2 # Définit les coordonnées en abscisse de la raquette à la moitié de sa largeur.
        self.y = self.jeu.hauteur_fenetre() - self.jeu.hauteur_fenetre() / 8 # Définit les coordonnées en ordonné de la raquette à 1/8ème de sa hauteur.
        self.update = True # Update à True seulement si une animation est en cours. Dans ce cas, un appel au paint() est pris en compte, sinon non