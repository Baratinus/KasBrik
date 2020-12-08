# Import des Librairies nécessaires, et des classes d'autres fichiers.
from brique import Brique # Pour la gestion des Briques dans le niveau (level).

class Level : 


    '''
        classe Groupe Brique visant à créer l'objet de Gestion des briques affichés à l'écran.
    '''

    def __init__ (self, i_jeu, i_level) :

        '''
            Définition des variables du constructeur.
        '''

        self.jeu = i_jeu # Recupération des données de la classe Jeu.
        self.level = i_level # Définit l'attribut Level entrée dans le constructeur (qui correspond au niveau choisi) .

#--------------------------------------------------------------------------------------------------------------------------------------#

        # Créé la liste des briques à l'écran

        # Niveau de test 1 :
            # self.lvl_table = [['V1']]

        # Niveau de test 2 :
        self.lvl_table = [['V3','R0','V3']
                            ,['V3','R0','V3']
                            ,['V3','R0','V3']]
        # Niveau de test 3 :
            # self.lvl_table  = [
            #        ['-0','R0','V1','B2','R3','V0','B1','R2','V3','B0','R1','V2','B3','R0','V1','B2','R3']
            #       ,['-0','R0','V1','B2','V3','B0','R1','V2','B3','R0','V1','B2','R3','V0','B1','R2','V3']
            #       ,['-0','R0','V1','B2','B3','R0','V1','B2','R3','V0','B1','R2','V3','B0','R1','V2','B3']
            #       ,['-0','R0','V1','B2','R3','V0','B1','R2','V3','B0','R1','V2','B3','R0','V1','B2','R3']
            #       ,['-0','R0','V1','B2','V3','B0','R1','V2','B3','R0','V1','B2','R3','V0','B1','R2','V3']
            #       ,['-0','R0','V1','B2','B3','R0','V1','B2','R3','V0','B1','R2','V3','B0','R1','V2','B3']
            #       ,['-0','R0','V1','B2','R3','V0','B1','R2','V3','B0','R1','V2','B3','R0','V1','B2','R3']
            #       ,['-0','R0','V1','B2','V3','B0','R1','V2','B3','R0','V1','B2','R3','V0','B1','R2','V3']
            #        ]

