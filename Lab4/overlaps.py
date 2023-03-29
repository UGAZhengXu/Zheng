from point import Point
from rectangle import Rectangle
from circle import Circle
import math

def point_rectangle(p,r):
    if abs(p.x-r.center.x)<r.width/2:
        if abs(p.y-r.center.y)<r.height/2:
            return True
        else:
            return False
    else:
        return False

def point_circle(p,c):
    newx=p.x-c.center.x
    newy=p.y-c.center.y
    if math.sqrt(newx*newx+newy*newy)<c.radius:
        return True
    else:
        return False

def rectangle_rectangle(r1, r2):
    center_disx=abs(r1.center.x-r2.center.x)
    center_disy=abs(r1.center.y-r2.center.y)
    if center_disx<(r1.width+r2.width)/2 and center_disy<(r1.height+r2.height)/2:
        return True
    else:
        return False

def circle_circle(c1, c2):
    newx=c1.center.x-c2.center.x
    newy=c1.center.y-c2.center.y
    if math.sqrt(newx*newx+newy*newy)<(c1.radius+c1.radius):
        return True
    else:
        return False
    
def rectangle_circle(r, c):
    p_x = max(r.center.x-r.width/2, min(r.center.x+r.width/2, c.center.x))
    p_y = max(r.center.y-r.height/2, min(r.center.x+r.width/2, c.center.y))
    if math.sqrt((p_x-c.center.x)*(p_x-c.center.x)+(p_y-c.center.y)*(p_y-c.center.y))<c.radius:
        return True
    else:
        return False

if __name__=="__main__":
    testPoint=Point(3,4)
    testRectangle1=Rectangle(Point(2,2),6,8)
    testRectangle2=Rectangle(Point(3,0),2,4)
    testCircle1=Circle(Point(3,4),5)
    testCircle2=Circle(Point(-15,0),1)
    print("TestPoint:",testPoint)
    print("TestRetangles:",testRectangle1,testRectangle2)
    print("TestCircles:",testCircle1,testCircle2)
    print(point_rectangle(testPoint,testRectangle1))
    print(point_circle(testPoint,testCircle1))
    print(rectangle_rectangle(testRectangle1,testRectangle2))
    print(circle_circle(testCircle1,testCircle2))
    print(rectangle_circle(testRectangle1,testCircle1))
