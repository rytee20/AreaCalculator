from math import pi, sqrt
from abc import abstractmethod

class AreaCalculator:
    @abstractmethod
    def area_calculation(self):
        pass

class Circle(AreaCalculator):
    def __init__(self, rad):
        self.rad = rad
        
    def area_calculation(self):
        return pi * self.rad**2

class Triangle(AreaCalculator):
    def __init__(self,edge1,edge2,edge3):
        self.edge1 = edge1;
        self.edge2 = edge2;
        self.edge3 = edge3;

    def is_triangle_exist(self):
        if((self.edge1 + self.edge2 > self.edge3 and
        self.edge1 + self.edge3 > self.edge2 and
        self.edge2 + self.edge3 > self.edge1) and
        (self.edge1 != 0 and self.edge2 != 0 and self.edge3 != 0)):
            return True
        else:
            return False

    def area_calculation(self):
        if(self.is_triangle_exist()):
            p = (self.edge1 + self.edge2 + self.edge3) / 2
            return sqrt(p * (p - self.edge1) * (p - self.edge2) * (p - self.edge3))
        else:
            print('Triangle with specified edges does not exist');

    def is_triangle_rectangular(self):
        if (self.is_triangle_exist()):
            if(self.edge1**2 == self.edge2**2 + self.edge3**2 or
            self.edge2**2 == self.edge1**2 + self.edge3**2 or
            self.edge3**2 == self.edge1**2 + self.edge2**2):
                print('Triangle is rectangular')
            else:
                print('Triangle is not rectangular')
        else:
            print('Triangle with specified edges does not exist')

if __name__ == '__main__':
    circle = Circle(5)
    triangle = Triangle(3, 0, 5)

    print("Circle Area:", circle.area_calculation())
    print("Triangle Area:", triangle.area_calculation())
    print("Is Triangle Rectangular:")
    triangle.is_triangle_rectangular()
