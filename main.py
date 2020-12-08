# Import des Librairies nécessaires, et des classes d'autres fichiers.
from jeu import Jeu # Pour la gestion du Jeu.
import tkinter as tk # Pour la gestion de Fenêtres.

WIDTH_SCREEN = 600 # Paramétrage de la hauteur de la fenêtre.
HEIGHT_SCREEN = 600 # Paramétrage de la Longeur de la fenêtre.


def close_window():
  '''
      Fonction pour fermer la fenêtre du jeu.  
  '''
  jeu.stopGame() # Ferme les processus en cours (sortie de la boucle infinie(While).
  print ("Game closed") 
  fen.destroy() # Ferme la fenêtre affichée sur l'écran.
 
fen = tk.Tk() # Ouvre une instance de Tkinter sur fen.
fen.protocol("WM_DELETE_WINDOW", close_window) # Fonction appelée lors d'un clic sur la croix de la fenêtre.

fen.config(width=WIDTH_SCREEN,height=HEIGHT_SCREEN) # Initialise la taille de la fenêtre.
fen.resizable(width=False, height=False) # Interdit le redimensionnement de la fenêtre en hauteur et en largeur.
fen.title('Casse Brique') # Définit un titre à la fenêtre.
fen.update() # Demande à l'os de rafraîchir le fenêtre. 

jeu = Jeu(fen) # Crée une instance de Jeu dans la fenêtre.
jeu.startGame() # Démarre la boucle infinie (While) qui permet de rafraîchir tout les eléments du jeu, elle s'éxécute tant que la variable running est à l'état : True.
fen.mainloop() # Maintient la fenêtre ouverte (gestion des évênements clavier même lorsque le jeu est mis en pause(sortie de la boucle infinie)).