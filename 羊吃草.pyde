WHITE = color(255)
BROWN = color(102,51,0)
RED = color(255,0,0)
GREEN = color(0,102,0)
YELLOW = color(255,255,0)
PURPLE = color(102,0,204)
# rows_of_grass = height/patchSize

sheepList = []
grassList = []
patchSize = 10
class Grass:
    def __init__(self,x,y,sz):
        self.x =x
        self.y =y
        self.energy =5
        self.eaten = False
        self.sz = sz
    def update(self):
        if self.eaten:
            fill(BROWN)
        else:
            fill(GREEN)
        rect(self.x,self.y,self.sz,self.sz)

class Sheep:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.sz = 10
        self.energy =350
        
    def update(self):
        move = 1
        self.energy-= 1
        if self.energy <= 0:
            sheepList.remove(self)
        self.x += random(-move,move)
        self.y += random(-move,move)
        if self.x > width:
            self.x %= width
        if self.y > height:
            self.y %= height
        if self.x<0:
            self.x += width
        if self.y <0:
            self.y += height
        xscl = int(self.x/patchSize)
        yscl = int(self.y/patchSize)
        grass = grassList[xscl * rows_of_grass+yscl]
        if not grass.eaten:
            self.energy +=grass.energy
            grass.eaten = True
        fill(255)
        ellipse(self.x,self.y,self.sz,self.sz)


def setup():
    rows_of_grass = height/patchSize
    global patchSize,rows_of_grass
    size(600,600)
    noStroke()
    for i in range(25):
        sheepList.append(Sheep(random(width),random(height)))
    for x in range(0,width,patchSize):
        for y in range(0,height,patchSize):
            grassList.append(Grass(x,y,patchSize))
        
def draw():
    background(255)
    for grass in grassList:
        grass.update()
        
    for sheep in sheepList:
        sheep.update()
