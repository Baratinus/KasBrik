from pynput.mouse import Controller
from balle import Balle
from raquette import Raquette
from level import Level
from lives import Lives
from time import sleep
import tkinter as tk


class Jeu:
    def __init__(self,fenetre):

        self.running = True
        self.fenetre = fenetre
        self.canevas = tk.Canvas(fenetre, width = self.largeur_fenetre(), height = self.hauteur_fenetre())
        self.canevas.place(x = 0, y = 0) #Affiche le Canvas

        self.raquette = Raquette(self)
        self.balle = Balle(self)
        self.level_id = -1
        self.niveau = Level(self, self.level_id)
        self.lives = Lives(self, 3, self.largeur_fenetre() / 8 , (self.hauteur_fenetre() * 15) / 16)

        self.touche_possible = ["q","d","Q","D"]
        self.touche_pressee = {}

        # Catch the mouse events
        self.canevas.bind("<Motion>", self.moved)
        self.canevas.bind("<Button-3>", self.leftClick)
        self.canevas.bind("<Leave>", self.leave)
        self.canevas.bind("<Enter>", self.enter)
        
        # Catch the keybord events
        self.fenetre.bind("<KeyPress>", self.checkKeyPressed)

    def largeur_fenetre (self) -> int :
        
        return self.fenetre.winfo_width()


    def hauteur_fenetre (self) -> int :

        return self.fenetre.winfo_height()

    def checkKeyPressed(self, event) :
        #print(f"Touche : {event.keysym}")
        if event.keysym == "Escape" :
            self.stopGame()
        if event.keysym in self.touche_possible  :
            if event.keysym == "q" or event.keysym == "Q" :
                self.raquette.goLeft()
            elif event.keysym == "d" or event.keysym == "D" :
                self.raquette.goRight()


    def moved(self, event):
        x = event.x
        self.raquette.setPosition(x)

    def enter(self, event):
        x,y = event.x, event.y
        if y > 0 and y < self.hauteur_fenetre() :
            self.raquette.setPositionEnter(x)

    def leave(self, event):
        x,y = event.x, event.y
        if y > 0 and y < self.hauteur_fenetre() :
            self.raquette.setPositionLeave(x)

    def miseAJour(self):
        # partie temporaire
        self.balle.deplacer()
        self.balle.paint()
        self.raquette.paint()
        self.lives.paint()

    def stopGame (self) :
        self.running = False
        print ("Game Stopped")

    def getStateGame (self) :
        return self.running

    def resetGame (self) :
        self.raquette.reset()
        self.balle.reset()
        self.lives.reset()
        self.niveau.reset()



    def leftClick (self, event):
        if self.getStateGame() == False :
            self.resetGame()
            self.startGame()

    def startGame (self) :
        self.running = True

        while self.getStateGame() :

        # mise à jour du jeu

            self.miseAJour()
            self.fenetre.update()
            sleep(0.01) 