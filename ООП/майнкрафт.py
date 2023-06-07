class BaseObject:

  def __init__(self, x, y, z):
    self.x = x
    self.y = y
    self.z = z

  def get_coordinates(self):
    return [self.x, self.y, self.z]


class Block(BaseObject):

  def shetter(self):
    self.x = 0
    self.y = 0
    self.z = 0


class Entity(BaseObject):

  def move(self, x1, y1, z1):
    self.x = x1
    self.y = y1
    self.z = z1


class Thing(BaseObject):
  ...


a = Block(1, 3, 4)
a.shetter()
print(a.get_coordinates())
a = Entity(1, 3, 4)
a.move(9, 9, 9)
print(a.get_coordinates())