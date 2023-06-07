class OddEvenSeparator:
  def __init__(self):
    self.even_list = []
    self.odd_list = []
  
  def add_number(self, a):
    if a % 2 == 0:
      self.even_list.append(a)
    else:
      self.odd_list.append(a)
  
  def even(self):
    return self.even_list
    
  def odd(self):
    return self.odd_list


separator = OddEvenSeparator()
separator.add_number(1)
separator.add_number(5)
separator.add_number(6)
separator.add_number(8)
separator.add_number(3)
print(' '.join(map(str, separator.even())))
print(' '.join(map(str, separator.odd())))