class  Triangle:
  def __init__(self, a, b, c):
    self.a = a
    self.b = b
    self.c = c

  def perimeter(self):
    d = self.a + self.b + self.c
    return d


class EquilateralTriangle(Triangle):
  def __init__(self, side):
    super().__init__(side, side, side)


a = EquilateralTriangle(5)
print(a.perimeter())