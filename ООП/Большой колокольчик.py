class BigBell:

  def __init__(self):
    self.n = 0

  def sound(self):
    self.n += 1
    if self.n % 2 == 1:
      print('ding')
    else:
      print('dong')


bell = BigBell()
bell.sound()
bell.sound()
bell.sound()