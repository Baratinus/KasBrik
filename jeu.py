# Import des Librairies nécessaires, et des classes d'autres fichiers.
from pynput.mouse import Controller # Pour la gestion des évênements Souris.
from balle import Balle # Pour la gestion de la Balle dans Jeu.
from raquette import Raquette # Pour la gestion de la Raquette dans Jeu.
from level import Level # Pour la gestion du Niveau dans Jeu.
from lives import Lives # Pour la gestion des Vies dans Jeu.
from time import sleep #Pour la gestion du temps de pause du jeu.
import tkinter as tk # Pour le bon fonctionnement de la Ffnêtre du jeu.


class Jeu:
    '''
        Classe pour gérer l'ensemble des intéractions avec le jeu.
    '''
    def __init__(self,i_fenetre):
        '''
            Définition des variables du constructeur.
        '''

        self.fenetre = i_fenetre # Stocke les paramètres de la fenêtre.
        self.canevas = tk.Canvas(self.fenetre, width = self.largeur_fenetre(), height = self.hauteur_fenetre()) # Crée un canvas ( Support de tout les éléments d'affichage. )
        self.canevas.place(x = 0, y = 0) # Place le Canvas

        self.raquette = Raquette(self) # Crée une instance de Raquette.
        self.balle = Balle(self) # Crée une instance de Balle.
        self.level_id = -1 # Numéro du niveau à charger.
        self.niveau = Level(self, self.level_id) # Crée une instance du Niveau .
        self.lives = Lives(self, 3, self.largeur_fenetre() / 16 , (self.hauteur_fenetre() * 15) / 16) # Crée une instance des Vies.

        self.touche_possible = ["q", "d", "Q", "D"] # Liste des touches qui seront utilisées pour jouer.
        self.touche_options = ['plus','minus','slash'] # Liste des touches qui seront utilisées pour les options du jeu (Augmenter le taux de rafraîchissement : +, le Diminuer : -, Mettre en place un sol : / ). 

        # Capture les événements de la souris.
        self.canevas.bind("<Motion>", self.moved) # Coordonnées du curseur de la souris en abscisse.
        self.canevas.bind("<Button-3>", self.rightClick) # Si le click droit a été activé.
        self.canevas.bind("<Leave>", self.leave) # Si la souris a quitté le périmètre de la fenêtre.
        self.canevas.bind("<Enter>", self.enter) # Si la souris est entrée le périmètre de la fenêtre.
        
        # Capture les événements du clavier.
        self.fenetre.bind("<KeyPress>", self.checkKeyPressed) # Active la capture des touches du clavier dans la fenêtre.
        self.resetGame() # Initialise tout les objets avec leurs paramètres par défaut.

    def largeur_fenetre (self) -> int :
        '''
            Fonction qui retourne la valeur de la largeur de la fenêtre.
        '''

        return self.fenetre.winfo_width() # Retourne la largeur définie dans main.py


    def hauteur_fenetre (self) -> int :
        '''
            Fonction qui retourne la valeur de la hauteur de la fenêtre.
        '''

        return self.fenetre.winfo_height() # Retourne la heuteur définie dans main.py

    def checkKeyPressed(self, event) :
        '''
            Fonction qui vérifie si une touche à été préssée, et si elle est prise en compte par le programme.
        '''
        # print(f"Touche : {event.keysym}") #Affiche toutes les touches préssés. 
        if event.keysym == "Escape" : # Si la touche préssée est 'Echap' alors ,
            self.stopGame() #Le jeu s'arrête (Sortie de la boucle while -> infini)
        if event.keysym in self.touche_possible  : # Si la touche préssée est dans la liste de celles possibles pour le jeu.
            if event.keysym == "q" or event.keysym == "Q" : # Si la touche préssée est la touche 'q' ou 'Q' (dans le cas d'un clavier en mode MAJS )
                self.raquette.goLeft()  # Apelle la fonction qui permet de déplacer la Raquette vers la Gauche.
            elif event.keysym == "d" or event.keysym == "D" : # Si la touche préssée est la touche 'd' ou 'D' (dans le cas d'un clavier en mode MAJS )
                self.raquette.goRight() # Apelle la fonction qui permet de déplacer la Raquette vers la Droite.
        if event.keysym in self.touche_options : # Si la touche préssée est dans la liste de celles possibles pour les options.
            if event.keysym == "plus" : # Si la touche préssée est la touche '+'
                self.time_sleep /= 2 # Le taux de rafraîchissement de la fenêtre est augmenté (temps de pause diminué).
                print("Taux de Rafraîchissement : Augmenté") # Message qui s'affiche au passage dans la condition.
            elif event.keysym == "minus" : # Si la touche préssée est la touche '-'
                self.time_sleep *= 2 # Le taux de rafraîchissement de la fenêtre est diminué (temps de pause augmenté).
                print("Taux de Rafraîchissement : Diminué") # Message qui s'affiche au passage dans la condition.
            elif event.keysym == 'slash' : # Si la touche préssée est la touche '/'
                self.niveau.ground = not self.niveau.ground # Toggle (= Basculer) le sol à True / False.
                if self.niveau.ground == True : # Si le sol est à l'état True.
                    print("Sol Activé") # Message qui s'affiche au passage dans la condition.
                else : # Sinon 
                    print("Sol Désactivé") # Message qui s'affiche si le sol est désactivé après passage dans la boucle.

    def moved(self, event):
        '''
            Fonction récupérant les coordonnées en abscisse de la souris et  les attribuants à la raquette.
        '''
        x = event.x # Capte les coordonées de la souris en abscisse.
        self.raquette.setPosition(x) # Attributs les coordonnées en abscisse de la souris captés précédement et les attributs à la Raquette.

    def enter(self, event):
        '''
            Fonction qui gère l'entrée de la souris dans la zone du canvas.
        '''
        x,y = event.x, event.y # Capture les coordonnées en abscisse, en ordonné et les stockent.
        if y > 0 and y < self.hauteur_fenetre() : # Si la souris est dans la fenêtre en hauteur alors ,
            self.raquette.setPositionEnter(x) # On demande à placer la souris au maximum de la zone du canvas en largeur.

    def leave(self, event):
        '''
            Fonction qui gère la sortie de la souris de la zone du canvas.
        '''
        x,y = event.x, event.y # Capture les coordonnées en abscisse, en ordonné et les stockent.
        if y > 0 and y < self.hauteur_fenetre() : # Si la souris est dans la fenêtre en hauteur alors , 
            self.raquette.setPositionLeave(x) # On demande à placer la souris au maximum de la zone du canvas en largeur.

    def miseAJour(self):
        '''
            Fonction mettant à jour tout les éléments susceptibles de varier // Sauf les briques (Auto gérées)
        '''
        
        self.balle.deplacer() #  Provoque le déplacement de la Balle.
        self.balle.paint() #  Actualise l'affichage de la Balle.
        self.raquette.paint() # Actualise l'affichage de la Raquette.
        self.lives.paint() # Actualise l'affichage de la Vie.

    def stopGame (self) :
        '''
            Fonction permettant d'arrêter le jeu.
        '''
        self.running = False # Sortie de la bouble infini While.
        print ("Game Stopped") # Message qui s'affiche lors de l'appel de cette fonction.

    def getStateGame (self) :
        '''
            Fonction permettant d'obtenir l'état du jeu (Pause/Running). 
        '''
        return self.running # Retourne True si le jeu est en marche, sinon, s'il est arrêté, retourne False.

    def resetGame (self) :
        '''
            Réinitialise tout les paramètres par défaut de tout les objets.
        '''
        self.raquette.reset() # Réinitialise les paramètres de la Raquette.
        self.balle.reset() # Réinitialise les paramètres de la Balle.
        self.lives.reset() # Réinitialise les paramètres de la Vie.
        self.niveau.reset() # Réinitialise les paramètres du Niveau.
        self.time_sleep = 0.01 # Réinitialise les paramètres de temps de pause du jeu.

    def rightClick (self, event):
        '''
            Fonction permettant de rédémarrer le Jeu avec un clic droit si le Jeu est en pause.
        '''
        if self.getStateGame() == False : # Si le Jeu est en pause alors ,
            self.resetGame() # L'on réinitialise tout les paramètres par défaut.
            self.startGame() # L'on rentre dans la boucle infini While.

    def startGame (self) :
        '''
            Fonction permattant de démarrer le Jeu.
        '''
        self.running = True # Passe la condition de la boucle infini While à l'état : True (l'on rentre dans la boucle).

        while self.getStateGame() : # Tant que le Jeu est à l'état True :

            self.miseAJour() # Mise à jour du jeu.
            self.fenetre.update() # Mise à jour par l'os de l'affichage.
            sleep(self.time_sleep) # Temps d'arrêt entre chaque rafraîchissement de l'écran qui est défini par : self.time_sleep .
            # print(f'time sleep {self.time_sleep}') # Message de test pour obtenir le temps de pause dans la variable : self.time_sleep . 