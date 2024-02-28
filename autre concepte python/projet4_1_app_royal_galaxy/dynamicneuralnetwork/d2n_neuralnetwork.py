import dynamicneuralnetwork.d2n_math as mth
global BASE_DIST
BASE_DIST=70

class Nnr():
    # par defaut un Nnr est en mode "NULL"
    def __init__(self, x=0, y=0, neurone_of_stack=[], mode="NULL"):
        self.mode=mode
        self.neurone_of_stack = neurone_of_stack
        self.max_stack=max(self.neurone_of_stack)
        self.stack=[]
        self.INTER_NER_DIST3=340
        self.start=mth.Vect(x, y)
        self.BASE_DIST=BASE_DIST
        

        # génération des couches "stack"

        # max=self.max_stack
        # base=self.BASE_DIST

        for i in range(len(self.neurone_of_stack)):
            n=self.neurone_of_stack[i]
            centrage=self.BASE_DIST*(self.max_stack-n) # pour que les couches soient centrées les une par rapport aux autres
            if i==0:
                self.stack.append(Stack(x, y +centrage, self.neurone_of_stack[0], mode=self.mode))
            else:
                self.stack.append(Stack(x+i*self.INTER_NER_DIST3, y +centrage, self.neurone_of_stack[i], mode=self.mode))
        
        

        

    def show_mode(self):
        print(f"Le mode actuel est : <{self.mode}>")
        print("LR   : créer un reseau de neurones avec les branches de gauche(Left) et de droite(Right) pour chaque neurones")
        print("L    : créer un reseau de neurones avec uniquement les branches de gauche(Left) pour chaque neurones")
        print("R    : créer un reseau de neurones avec uniquement les branches de droite(Right) pour chaque neurones")
        print("NULL : aucun des modes cités précedement")

    def drawall(self, cnv):
        # génération des branches de droites des neurones de toutes les couches sauf la dernière couche
        # IL FAUT QUE LE RESEAU EST AU MOINS 2 COUCHES, SINON LES BOUCLES QUI VIENENT JUSTE APRES PRODUIRONS DES ERREURS
        for i in range(len(self.neurone_of_stack)-1):
            for j in range(self.neurone_of_stack[i]):
                # on conserve le <center> du j-ième neurone de la i-ième couche
                start=self.stack[i].neurone[j].center
                for k in range(self.neurone_of_stack[i+1]):
                    # on conserve le <center> du k-ième neurone de la (i+1)-ième couche
                    end=self.stack[i+1].neurone[k].center
                    # on dessine la branch partant de <start> jusqu'à <end>
                    self.stack[i].neurone[j].draw_branch(start, end, cnv)
        
        # génération des neurones de toutes les couches
        for i in range(len(self.neurone_of_stack)):
            self.stack[i].drawall(cnv)
        pass
    
    def hideall():
        pass

    def toggle():
        pass

    def add(num, nb=1):
        pass

    def rem(num, nb=1):
        pass

class Stack():
    # par defaut un Stack est en mode "NULL"
    def __init__(self, x=0, y=0, n=0, mode="NULL"):
        self.mode=mode
        self.neurone_nb = n
        self.neurone=[]
        self.INTER_NER_DIST2=140
        self.start=mth.Vect(x, y)

        # initialisation des neuronnes
        for i in range(n):
            self.neurone.append(Neurone(x, y+i*self.INTER_NER_DIST2, mode=self.mode))
        

    def show_mode(self):
        print(f"Le mode actuel est : <{self.mode}>")
        print("LR : créer une couche avec les branches de gauche(Left) et de droite(Right) pour chaque neurones")
        print("L  : créer une couche avec uniquement les branches de gauche(Left) pour chaque neurones")
        print("R  : créer une couche avec uniquement les branches de droite(Right) pour chaque neurones")
        print("NULL : aucun des modes cités précedement")

    
    def drawall(self, cnv):
        for i in range(self.neurone_nb):
            self.neurone[i].draw(cnv)

    def hideall():
        pass
    
    def toggle():
        pass

    def add(nb=1):
        pass

    def rem(nb=1):
        pass

