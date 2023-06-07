class Balance:

  def __init__(self):
    self.balanse = 0

  def add_right(self, ves):
    self.balanse += ves

  def add_left(self, ves):
    self.balanse -= ves

  def result(self):
    if self.balanse < 0:
      return 'L'
    elif self.balanse > 0:
      return 'R'
    else:
      return '='


balance = Balance()
balance.add_right(10)
balance.add_left(9)
balance.add_left(2)
print(balance.result())
