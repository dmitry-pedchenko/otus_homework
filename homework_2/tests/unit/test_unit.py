import pytest

from src.triangle import Triangle
from src.square import Square
from src.figure import Figure
from src.rectangle import Rectangle
from src.circle import Circle


class TestTriangle:
    def test_create_triangle_with_error(self):
        with pytest.raises(ValueError):
            Triangle(1, 1, 4)

    def test_triangle_area_perimeter(self):
        triangle = Triangle(6, 4, 4)

        assert triangle.area == 7.937253933193772
        assert triangle.perimeter == 14
        assert triangle.name == "Triangle"


class TestSquare:
    def test_square_area_perimeter(self):
        square = Square(2)

        assert square.area == 4
        assert square.perimeter == 8
        assert square.name == "Square"


class TestRectangle:
    def test_rectangle_area_perimeter(self):
        rectangle = Rectangle(1, 2)

        assert rectangle.area == 2
        assert rectangle.perimeter == 6
        assert rectangle.name == "Rectangle"


class TestCircle:
    def test_circle_area_perimeter_with_radius(self):
        circle = Circle(radius=2)

        assert circle.area == 12.566370614359172
        assert circle.perimeter == 12.566370614359172
        assert circle.name == "Circle"

    def test_circle_area_perimeter_with_diameter(self):
        circle = Circle(diameter=3)

        assert circle.area == 7.0685834705770345
        assert circle.perimeter == 9.42477796076938

    def test_create_empty_circle_error(self):
        with pytest.raises(ValueError):
            Circle()


class TestFigure:
    def test_create_figure_error(self):
        with pytest.raises(TypeError):
            Figure()
