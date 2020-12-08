# Import des Librairies nécessaires, et des classes d'autres fichiers.
from tkinter import PhotoImage # Pour la gestion de l'image des Vies.

class Lives :  
    '''
        Classe permettant la gestion des vies dans le Jeu.
    '''
    def __init__ (self, i_jeu, i_nb_lives, i_x, i_y ) :
        '''
            Définition des variables du constructeur.
        '''

        self.jeu = i_jeu # Recupération des données de la classe Jeu.
        self.init_lives = i_nb_lives # Définit l'attribut initialiser vies entrée dans le constructeur (Qui ne sera pas modifié au long du programme).
        self.nb_lives = i_nb_lives # Définit l'attribut nombre de vie entrée dans le constructeur (Qui peut-être modifié tout au long du programme).
        self.x = i_x # Définit l'attribut x des abscisse pour la position du canvas des vies entrées dans le constructeur.
        self.y = i_y  # Définit l'attribut y des ordonées pour la position du canvas des vies entrées dans le constructeur.
        self.text_tag = -1 # Définit par défaut la nombre de vie.
        self.image = PhotoImage(file = "_lives_icon.gif") # Définit et attribut une image au canvas des  vies.
        self.reset() # Réinitialise les vies.
        self.graphics = self._dessiner() # Initie self.graphics avec la méthode locale _dessiner

    def _dessiner (self) :
        '''
            Fonction visant à dessiner le Canvas des vies avec une image.
        '''
        self.jeu.canevas.create_image(self.x, self.y, image=self.image) # Initie le dessin aux coordonnées et avec une image.
        return self.update_text() # Mets à jour le texte du canevas.

    def paint(self) :
        '''
            Fonction visant à redessiner le canvas si self.update est à l'état True. 
        '''
        if self.update == True : # Si self.update à True :
            self.update_text() # On mets a jour le nombre de vies.
            self.update = False # Repasse l'état de mise à jour à False.

    def addLife (self) :
        '''
            Fonction visant à ajouter une vie.
        '''
        self.nb_lives += 1 # Ajoute 1 au nombre de vies.
        self.update = True # Active la mise à jour du texte.


    def removeLife (self) :
        '''
            Fonction visant à retirer une vie.
        '''
        if self.nb_lives > 0 : # Si le nombre de vie est strictement supèrieur à 0 : 
            self.nb_lives -= 1 # On retire 1 au nombre de vies.
            self.update = True # Active la mise à jour du texte.


    def getNbLives (self) :
        '''
            Fonction visant à retourner le nombre de vies restantes.
        '''
        return self.nb_lives # retourne le nombre de vies restantes.

    def update_text (self) :
        '''
            Fonction visant à mettre à jour le texte (du nombre de vies).
        '''
        if self.nb_lives > 0 : # Si le nombre de vies est strictement supèrieur à 0 :
            if self.text_tag != -1 : # Si le tag du texte est resté inchangé :
                self.jeu.canevas.delete(self.text_tag) # On suprime le texte.
            self.text_tag = self.jeu.canevas.create_text(self.x, self.y, text = str(self.nb_lives) ) # Et on en recré un avec le nombre de vie restant.
        else : # Sinon :
            if self.text_tag != -1 :  # Si le tag du texte est resté inchangé :
                self.jeu.canevas.delete(self.text_tag) # On suprime le texte.
            self.text_tag = self.jeu.canevas.create_text(self.x, self.y, text = "/" ) # Et on en recré un avec un 'slash' ("/").
        return self.text_tag # On retourne le tag du texte.

    def reset (self) :
        '''
            Fonction visant à réinitialiser le nombre de vies et à mettre à jour le canevas.
        '''
        self.nb_lives = self.init_lives # Remise a la valeur par défaut du nombre de vies.
        self.update = True # Passage de l'état de mise à jour à True.