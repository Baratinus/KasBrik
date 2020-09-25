from jeu import Jeu
import tkinter as tk
import time

WIDTH_SCREEN = 600
HEIGHT_SCREEN = 600

fen = tk.Tk()

fen.config(width=WIDTH_SCREEN,height=HEIGHT_SCREEN)
fen.title('Jeu')

jeu = Jeu(fen)

while 1:
    # détection si une touche a été apuyée
    # fen.bind("<keyPressed>")
    fen.update_idletasks() # met à jour les tâches de la fenêtre
    fen.update() #met à jour la fenêtre
    time.sleep(0.01)