class Neurone():
    # par defaut un Neurone est en mode "LR"
    def __init__(self, x=0, y=0, color="black", mode="NULL"):
        self.mode=mode

        self.COLOR=color
        self.COLOR_BG="ivory"
        # self.isfill=True
        # self.limits=[] # tableau de 4 entiers

        self.INTER_NER_DIST1=170
        self.BASE_DIST=BASE_DIST
        self.RADIUS=30
        self.RADIUS_BG=self.RADIUS+12
        self.start=mth.Vect(x, y+self.BASE_DIST)
        self.nw_corner_pos=mth.Vect(x, y-self.BASE_DIST)
        self.center=mth.Vect(self.start.getx()+self.INTER_NER_DIST1, self.start.gety())
    
    def show_mode(self):
        print(f"Le mode actuel est : <{self.mode}>")
        print("LR : créer un neurone avec les branches de gauche(Left) et de droite(Right)")
        print("L  : créer un neurone avec uniquement les branches de gauche(Left)")
        print("R  : créer un neurone avec uniquement les branches de droite(Right)")
        print("NULL : aucun des modes cités précedement")

    def draw(self, cnv):
        self.branch(cnv)
        # je crée un cercle legèrement plus grand que le cercle qui represente le neurone
        self.circle_bg(cnv)
        # pour que les branches ne touches ou ne soit ni à l'interieur du cercle qui represente le neurone (celui que je crée juste après)
        self.circle(cnv) # (celui là)
    
    def draw_branch(self, start, end, cnv):
        x0=start.getx()
        y0=start.gety()
        x1=end.getx()
        y1=end.gety()
        cnv.create_line(x0, y0, x1, y1, width=2)


    def show(self, cnv):
        pass
    
    def show_circle(self, cnv):
        pass

    def show_branch(self, cnv):
        pass

    def show_branch_back(self, cnv):
        pass

    def show_branch_next(self, cnv):
        pass

    def hide():
        pass

    def hide_circle(self, cnv):
        pass

    def hide_branch(self, cnv):
        pass

    def hide_branch_back(self, cnv):
        pass

    def hide_branch_next(self, cnv):
        pass

    def toggle():
        pass

    def toggle_circle(self, cnv):
        pass

    def toggle_branch(self, cnv):
        pass

    def toggle_branch_back(self, cnv):
        pass

    def toggle_branch_next(self, cnv):
        pass

    def move():
        pass

    def circle(self, cnv):
        color=self.COLOR
        r=self.RADIUS
        x=self.center.getx()
        y=self.center.gety()

        cnv.create_oval(x-r, y-r, x+r, y+r, outline=color, width=2)

    def circle_bg(self, cnv):
        color_bg=self.COLOR_BG
        r=self.RADIUS_BG
        x=self.center.getx()
        y=self.center.gety()

        cnv.create_oval(x-r, y-r, x+r, y+r, fill=color_bg, outline="")

    def branch(self, cnv):
        # inter_ner_dist1=self.INTER_NER_DIST1


        # creation des deux branches du coté gauche du neurone
        if self.mode=="LR" or self.mode=="L":
            self.branch_back(cnv)
        # creation de la branche du coté droit du neurone
        # le probleme est que là il serai compliqué de créer
        # un programme qui decale (par translation) les neurones
        # sachant que les branches doivent aussi être décalées,
        # la solution serai peut-être d'utiliser la POO
        # (pour créer des objets) et des design patterh appropriés
        if self.mode=="LR" or self.mode=="R":
            self.branch_next(cnv)


    def branch_back(self, cnv):
        x=self.center.getx()
        y=self.center.gety()

        x1=self.start.getx()
        y1=self.start.gety()

        base=self.BASE_DIST

        cnv.create_line(x1, y1-base, x, y, width=2)
        cnv.create_line(x1, y1+base, x, y, width=2)

    def branch_next(self, cnv):
        x=self.center.getx()
        y=self.center.gety()

        cnv.create_line(x, y, x+self.INTER_NER_DIST1, y, width=2)