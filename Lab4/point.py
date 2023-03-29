from dataclasses import dataclass
import math

@dataclass

class Point:
    x:float
    y:float

    def length(self):
        return math.sqrt(self.x*self.x+self.y*self.y)
    
    def __str__(self):
        return f"<{self.x},{self.y}>"

if __name__=="__main__":
    p = Point(3,4)
    print(p)
    print(p.length())