"""
    f1 module
"""
import math
from math import sin, cos

def calculate_square(x):
    '''f'''
    result= x*x
    return result


def calculate_circle_area(radius):
    '''f'''
    if radius <= 0:
        return None
    area = math.pi * radius ** 2
    return area


def calculate_rectangle_area(length, width):
    '''f'''
    area = length * width
    return area


def main():
    '''f'''
    radius = 5
    square = calculate_square(radius)
    print("Square:", square)
    rectangle_area = calculate_rectangle_area(4, 6)
    print("Rectangle Area:", rectangle_area)
    print("Sin(30 degrees):", sin(math.radians(30)))
    print("Cos(45 degrees):", cos(math.radians(45)))


if __name__ == "__main__":
    main()
