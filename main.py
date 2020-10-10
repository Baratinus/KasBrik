from jeu import Jeu
import tkinter as tk
import time

LARGEUR_FENETRE = 600
HAUTEUR_FENETRE = 600

def close_window():
  global running
  running = False
  print ("Game closed")

fen = tk.Tk()
fen.protocol("WM_DELETE_WINDOW", close_window)

running = True
fen.config(width=LARGEUR_FENETRE,height=HAUTEUR_FENETRE)
fen.resizable(width=False, height=False)
fen.title('Jeu')

jeu = Jeu(fen, LARGEUR_FENETRE, HAUTEUR_FENETRE)

while running :

    if not running: 
        break

    # détection si une touche est apuyée
    fen.bind("<KeyPress>", jeu.toucheAppuyee)
    fen.bind("<KeyRelease>", jeu.toucheRelachee)

    # mise à jour du jeu
    jeu.miseAJour()

    fen.update_idletasks() # met à jour les tâches de la fenêtre
    fen.update() #met à jour la fenêtre
    time.sleep(0.01)