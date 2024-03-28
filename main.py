from AreaCalculator import Circle, Triangle


if __name__ == '__main__':
    circle = Circle(5)
    triangle = Triangle(3, 3, 5)

    print("Circle Area:", circle.area_calculation())
    print("Triangle Area:", triangle.area_calculation())
    print("Is Triangle Rectangular:")
    triangle.is_triangle_rectangular()
