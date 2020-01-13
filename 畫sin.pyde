r1= 100
# 在畫面左邊的大圓
r2= 10
#在大圓的紅色點,相當於一個mark點
t =0
#時間等於開始
circleList = []
#用於存儲高度的歷史數據,即高度y
def setup():
    size(600,600)
    #大爲600的屏幕
    
def draw():
    global t,circleList
    background(200)#背景色0是黑色  255是白色
       #所以這裏是灰白
    
    translate(width/4,height/2)
    #畫面靠左邊的位置
    noFill()
    #大圓不需要填充
    stroke(0)
    ellipse(0,0,2*r1,2*r1)
    
    fill(255,0,0)
    #小圓填充成紅色
    y = -r1*sin(t)
    x = r1*cos(t)
    #這裏不需要切換成角度,弧度即可
    # circleList.insert(0,y)
    circleList = [y] +circleList[:249]
    #將所有的y,在0的位置插入,但是限制了最多是250個點
    ellipse(x,y,r2,r2)
    
    stroke(0,255,0)
    #綠色的線
    line(x,y,200,y)
    #xy這個向右延伸200,這個很直觀
    fill(0,255,0)
    for i in range(len(circleList)):
        ellipse(200+i,circleList[i],5,5)
    t += 0.05
