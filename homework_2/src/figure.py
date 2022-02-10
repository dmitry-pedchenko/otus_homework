from abc import ABC
from abc import abstractmethod
from pydantic.dataclasses import dataclass


@dataclass
class Figure(ABC):
    @abstractmethod
    def area(self) -> float:
        ...  # noqa: WPS428

    @abstractmethod
    def perimeter(self) -> float:
        ...  # noqa: WPS428

    @property
    def name(self) -> str:
        return self.__class__.__name__

    def __add__(self, other) -> float:
        if isinstance(other, Figure):
            return self.area + other.area  # type: ignore

        raise ValueError(f"Wrong added object {other.__class__.__name__}.")
