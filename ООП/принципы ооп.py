class Bird:

  def __init__(self, name, size):
    self.name = name
    self.size = size

  def describe(self, full=False):
    return f'Название птицы - {self.name}, размер - {self.size}, цвет - {self.color}'


class Penguin(Bird):

  def __init__(self, name, size, genus):
    super().__init__(name, size)
    self.genus = genus

  def describe(self, full=False):
    if not full:
      return super().describe()
    else:
      return f'Размер пингвина {self.name} из рода {self.genus} - {self.size}. Интересный факт:...'

  def swimming(self):
    return f'Пингвин {self.name} плавает со средней скоростью 11 км/ч'


class Parrot(Bird):

  def __init__(self, name, size, color):
    super().__init__(name, size)
    self.color = color

  def describe(self, full=False):
    if not full:
      return super().describe()
    else:
      return (f'{self.name} - заметная прица,'
              f'окрас её перьев - {self.color}, '
              f'а размер - {self.size} Интересный факт:...')

  def repeat(self, phrase):
    return f'Попугай {self.name} говорит: {phrase}'


kesha = Parrot('Ара', 'средний', 'красный')
kowalski = Penguin('Королевский', 'большой', 'Aptenodytes')
print(kesha.repeat('добрый день'))
print(kesha.describe(True))
print(kowalski.swimming())
print(kowalski.describe(True))