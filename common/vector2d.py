from __future__ import annotations
from typing import Any
import math

class Vector2D:
    def __init__(self, x: float=0.0, y: float=0.0) -> None:
        self.x = x
        self.y = y

    def zero(self) -> None:
        self.x = 0.0
        self.y = 0.0

    def __bool__(self) -> bool:
        return self.x == self.x == 0.0

    def __repr__(self) -> str:
        return f"Vector2D({self.x}, {self.y})"

    def __str__(self) -> str:
        return f"<{self.x:.2f} {self.y:.2f}>"

    def __eq__(self, o: Any) -> bool:
        return isinstance(o, Vector2D) and self.x == o.x and self.y == o.y

    def __add__(self, v2: Vector2D) -> Vector2D:
        raise NotImplementedError

    def __iadd__(self, v2: Vector2D) -> Vector2D:
        raise NotImplementedError

    def __sub__(self, v2: Vector2D) -> Vector2D:
        raise NotImplementedError

    def __isub__(self, v2: Vector2D) -> Vector2D:
        raise NotImplementedError

    def __mul__(self, other: float) -> Vector2D:
        raise NotImplementedError

    def __imul__(self, other: float) -> Vector2D:
        raise NotImplementedError

    def __truediv__(self, other: float) -> Vector2D:
        raise NotImplementedError

    def __itruediv__(self, other: float) -> Vector2D:
        raise NotImplementedError

    def length(self) -> float:
        return math.sqrt(self.length_sq())

    def length_sq(self) -> float:
        return self.x ** 2 + self.y ** 2

    def normalize(self) -> Vector2D:
        raise NotImplementedError

    def dot(self, v2: Vector2D) -> Vector2D:
        raise NotImplementedError
    
    def sign(self, v2: Vector2D) -> Vector2D:
        """ Returns positive if v2 is clockwise of this vector,
        and negative if counterclockwise
        """
        raise NotImplementedError

    def perp(self) -> Vector2D:
        raise NotImplementedError

    def truncate(self, maximum:float) -> None:
        raise NotImplementedError

    def distance(self, v2: Vector2D) -> float:
        raise NotImplementedError

    def distance_sq(self, v2: Vector2D) -> float:
        raise NotImplementedError

    def get_reverse(self) -> Vector2D:
        raise NotImplementedError
