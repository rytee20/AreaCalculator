from unittest import TestCase
from math import pi
from unittest.mock import patch
from AreaCalculator import Circle, Triangle

class TestAreaCalculator(TestCase):
    def testCircleAreaCalculate(self):
        circle = Circle(5)
        self.assertAlmostEqual(circle.area_calculation(), pi * 5 ** 2)

    def testTriangleIsNotExist(self):
        triangle = Triangle(1, 1, 100)
        self.assertFalse(triangle.is_triangle_exist())

    def testTriangleIsNotExistZero(self):
        triangle = Triangle(1, 0, 5)
        self.assertFalse(triangle.is_triangle_exist())

    def testTriangleIsExist(self):
        triangle = Triangle(3, 4, 5)
        self.assertTrue(triangle.is_triangle_exist())

    @patch('builtins.print')
    def testTriangleIsRectangular(self, mock_print):
        triangle = Triangle(3, 4, 5)
        triangle.is_triangle_rectangular()
        mock_print.assert_called_with('Triangle is rectangular')

    @patch('builtins.print')
    def testTriangleIsNotRectangular(self, mock_print):
        triangle = Triangle(2, 6, 5)
        triangle.is_triangle_rectangular()
        mock_print.assert_called_with('Triangle is not rectangular')
