class Bird:

  def __init__(self, name, size):
    self.name = name
    self.size = size

  def describe(self):
    return f'Название птицы - {self.name}, размер - {self.size}, цвет - {self.color}'


class Penguin(Bird):

  def __init__(self, name, size, genus):
    super().__init__(name, size)
    self.genus = genus


class Parrot(Bird):

  def __init__(self, name, size, color):
    super().__init__(name, size)
    self.color = color


kesha = Parrot('Ара', 'средний', 'красный')
kowalski = Parrot('Королевский', 'большой', 'Aptenodytes')
print(kesha.describe())
print(kowalski.describe())