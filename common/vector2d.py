from __future__ import annotations
from typing import Any, Literal

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
        return Vector2D(self.x + v2.x, self.y + v2.y)

    def __iadd__(self, v2: Vector2D) -> Vector2D:
        self.x += v2.x
        self.y += v2.y
        return self

    def __sub__(self, v2: Vector2D) -> Vector2D:
        return Vector2D(self.x - v2.x, self.y - v2.y)

    def __isub__(self, v2: Vector2D) -> Vector2D:
        self.x -= v2.x
        self.y -= v2.y
        return self

    def __mul__(self, other: float) -> Vector2D:
        return Vector2D(self.x * other, self.y * other)

    def __imul__(self, other: float) -> Vector2D:
        self.x *= other
        self.y *= other
        return self

    def __truediv__(self, other: float) -> Vector2D:
        return Vector2D(self.x / other, self.y / other)

    def __itruediv__(self, other: float) -> Vector2D:
        self.x /= other
        self.y /= other
        return self

    def length(self) -> float:
        return math.sqrt(self.length_sq())

    def length_sq(self) -> float:
        return self.x ** 2 + self.y ** 2

    def normalize(self) -> None:
        length = self.length()
        self.x /= length
        self.y /= length

    def dot(self, v2: Vector2D) -> float:
        return self.x * v2.x + self.y * v2.y
    
    def sign(self, v2: Vector2D) -> Literal[-1,1]:
        """ Returns positive if v2 is clockwise of this vector,
        and negative if counterclockwise
        """
        if self.y * v2.x > self.x * v2.y:
            return -1
        return 1

    def perp(self) -> Vector2D:
        return Vector2D(-self.y, self.x)

    def truncate(self, maximum:float) -> None:
        if self.length() > maximum:
            self.normalize()
            self.x *= maximum
            self.y *= maximum

    def distance(self, v2: Vector2D) -> float:
        return math.sqrt(self.distance_sq(v2))

    def distance_sq(self, v2: Vector2D) -> float:
        y_separation = v2.y - self.y
        x_separation = v2.x - self.x
        return y_separation ** 2 + x_separation ** 2

    def get_reverse(self) -> Vector2D:
        return Vector2D(-self.x, -self.y)
