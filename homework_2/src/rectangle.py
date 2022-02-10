from pydantic.dataclasses import dataclass

from figure import Figure


@dataclass
class Rectangle(Figure):
    edge1: float
    edge2: float

    @property
    def area(self) -> float:
        return self.edge1 * self.edge2

    @property
    def perimeter(self) -> float:
        return (self.edge1 + self.edge2) * 2
