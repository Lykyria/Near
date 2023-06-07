class User:
  def __init__(self, name):
    self.user_name = name

  def send_message(self, user, message):
    print(f"{self.user_name} отправляет сообщение {user.user_name}"
          f' Cодержимое: {message}')

  def  post(self, message):
    print(f'{self.user_name} cделал новую публикацию')

  def info(self):
    return ''

  def describe(self):
    print(f'Имя: {self.user_name}, '
          f'краткое описание: {self.info()}')


class Person(User):
  def __init__(self, name, data):
    super().__init__(name)
    self.data = data

  def info1(self):
    return f'Дата рождения: {self.data}'

  def subscribe(self, user):
    print(f'{self.user_name} подписался на {user.user_name}')


class Community(User):
  def __init__(self, name, op):
    self.us_grup = name
    self.op = op

  def info2(self):
    return f'Описание: {self.op}'

lykyria = User('lykyr')
gleb = User('Глеб')
lykyria.send_message(gleb, "Hello my friend!")