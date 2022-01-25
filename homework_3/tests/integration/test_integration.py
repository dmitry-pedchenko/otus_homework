import pytest

from src.triangle import Triangle
from src.square import Square
from src.rectangle import Rectangle
from src.circle import Circle


class TestIntegration:
    @pytest.mark.parametrize(
        "figure1,figure2,result",
        [
            (Triangle(6, 4, 4), Triangle(6, 4, 4), 15.874507866387544),
            (Triangle(6, 4, 4), Square(2), 11.937253933193773),
            (Square(2), Square(2), 8),
            (Rectangle(1, 2), Rectangle(1, 2), 4),
            (Triangle(6, 4, 4), Rectangle(1, 2), 9.937253933193773),
            (Square(2), Rectangle(1, 2), 6),
            (Circle(radius=2), Circle(radius=2), 25.132741228718345),
            (Circle(radius=2), Triangle(6, 4, 4), 20.503624547552946),
            (Circle(radius=2), Square(1), 13.566370614359172),
            (Circle(radius=2), Rectangle(1, 2), 14.566370614359172),
        ],
        ids=[
            ("Triangle,Triangle"),
            ("Triangle,Square"),
            ("Square,Square"),
            ("Rectangle,Rectangle"),
            ("Triangle,Rectangle"),
            ("Square,Rectangle"),
            ("Circle with radius,Circle with radius"),
            ("Circle,Triangle"),
            ("Circle,Square"),
            ("Circle,Rectangle"),
        ],
    )
    def test_sum(self, figure1, figure2, result):
        assert figure1 + figure2 == result
