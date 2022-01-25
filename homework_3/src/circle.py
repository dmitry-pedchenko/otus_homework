from pydantic.dataclasses import dataclass
from pydantic.types import Optional
from math import pi

from figure import Figure


@dataclass
class Circle(Figure):
    radius: Optional[float] = None
    diameter: Optional[float] = None

    def __post_init__(self):
        if self.radius and self.diameter:
            raise ValueError("Please, set only radius or diameter not both.")

        if not self.diameter and not self.radius:
            raise ValueError("Set radius or diameter.")

    @property
    def area(self) -> float:
        if self.radius:
            return pi * self.radius * self.radius

        return ((self.diameter * self.diameter) / 4) * pi  # type: ignore

    @property
    def perimeter(self) -> float:
        if self.radius:
            return 2 * self.radius * pi

        return self.diameter * pi  # type: ignore
