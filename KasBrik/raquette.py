class Raquette :

    '''
        classe Raquette visant a créer l'objet Raquette pour le jeu 'casse Brique'.
    '''

    def __init__ (self, jeu) :

        '''
            Fonction d'initialisation avec comme paramètre self et jeu.
        '''

        self.jeu = jeu
        self.largeur = 45
        self.hauteur = 20
        self.vitesse = 15
        self.x = (jeu.largeur_fenetre / 2) - (self.largeur / 2)
        self.y = jeu.hauteur_fenetre - jeu.hauteur_fenetre / 8
        self.image = self._dessiner()
        self.valeur_collision = 0

    def _dessiner (self) :
        
        return self.jeu.canevas.create_rectangle(self.x, self.y, self.x + self.largeur, self.y + self.hauteur, fill = "red")



    def aller_Droite (self) :

        pass

    def aller_Gauche (self) :

        pass

    def collision (self, x) :

        pass


