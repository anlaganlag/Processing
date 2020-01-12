from math import sin,cos,tan
xmin=-10
xmax=10
ymin=-10
ymax=10
rangex = xmax - xmin
rangey = ymax - ymin
def setup():
    global xscl,yscl
    size(600,600)
    xscl = width/rangex
    yscl = -height/rangey
    
def draw():
    global xscl,yscl#tell py not creating new var use the global
    background(255)#set background color white 
    translate(width/2,height/2)
    grid(xscl,yscl)
    graphFunction()
    
def grid(xscl,yscl):
    #use to move shapes up and down
    #or left and right
    #move the orgin from top left to center of the screen
    strokeWeight(1)
    stroke(0,255,255)
    for i in range(xmin,xmax+1):
        line(i*xscl,ymin*yscl,i*xscl,ymax*yscl)
    for i in range(ymin,ymax+1):
        line(xmin*xscl,i*yscl,xmax*xscl,i*yscl)
    stroke(0)
    line(0,ymin*yscl,0,ymax*yscl)
    line(xmin*xscl,0,xmax*xscl,0)
    


def f(x):
    return tan(x)

def graphFunction():
    x = xmin
    while x <= xmax:
        stroke(255,0,0)
        line(x*xscl,f(x)*yscl,(x+0.1)*xscl,f(x+0.1)*yscl)
        x += 0.1
