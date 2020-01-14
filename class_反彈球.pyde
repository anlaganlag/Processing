ballList = []  # save ball objs in
balls = 300
ball_size =20

class Ball:
    def __init__(self,x,y):
        #__int__ method is mainly contains attr/properties
        '''init a Ball obj'''
        self.xcor = x
        self.ycor = y
        self.xvel = random(-2,2)
        self.yvel = random(-2,2)
        self.col  = color(random(255),random(255),random(255))
    def update(self):
        self.xcor +=self.xvel
        self.ycor +=self.yvel
        if self.xcor > width or self.xcor < 0:
            self.xvel = -self.xvel
        if self.ycor > height or self.ycor < 0:
            self.yvel = -self.yvel   
        fill(self.col) 
        ellipse(self.xcor,self.ycor,ball_size,ball_size)
        
        

def setup():
    size(600,600)
    for i in range(balls):
        ballList.append(Ball(random(width),random(height)))
                             
    
def draw():
    background(0)
    for ball in ballList:
        ball.update()
    
    
    
