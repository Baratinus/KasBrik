from jeu import Jeu
import tkinter as tk

WIDTH_SCREEN = 600
HEIGHT_SCREEN = 600



def close_window():
  jeu.stopGame()
  print ("Game closed")
  fen.destroy()

fen = tk.Tk()
fen.protocol("WM_DELETE_WINDOW", close_window)

running = True
fen.config(width=WIDTH_SCREEN,height=HEIGHT_SCREEN)
fen.resizable(width=False, height=False)
fen.title('Jeu')
fen.update()

jeu = Jeu(fen)
jeu.startGame()

fen.mainloop()
