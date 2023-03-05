class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y


class Triangle:
    def __init__(self,P1: Point,P2:Point, P3:Point):
        self.P1=P1
        self.P2=P2
        self.P3=P3
    # def __init__(self,Points):
    #     self.P1=Point[0]
    #     self.P2=Point[1]
    #     self.P3=Point[2]
t=Triangle(Point(1,2),Point(3,2),Point(5,6))
# t=Triangle([Point(1,2),Point(3,2),Point(5,6)])