#--------------------------------------------------------------------------------------------------------------------------------------#

        self.lvl_table_height = len(self.lvl_table) # Définit l'attribut 'hauteur'(height) qui correspond au nombre de listes dans la liste : self.lvl_table .
        self.lvl_table_witdh = len(self.lvl_table[0]) # Définit l'attribut 'largeur'(witdh) qui correspond au nombre déléments dans une liste de : self.lvl_table .
         
        self.lvl_padding_pct = 1 # en % // Définit l'attribut 'Bordure_pourcentage'(padding_pct) qui correspond à la taille en pourcent laissé de part et d'autre sur les côtés de la fenêtre avant d'afficher les différentes Brique(s).
        self.lvl_vertical_stt_pct = 5 # en % // Définit l'attribut 'commencement_vertical'(vertical_stt) qui correspond à la taille en pourcent laissé en haut de la fenêtre avant d'afficher la 1er Brique.
        self.lvl_vertical_end_pct = 60 # en % /!\ PAS PLUS DE 75 % /!\  // Définit l'attribut 'fin_vertical'(vertical_end) qui correspond à la taille en pourcent laissé en haut de la fenêtre avant d'afficher la dernière Brique.
        
        self.lvl_padding_px = i_jeu.hauteur_fenetre() * self.lvl_padding_pct / 100 # en px // Définit l'attribut 'Bordure_pourcentage'(padding_pct) qui correspond à la taille en Pixels laissé de part et d'autre sur les côtés de la fenêtre avant d'afficher les différentes Brique(s).
        self.lvl_vertical_stt_px = i_jeu.hauteur_fenetre() * self.lvl_vertical_stt_pct / 100 # en px // Définit l'attribut 'commencement_vertical'(vertical_stt) qui correspond à la taille en Pixels laissé en haut de la fenêtre avant d'afficher la 1er Brique.
        self.lvl_vertical_end_px = i_jeu.hauteur_fenetre() * self.lvl_vertical_end_pct / 100 # en px // Définit l'attribut 'fin_vertical'(vertical_end) qui correspond à la taille en Pixels laissé en haut de la fenêtre avant d'afficher la dernière Brique.
        
        self.brick_width = (self.jeu.largeur_fenetre() - (self.lvl_padding_px * ( 2 + self.lvl_table_witdh-1 ))) / self.lvl_table_witdh # Définit la Largeur que chaque brique doit avoir pour être equivalentes et respecter les marges.
        self.brick_height = ( (self.lvl_vertical_end_px - self.lvl_vertical_stt_px) - (self.lvl_padding_px * ( 2 + self.lvl_table_height - 1 ))) / self.lvl_table_height # Définit la Hauteur que chaque brique doit avoir pour être equivalentes et respecter les marges.
        self.list_brick = [] # Crée une liste vide afin d'accueillir les différentes briques du niveau.

        self.reset() 

        # Position de la brique la plus basse sur l'écran
        # Utilisé afin de ne pas passer du temps à controler les collisions
        # si la balle est de toute façon trop basse pour entrer en collision avec une des briques
        self.lowestBrickPosition = self.lvl_vertical_end_px

    def initialisationTableauBrique (self) :
        '''
            Fonction initialisant toutes les Briques dans le tableau : self.list_brick.
        '''
        for h in range(0,self.lvl_table_height) : # Pour une variable allant de 0 à la hauteur du tableau de Brique(s).
            for l in range(0,self.lvl_table_witdh) : # Pour une variable allant de 0 à la largeur du tableau de Brique(s).
                brick_x = self.lvl_padding_px + l * (self.brick_width + self.lvl_padding_px) + self.brick_width / 2 # Attribut une certaine largeur de brique à une variable : brick_x .
                brick_y = self.lvl_padding_px + h * (self.brick_height + self.lvl_padding_px) + self.lvl_vertical_stt_px + self.brick_height / 2 # Attribut une certaine hauteur de brique à une variable : brick_y .
                brick = Brique(self.jeu, brick_x, brick_y, self.brick_width, self.brick_height, self.lvl_table[h][l]) # Crée dans une variable brick un Objet Brique.
                if brick.getColorType() != '-' : # Si la brique ne possède pas le caractère couleur '-' servant a dire qu'il n'y a pas de brique, Alors : 
                    self.list_brick.append(brick) # La Brique est ajouté à : list_brick.


    def collision (self, balle) -> tuple :
        '''
            Fonction qui vérifie si la balle est entrée en collision avec une des briques. 
        '''
        r_collision = None # Valeur par défaut de la collision
        if self.lowestBrickPosition >= (balle.y - balle.rayon) : # Si la balle est contenu dans le tableau de brique à son niveau le plus bas, Alors :
            for e in self.list_brick : # Pour les éléments dans : self.list_brick.
                collision =  e.collision(balle) # Attribut les valeurs de la collision de la Brique en question dans la variable : collision.
                if collision != None : # Si la valeur retournée est différente de None, et donc c'est que la brique a été touché, Alors :
                    e.paint() # On met a jour le texte sur la brique 
                    r_collision = collision # La valeur de retour est associée à la valeur de collision.
                    if e.hit_points == -1 : # Si le nombre de points de vie est égale à -1 , et alors doit être détruite.
                        e.deleteFromCanvas() # On détruit le canvas de la Brique en question,
                        self.list_brick.remove(e) # et on la retire de la liste des Brique(s).
                    break # On casse la boucle pour éviter une boucle infinie sur le != de None.
                
        return r_collision # Retour de la valeur de collision.
        
    def reset (self) :
        '''
            Fonction permettant de réinitialiser les objets Brique(s) dans le canvas et de réinitialiset le noveau à son état initial.
        '''

        for e in self.list_brick : # Pour toutes les briques dans la liste :
            e.deleteFromCanvas() # On supprime le canvas associé pour leurs l'affichage graphique .

        self.list_brick.clear() # On réinitialise la liste des objets Brique(s) (elle est donc vide).
        self.initialisationTableauBrique() # On relance la création des objets Brique(s) dans la liste : self.list_brick.
        self.ground = False # Si ground vaut True , alors la balle rebondit sur le sol.