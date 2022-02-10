from pydantic.dataclasses import dataclass
from math import sqrt

from figure import Figure


@dataclass
class Triangle(Figure):
    first_edge: float
    second_edge: float
    third_edge: float

    def __post_init__(self):
        if self.first_edge + self.second_edge >= self.third_edge:
            if self.first_edge + self.third_edge >= self.second_edge:
                if self.third_edge + self.second_edge >= self.first_edge:
                    return

        raise ValueError("Triangle does not exists.")

    @property
    def area(self) -> float:
        return sqrt(
            self._half_perimeter
            * (self._half_perimeter - self.first_edge)
            * (self._half_perimeter - self.second_edge)
            * (self._half_perimeter - self.third_edge),
        )

    @property
    def perimeter(self) -> float:
        return self.first_edge + self.second_edge + self.third_edge

    @property
    def _half_perimeter(self) -> float:
        return self.perimeter / 2
