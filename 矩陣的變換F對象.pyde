xmin=-10
xmax=10
ymin=-10
ymax=10
rangex = xmax - xmin
rangey = ymax - ymin
fmatrix = [[0,0],[1,0],[1,2],[2,2],[2,3],[1,3],[1,4],[3,4],[3,5],[0,5]]
transformation_matrix=[[0,-1],[1,0]]

def setup():
    global xscl,yscl
    size(600,600)
    xscl = width/rangex
    yscl = -height/rangey
    noFill()
    
def draw():
    global xscl,yscl#tell py not creating new var use the global
    background(255)#set background color white 
    translate(width/2,height/2)
    grid(xscl,yscl)
    # graphFunction()
    newmatrix = multmatrix(fmatrix,transformation_matrix)
    graphPoints(fmatrix)
    strokeWeight(2) #thicker line
    stroke(255,0,0) #black
    graphPoints(newmatrix)

    
def graphPoints(matrix):
    #draw line segments between consecutive points
    beginShape()
    for pt in matrix:
        vertex(pt[0]*xscl,pt[1]*yscl)
    endShape(CLOSE)
    
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
    
def multmatrix(a,b):
    #Returns the product of matrix a and matrix b
    m = len(a) #number of rows in first matrix
    n = len(b[0]) #number of columns in second matrix
    newmatrix = []
    for i in range(m):
        row = []
        #for every column in b
        for j in range(n):
            sum1 = 0
            #for every element in the column
            for k in range(len(b)):
                sum1 += a[i][k]*b[k][j]
            row.append(sum1)
        newmatrix.append(row)
    return newmatrix

def f(x):
    return sin(x)

def graphFunction():
    x = xmin
    while x <= xmax:
        stroke(255,0,0)
        line(x*xscl,f(x)*yscl,(x+0.1)*xscl,f(x+0.1)*yscl)
        x += 0.1
