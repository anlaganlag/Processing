from math import sin ,cos
def setup():
    size(600,600)


def draw():
   #range 循環次數比如10邊形就是乘以 36 
   #總之乘積就是360
   #7邊就是range(7)   (51.43*i)
    translate(width/2,height/2)
    beginShape()
    for i in range(10):
        vertex(100*cos(radians(36*i)),100*sin(radians(36*i)))
    endShape(CLOSE)



def setup():
    size(600,600)
    
def draw():
    translate(width/2,height/2)
    polygon(7,100)#3 sides ,v 100 units from the center
    
def polygon(sides,sz):
    beginShape()
    for i in range(sides):
        step = radians(360/sides)
        vertex(sz*cos(i*step),sz*sin(i*step))
    endShape(CLOSE)
