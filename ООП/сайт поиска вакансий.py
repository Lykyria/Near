class Profile:

  def __init__(self, name):
    self.name = name

  def info(self):
    return ''

  def describe(self):
    print(self.name, self.info())


class Vacancy(Profile):

  def __init__(self, name, zp):
    super().__init__(name)
    self.zp = zp

  def info(self):
    return f'Предлагаемая зарплата: {self.zp}'


class Resume(Profile):

  def __init__(self, name, staj):
    super().__init__(name)
    self.staj = staj

  def info(self):
    return f'Стаж работы: {self.staj}'


x = Vacancy('prom', 19394)
print(x.info())
x.describe()