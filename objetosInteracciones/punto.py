class punto:
    def __init__(self,x0,y0):
        self.posx = x0
        self.posy = y0

    def movx (self,valor):
        self.posx+=valor

    def movy (self,valor):
        self.posy += valor

    def __str__(self):
        return ('posicion x: '+str(self.posx)+' - '+'posicion y: '+str(self.posy))


salto_x = int(input('en x > '))

salto_y = int(input('en y > '))

#Instancio el objeto:
miPunto = punto(0,0)


while miPunto.posx<1000:
    print (miPunto)
    miPunto.movx(salto_x)
    miPunto.movy(salto_y)

