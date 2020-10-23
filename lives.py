from tkinter import PhotoImage
class Lives :  

    def __init__ (self, i_jeu, i_nb_lives, i_x, i_y ) :

        self.jeu = i_jeu
        self.init_lives = i_nb_lives
        self.nb_lives = i_nb_lives
        self.x = i_x
        self.y = i_y
        self.text_tag = -1
        self.image = PhotoImage(file = "_lives_icon.gif")
        self.reset()
        self.graphics = self._dessiner()

    def _dessiner (self) :
        self.jeu.canevas.create_image(self.x, self.y, image=self.image)
        return self.update_text()

    def paint(self) :
        if self.update == True :
            self.update_text()
            self.update = False

    def addLife (self) :
        self.nb_lives += 1
        self.update = True


    def removeLife (self) :
        if self.nb_lives > 0 : 
            self.nb_lives -= 1
            self.update = True


    def getNbLives (self) :
        return self.nb_lives

    def update_text (self) :
        if self.nb_lives > 0 :
            if self.text_tag != -1 :
                self.jeu.canevas.delete(self.text_tag)
            self.text_tag = self.jeu.canevas.create_text(self.x, self.y, text = str(self.nb_lives) )
        else :
            if self.text_tag != -1 :
                self.jeu.canevas.delete(self.text_tag)
            self.text_tag = self.jeu.canevas.create_text(self.x, self.y, text = "/" )
        return self.text_tag

    def reset (self) :

        self.nb_lives = self.init_lives
        self.update = True

