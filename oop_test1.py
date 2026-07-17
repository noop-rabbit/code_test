class Vector2D:
  def __init__(self, x: float, y: float):
    self.x = x
    self.y = y

  def __add__(self, other):
    if not isinstance(other, Vector2D):
      raise TypeError("Can only add Vector2D to Vector2D")

    return Vector2D(self.x + other.x, self.y + other.y)

  def __sub__(self, other):
    if not isinstance(other, Vector2D):
      raise TypeError("Can only subtract Vector2D from Vector2D")

    return Vector2D(self.x - other.x, self.y - other.y)

  def __eq__(self, other):
    return self.x == other.x and self.y == other.y

  def __repr__(self):
    return f"Vector2D({self.x}, {self.y})"

v1 = Vector2D(1, 2)
v2 = Vector2D(1, 2)
print(v1 + v2)
print(v1 - v2)
print(v1 == v2)
print(v1)        #---> try (v1 + 5), Will raise error, why? 5 doesn't have 5.x or 5.y