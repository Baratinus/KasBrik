# Import des Librairies nécessaires, et des classes d'autres fichiers.
from balle import Balle # Pour la gestion de la Balle dans Brique.
from math import atan2,pi,tan # Import du module math et des différentes fonctions pour la gestion des collisions.

class Brique : 
    '''
        classe Brique visant à créer l'objet Brique pour le jeu 'casse Brique'.
    '''

    def __init__ (self, i_jeu, i_coords_x, i_coords_y, i_width, i_height, i_brick_type) :
        '''
            Fonction d'initialisation avec comme paramètre self et jeu.
            
            Types de briques :
            ------------------
            '-' : Pas de brique
            '0' : Incassable
            '1' : Brique qui se casse en une fois.
            '2' : Brique qui se casse en 2 fois.
            '3' : Brique qui se casse en 3 fois.

            Couleurs des briques :
            ----------------------
            'R' : Brique simple, Rouge encore 
            'G' : Brique simple, Verte
            'B' : Brique simple, Bleue

            Ex : 'R2' == Une brique rouge qui se casse en 2 fois.
        '''
        self.jeu = i_jeu # Recupération des données de la classe Jeu.
        self.largeur = i_width # Définition de la largeur de la brique. 
        self.hauteur = i_height # Définition de la hauteur de la brique.

        # Decode le Type de la brique.
        self.color_type = i_brick_type[0] # La couleur est définie par le premier caractère de la chaîne de caractère : self.i_brick_type
        if self.color_type != '-' : # Si la couleur est différente de ('-'), Alors :
            self.hit_type = i_brick_type[-1] # le nombre de vies de la Brique est le dernier caractère de la chaîne de caractère.
            self.text_tag = -1 # Son tag vaut -1.

            # Defini la couleur de la brique et son contour.
            self.color_fill = ''
            self.color_outline = ''
            self.color_outline_type = ''
            self.set_color()
            
            # Defini la 'dureté' de la brique.
            self.hit_points = -1 # La brique est cassée.
            self.dash_type = None # Si la brique est incassable.
            
            if self.color_type != '-' :
                self.hit_points = int(self.hit_type)
            
            if self.hit_points == 0 :
                self.dash_type = (5,3)
                self.color_outline = '#000000'

            # Update à True seulement si une animation est en cours.
            # Par exemple, Brique touchée.
            # Dans ce cas, un appel au paint() est pris en compte, sinon non.
            self.update = True

            self.x = i_coords_x # Récuperation des coordonnées entrés en abscisse de la Brique.
            self.y = i_coords_y # Récuperation des coordonnées entrés en ordonné de la Brique.
            self.graphics = self._dessiner() # Initie self.graphics avec la méthode locale _dessiner .

    def _dessiner (self) :
        '''
            Fonction qui permets de dessiner la Brique.
        '''
        r_tag = self.jeu.canevas.create_rectangle(self.x - self.largeur / 2, self.y - self.hauteur / 2, self.x + self.largeur / 2, self.y + self.hauteur / 2, fill = self.color_fill,outline = self.color_outline, width= (self.hit_points + 1 ), dash = self.dash_type)
        self.update_text()
        return r_tag

    def paint (self) :
        '''
            Fonction appelée depuis l'extèrieur visant à mettre a jour le texte (le nombre de vie de la Brique /) du canevas de la Brique.
        '''
        if self.update == True :
           self.update_text()
           self.update = False

    def deleteFromCanvas (self) :
        '''
            Fonction visant à détruire la Brique du canevas.
        '''
        self.jeu.canevas.delete(self.graphics)
        if self.text_tag != -1 :
            self.jeu.canevas.delete(self.text_tag)
            self.text_tag = -1
        

    def limitPosition_x(self, x) :
        '''
            Fonction visant limiter la position de la brique en abscisse.
        '''
        r_position = x
        if x > self.jeu.largeur_fenetre - self.largeur / 2 :
            r_position = self.jeu.largeur_fenetre - self.largeur / 2
        if x < self.largeur / 2 :
            r_position = self.largeur / 2
        return r_position

    def limitPosition_y(self, y) :
        '''
            Fonction visant limiter la position de la brique en ordonné.
        '''
        r_position = y
        if y > self.jeu.largeur_fenetre - self.largeur / 2 :
            r_position = self.jeu.largeur_fenetre - self.largeur / 2
        if y < self.largeur / 2 :
            r_position = self.largeur / 2
        return r_position

    def setPosition_x(self, x) :
        '''
            Fonction pour placer la brique dans la fenêtre en abscisse.
        '''
        self.x = self.limitPosition_x(x)

    def setPosition_y(self, y) :
        '''
            Fonction pour placer la brique dans la fenêtre en ordonné.
        '''
        self.y = self.limitPosition_y(y)

    def collision (self, balle) -> tuple :
        '''
            Fonction gèrant la collision de la balle contre la Brique.
        '''
        angle = 0
        vitesse = 0
        touch = False
        r_tuple = None

        angleQuadrantBall  = atan2((self.y - balle.y ), (balle.x - self.x))
        angleQuadrantBrick = atan2(self.hauteur, self.largeur)
        if angleQuadrantBall < 0 :
            angleQuadrantBall += 2 * pi

        if angleQuadrantBall > (2*pi - angleQuadrantBrick) :
            if balle.x <= self.x + self.largeur / 2 + balle.rayon :
                balle.x = self.x + (self.largeur/2) + balle.rayon 
                angle = 0
                posOfCollision = (self.largeur / 2 + balle.rayon) * tan(angleQuadrantBall)
                normalisationPos = posOfCollision / (self.hauteur / 2)
                vitesse = self.speed(normalisationPos)
                # print('Est')#,angle, posOfCollision, normalisationPos, vitesse)
                touch = True
        elif angleQuadrantBall <= angleQuadrantBrick :
            if balle.x <= self.x + self.largeur / 2 + balle.rayon :
                balle.x = self.x + (self.largeur/2) + balle.rayon 
                angle = 0
                posOfCollision = (self.largeur / 2 + balle.rayon) * tan(angleQuadrantBall)
                normalisationPos = posOfCollision / (self.hauteur / 2)
                vitesse = self.speed(normalisationPos)
                # print('Est')#,angle, posOfCollision, normalisationPos, vitesse)
                touch = True
        elif angleQuadrantBall > angleQuadrantBrick and angleQuadrantBall < (pi - angleQuadrantBrick) :
            if balle.y >= self.y - self.hauteur / 2 - balle.rayon :
                balle.y = self.y - (self.hauteur/2) - balle.rayon  
                angle = (pi/2)
                posOfCollision = (self.hauteur / 2 + balle.rayon) / tan(angleQuadrantBall)
                normalisationPos = posOfCollision / (self.largeur / 2)
                vitesse = self.speed(normalisationPos)
                # print('Nord')#,angle, posOfCollision, normalisationPos, vitesse)
                touch = True
        elif angleQuadrantBall > (pi - angleQuadrantBrick) and angleQuadrantBall < (pi + angleQuadrantBrick) :
            if balle.x >= self.x - self.largeur / 2 - balle.rayon :
                balle.x = self.x - (self.largeur/2) - balle.rayon 
                angle = pi
                posOfCollision = -(self.largeur / 2 + balle.rayon) * tan(angleQuadrantBall)
                normalisationPos = posOfCollision / (self.hauteur / 2)
                vitesse = self.speed(normalisationPos)
                # print('Ouest')#,angle, posOfCollision, normalisationPos, vitesse)
                touch = True
        else :
            if balle.y <= self.y + self.hauteur / 2 + balle.rayon:
                balle.y = self.y + (self.hauteur/2) + balle.rayon 
                angle = 3*(pi/2)
                posOfCollision = -(self.hauteur / 2 + balle.rayon) / tan(angleQuadrantBall)
                normalisationPos = posOfCollision / (self.largeur / 2)
                vitesse = self.speed(normalisationPos)
                # print('Sud')#,angle, posOfCollision, normalisationPos, vitesse)
                touch = True
        
        if touch :
            r_tuple = (vitesse, angle, normalisationPos)

            if self.hit_points > 0 : # Si la brisque est destructible, il faut mettre à jour l'affichage
                self.update = True
                if self.hit_points - 1 == 0 :
                    self.hit_points = -1 # Brique est détruite
                else :
                    self.hit_points -= 1
    
        return r_tuple

    def set_color (self) :
        '''
            Fonction pour déterminer la couleur de la Brique.
        '''
        self.color_fill = '#000000'
        self.color_outline = '#A0A0A0'

        if self.color_type == 'R' : # Rouge.
            self.color_fill = '#FF0000'
            self.color_outline = '#FFA0A0'
        elif self.color_type == 'V' : # Vert.
            self.color_fill = '#00FF00'
            self.color_outline = '#A0FFA0'
        elif self.color_type == 'B' : # Bleue.
            self.color_fill = '#0000FF'
            self.color_outline = '#A0A0FF'

    def update_text (self) :
        '''
            Fonction visant à mettre à jour le texte de vie de la Brique.
        '''
        if self.hit_points > 1 :
            if self.text_tag != -1 :
                self.jeu.canevas.delete(self.text_tag)
            self.text_tag = self.jeu.canevas.create_text(self.x, self.y, text = str(self.hit_points))
        elif self.text_tag != -1 :
            self.jeu.canevas.delete(self.text_tag)
            self.text_tag = -1

    def getColorType (self) :
        '''
            Fonction renvoyant la couleur de la Brique.
        '''
        return self.color_type
        
    def speed (self, x) :
        '''
            Fonction visant à retourner la valeur de la vitesse de la Balle lors d'une collision avec une Brique.
        '''
        return (1+x**2)