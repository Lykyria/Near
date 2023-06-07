class Summator:
  def transform(self, n):
    return n

  def sum(self, N):
    result = 0
    for number in range(1, N + 1):
      result += self.transform(number)
    return result


class SquareSummator(Summator):
  def transform(self, n):
    return n ** 2


class CubeSummator(Summator):
  def transform(self, n):
    return n ** 3


x = Summator()
print(x.sum(3))
x = SquareSummator()
print(x.sum(3))
x = CubeSummator()
print(x.sum(3))