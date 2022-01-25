from pydantic.dataclasses import dataclass

from figure import Figure


@dataclass
class Square(Figure):
    edge: float

    @property
    def perimeter(self) -> float:
        return self.edge * 4

    @property
    def area(self) -> float:
        return self.edge * self.edge
