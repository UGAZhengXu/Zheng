from dataclasses import dataclass
from point import Point
import math

@dataclass

class Rectangle:
    center: Point
    width: float
    height:float

    def area(self):
       return self.width*self.height
    
    def perimeter(self):
       return (self.width+self.height)*2
    
    def boundingCircle(self):
       from circle import Circle
       return Circle(self.center,math.sqrt(self.width*self.width+self.height*self.height)/2)
    
    def getPoints(self):
       PointA=Point(self.center.x+self.width/2,self.center.y-self.height/2)
       PointB=Point(self.center.x-self.width/2,self.center.y-self.height/2)
       PointC=Point(self.center.x-self.width/2,self.center.y+self.height/2)
       PointD=Point(self.center.x+self.width/2,self.center.y+self.height/2)
       return [PointA,PointB,PointC,PointD]

    def __str__(self):
       return f"({self.center},width={self.width},height={self.height})"
    
if __name__=="__main__":
   Re=Rectangle(Point(2,2),6,8)
   print(Re)
   print(Re.area())
   print(Re.perimeter())
   print(Re.boundingCircle())
   print(Re.getPoints())