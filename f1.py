import math, os

def calculate_square(x):
    result= x*x
    return result


def calculate_circle_area(radius):
    if radius <= 0:
        return None
    else:
        area = math.pi * radius ** 2
        return area
        pass

from math import pi, sin, cos

def calculate_rectangle_area(length, width):
    area = length * width
    return area


def main():
    radius = 5
    square = calculate_square(radius)
    print("Square:", square)
    
    rectangle_area = calculate_rectangle_area(4, 6)
    print("Rectangle Area:", rectangle_area)
    
    print("Sin(30 degrees):", sin(math.radians(30)))
    print("Cos(45 degrees):", cos(math.radians(45)))


if __name__ == "__main__":
    main()
