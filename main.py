from jeu import Jeu
import tkinter as tk
import time

WIDTH_SCREEN = 600
HEIGHT_SCREEN = 600

def close_window():
  global running
  running = False
  print ("Game closed")

fen = tk.Tk()
fen.protocol("WM_DELETE_WINDOW", close_window)

running = True
fen.config(width=WIDTH_SCREEN,height=HEIGHT_SCREEN)
fen.resizable(width=False, height=False)
fen.title('Jeu')

jeu = Jeu(fen)

while running :

    if not running: 
        break

    # détection si une touche a été apuyée
    # fen.bind("<keyPressed>")


    # mise à jour du jeu
    jeu.miseAJour()

    fen.update_idletasks() # met à jour les tâches de la fenêtre
    fen.update() #met à jour la fenêtre
    time.sleep(0.01)