class Naves():
    def __init__(self, coraza, escudo, distancia, fuerzaAtaque):
        self.coraza = coraza
        self.escudo = escudo
        self.distancia = distancia
        self.fuerzaAtaque = fuerzaAtaque

    def daño(self, fuerzaAtaque):
        self.escudo -= fuerzaAtaque
        if self.escudo <= 0:
            self.coraza -= fuerzaAtaque

cruseroResurgente = DestructorEstelar = Naves(115, 142, 48, 93)
#----------------------------------------------------VERSUS------------------------------------------------------------#
cruseroLibertad = cruseroMonCalamari_1 = Naves(120, 140, 70, 85)
fragataShantipole = fragataNebulonB_1 = Naves(78, 64, 45, 47)
fragataDiplomacia = fragataNebulonB_2 = Naves(78, 64, 37, 47)