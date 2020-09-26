class Raquette :

    '''
        classe Raquette visant a créer l'objet Raquette pour le jeu 'casse Brique'.
    '''

    def __init__ (self, jeu) :

        '''
            Fonction d'initialisation avec comme paramètre self et jeu.
        '''

        self.jeu = jeu
<<<<<<< Updated upstream
        self.x = (self.jeu(largeur_fenetre)) / 2
        self.y = (self.jeu(hauteur_fenetre)) / 8
        self.largeur = 45
        self.hauteur = 20
        self.vitesse = 15
        self.image = self.jeu.canvas.

=======
        self.largeur = 45
        self.hauteur = 20
        self.vitesse = 15
        self.x = (jeu.largeur_fenetre / 2) - (self.largeur / 2)
        self.y = jeu.hauteur_fenetre - jeu.hauteur_fenetre / 8
        self.image = self._dessiner()

    def _dessiner (self) :
        
        return self.jeu.canevas.create_rectangle(self.x, self.y, self.x + self.largeur, self.y + self.hauteur, fill = "red")
>>>>>>> Stashed changes


    def aller_Droite (self) :

        

    def aller_Gauche (self) :


    def collision (self, x) :



