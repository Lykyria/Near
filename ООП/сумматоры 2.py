class Summator:
  def transform(self, n):
    return n

  def sum(self, N):
    result = 0
    for number in range(1, N + 1):
      result += self.transform(number)
    return result


class PowerSummator(Summator):
  def __init__(self, b):
    self.b = b
    
  def transform(self, n):
    return n ** self.b


class SquareSummator(PowerSummator):
  def __init__(self):
    super().__init__(2)


class CubeSummator(PowerSummator):
  def __init__(self):
    super().__init__(3)


x = Summator()
print(x.sum(3))
x = SquareSummator()
print(x.sum(3))
x = PowerSummator(4)
print(x.sum(3))
x = CubeSummator()
print(x.sum(3))