from brique import Brique

class Level : 


    '''
        classe Groupe Brique visant à créer l'objet de Gestion des briques affichés à l'écran.
    '''

    def __init__ (self, jeu, level) :

        '''
            Fonction d'initialisation.
        '''

        self.jeu = jeu
        self.level = level

        # Créé la liste des briques à l'écran
        self.lvl_table  = [
               ['-0','R0','V1','B2','R3','V0','B1','R2','V3','B0','R1','V2','B3','R0','V1','B2','R3']
              ,['-0','R0','V1','B2','V3','B0','R1','V2','B3','R0','V1','B2','R3','V0','B1','R2','V3']
              ,['-0','R0','V1','B2','B3','R0','V1','B2','R3','V0','B1','R2','V3','B0','R1','V2','B3']
              ,['-0','R0','V1','B2','R3','V0','B1','R2','V3','B0','R1','V2','B3','R0','V1','B2','R3']
              ,['-0','R0','V1','B2','V3','B0','R1','V2','B3','R0','V1','B2','R3','V0','B1','R2','V3']
              ,['-0','R0','V1','B2','B3','R0','V1','B2','R3','V0','B1','R2','V3','B0','R1','V2','B3']
              ,['-0','R0','V1','B2','R3','V0','B1','R2','V3','B0','R1','V2','B3','R0','V1','B2','R3']
              ,['-0','R0','V1','B2','V3','B0','R1','V2','B3','R0','V1','B2','R3','V0','B1','R2','V3']
              ]



        self.lvl_table_height = len(self.lvl_table)
        self.lvl_table_witdh = len(self.lvl_table[0])
        
        self.lvl_padding_pct = 1 # %
        self.lvl_vertical_stt_pct = 5 # %
        self.lvl_vertical_end_pct = 60 # % /!\ PAS PLUS DE 75 % /!\
        
        self.lvl_padding_px = jeu.hauteur_fenetre() * self.lvl_padding_pct / 100
        self.lvl_vertical_stt_px = jeu.hauteur_fenetre() * self.lvl_vertical_stt_pct / 100
        self.lvl_vertical_end_px = jeu.hauteur_fenetre() * self.lvl_vertical_end_pct / 100
        
        self.brick_width = (self.jeu.largeur_fenetre() - (self.lvl_padding_px * ( 2 + self.lvl_table_witdh-1 ))) / self.lvl_table_witdh
        self.brick_height = ( (self.lvl_vertical_end_px - self.lvl_vertical_stt_px) - (self.lvl_padding_px * ( 2 + self.lvl_table_height - 1 ))) / self.lvl_table_height
        self.list_brick = []

        self.reset()

        # Position de la brique la plus basse sur l'écran
        # Utilisé afin de ne pas passer du temps à controler les collisions
        # si la balle est de toute façon trop basse pour entrer en collision avec une des briques
        self.lowestBrickPosition = self.lvl_vertical_end_px
        
        self.ground = False # Si ground vaut True , alors la balle rebondit sur le sol.

    def initialisationTableauBrique (self) :

        for h in range(0,self.lvl_table_height) :
            for l in range(0,self.lvl_table_witdh) :
                brick_x = self.lvl_padding_px + l * (self.brick_width + self.lvl_padding_px) + self.brick_width / 2
                brick_y = self.lvl_padding_px + h * (self.brick_height + self.lvl_padding_px) + self.lvl_vertical_stt_px + self.brick_height / 2 
                brick = Brique(self.jeu, brick_x, brick_y, self.brick_width, self.brick_height, self.lvl_table[h][l])
                if brick.getColorType() != '-' :
                    self.list_brick.append(brick)


    def collision (self, balle) -> int :
        # Vérifie si la balle est entrée en collision avec une des briques 
        r_collision = 0
        if self.lowestBrickPosition >= (balle.y - balle.rayon) :
            for e in self.list_brick :
                
                collision =  e.collision(balle)
                if collision != 0 :
                    e.paint()
                    r_collision = collision
                    if e.hit_points == -1 :
                        e.deleteFromCanvas()
                        self.list_brick.remove(e)
                    break
                
        return int(r_collision)
        
    def reset (self) :

        for e in self.list_brick :
            e.deleteFromCanvas()

        self.list_brick.clear()
        self.initialisationTableauBrique()