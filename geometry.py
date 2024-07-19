import math
from abc import ABC, abstractmethod


class Shape(ABC):
    """интерефейс для фигур"""
    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def is_right_triangle(self) -> bool:
        pass

class Circle(Shape):
    def __init__(self, radius: float):
        self.radius: float = radius

    def area(self) -> float:
        return math.pi * (self.radius ** 2)

    def is_right_triangle(self) -> bool:
        return False


class Triangle(Shape):
    def __init__(self, a: float, b: float, c: float):
        self.a: float = a
        self.b: float = b
        self.c: float = c

    def area(self) -> float:
        s: float = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def is_right_triangle(self) -> bool:
        sides: list[float] = sorted([self.a, self.b, self.c])
        return (sides[0] ** 2)  + (sides[1] ** 2) == sides[2] ** 2


class FigureCreator:
    """для создания объектов фигур"""
    @staticmethod
    def create_circle(radius: float) -> Circle:
        return Circle(radius)

    @staticmethod
    def create_triangle(a: float, b: float, c: float) -> Triangle:
        return Triangle(a, b, c)


# юнит-тесты
import unittest

class TestShapes(unittest.TestCase):
    def test_circle_area(self) -> None:
        circle: Circle = Circle(5)
        self.assertAlmostEqual(calculate_area(circle), 78.53981633974483, places=5)

    def test_triangle_area(self) -> None:
        triangle: Triangle = Triangle(3, 4, 5)
        self.assertAlmostEqual(calculate_area(triangle), 6, places=5)

    def test_triangle_is_right_triangle(self) -> None:
        triangle: Triangle = Triangle(3, 4, 5)
        self.assertTrue(triangle.is_right_triangle())

        triangle = Triangle(2, 2, 3)
        self.assertFalse(triangle.is_right_triangle())

    def test_triangle_area_invalid(self) -> None:
        triangle: Triangle = Triangle(1, 2, 3)
        self.assertAlmostEqual(calculate_area(triangle), 0.0, places=5)