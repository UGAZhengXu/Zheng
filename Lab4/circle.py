from dataclasses import dataclass
from point import Point
import math

@dataclass

class Circle:
    center: Point
    radius: float

    def insideSquare(self):
     from rectangle import Rectangle
     return Rectangle(Point(self.center.x,self.center.y),self.radius*math.sqrt(2),self.radius*math.sqrt(2))
    
    def area(self):
      return math.pi*self.radius*self.radius
    
    def perimeter(self):
      return 2*math.pi*self.radius

    def __str__(self):
     return f"({self.center},r={self.radius})"

if __name__=="__main__":
   c=Circle(Point(3,4),5)
   print(c)
   print(c.insideSquare())
   print(c.area())
   print(c.perimeter())