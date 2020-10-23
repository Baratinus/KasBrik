from balle import Balle

class Brique : 


    '''
        classe Brique visant à créer l'objet Brique pour le jeu 'casse Brique'.
    '''

    def __init__ (self, jeu, coords_x, coords_y, width, height, brick_type) :

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
        self.jeu = jeu
        self.largeur = width
        self.hauteur = height

        # Decode le Type de la brique
        self.color_type = brick_type[0]
        if self.color_type != '-' :
            self.hit_type = brick_type[-1]
            self.text_tag = -1

            # Defini la couleur de la brique et son contour
            self.color_fill = ''
            self.color_outline = ''
            self.color_outline_type = ''
            self.set_color()
            
            # Defini la 'dureté' de la brique
            self.hit_points = -1 # La brique est cassée
            self.dash_type = None
            
            if self.color_type != '-' :
                self.hit_points = int(self.hit_type)
            
            if self.hit_points == 0 :
                self.dash_type = (5,3)
                self.color_outline = '#000000'

            # Update à True seulement si une animation est en cours
            # Par exemple, Brique touchée
            # Dans ce cas, un appel au paint() est pris en compte, sinon non
            self.update = True

            self.x = coords_x
            self.y = coords_y
            self.graphics = self._dessiner()

    def _dessiner (self) :
        r_tag = self.jeu.canevas.create_rectangle(self.x - self.largeur / 2, self.y - self.hauteur / 2, self.x + self.largeur / 2, self.y + self.hauteur / 2, fill = self.color_fill,outline = self.color_outline, width= (self.hit_points + 1 ), dash = self.dash_type)
        self.update_text()
        return r_tag

    def paint (self) :  #Appelée depuis l'extèrieur
        if self.update == True :
           self.update_text()
           self.update = False

    def deleteFromCanvas (self) :
        self.jeu.canevas.delete(self.graphics)
        if self.text_tag != -1 :
            self.jeu.canevas.delete(self.text_tag)
            self.text_tag = -1
        

    def limitPosition_x(self, x) :
        r_position = x
        if x > self.jeu.largeur_fenetre - self.largeur / 2 :
            r_position = self.jeu.largeur_fenetre - self.largeur / 2
        if x < self.largeur / 2 :
            r_position = self.largeur / 2
        return r_position

    def limitPosition_y(self, y) :
        r_position = y
        if y > self.jeu.largeur_fenetre - self.largeur / 2 :
            r_position = self.jeu.largeur_fenetre - self.largeur / 2
        if y < self.largeur / 2 :
            r_position = self.largeur / 2
        return r_position

    def setPosition_x(self, x) :
        self.x = self.limitPosition_x(x)

    def setPosition_y(self, y) :
        self.y = self.limitPosition_y(y)

    def collision (self, balle) -> int :
        r_collision = 0
        
        # Does the ball touch the brick ?
        if balle.x > self.x - self.largeur / 2 - balle.rayon and balle.x < self.x + self.largeur / 2 + balle.rayon :
            if balle.y > self.y - self.hauteur / 2 - balle.rayon and balle.y <= self.y + self.hauteur / 2 :
                r_collision = 1 + 5 / (self.largeur + 2 * balle.rayon) * (balle.x - self.x + self.largeur / 2 + balle.rayon)
            elif balle.y < self.y + self.hauteur / 2 + balle.rayon and balle.y >= self.y - self.hauteur / 2 :
                r_collision = (-(1 + 5 / (self.largeur + 2 * balle.rayon) * (balle.x - self.x + self.largeur / 2 + balle.rayon)))

        if r_collision != 0 and self.hit_points > 0 :
            self.update = True

            if self.hit_points - 1 == 0 :
                self.hit_points = -1 # Brique est détruite
            else :
                self.hit_points -= 1

        return int(r_collision)

    def set_color (self) :
        self.color_fill = '#000000'
        self.color_outline = '#A0A0A0'

        if self.color_type == 'R' :
            self.color_fill = '#FF0000'
            self.color_outline = '#FFA0A0'
        elif self.color_type == 'V' :
            self.color_fill = '#00FF00'
            self.color_outline = '#A0FFA0'
        elif self.color_type == 'B' :
            self.color_fill = '#0000FF'
            self.color_outline = '#A0A0FF'

    def update_text (self) :
        if self.hit_points > 1 :
            if self.text_tag != -1 :
                self.jeu.canevas.delete(self.text_tag)
            self.text_tag = self.jeu.canevas.create_text(self.x, self.y, text = str(self.hit_points))
        elif self.text_tag != -1 :
            self.jeu.canevas.delete(self.text_tag)
            self.text_tag = -1

    def getColorType (self) :
        return self.color_type
        
    def speedy (self, x) :
        return (1+x**2)