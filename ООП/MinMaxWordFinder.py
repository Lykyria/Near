class MinMaxWordFinder:

  def __init__(self):
    self.full_sentence = []
    self.long_list = []
    self.short_list = []

  def add_sentence(self, tekst):
    self.full_sentence.extend(tekst.split())
    a = min(self.full_sentence, key=len)
    b = max(self.full_sentence, key=len)
    self.short_list = []
    self.long_list = []
    for i in self.full_sentence:
      if len(i) == len(a):
        self.short_list.append(i)
      if len(i) == len(b):
        self.long_list.append(i)

  def longest_words(self):
    self.long_list.sort()
    return self.long_list

  def shortest_words(self):
    self.short_list.sort()
    return self.short_list


finder = MinMaxWordFinder()
finder.add_sentence('hello')
finder.add_sentence('abc')
finder.add_sentence('world')
finder.add_sentence('def')
finder.add_sentence('asdf')
finder.add_sentence('qwert')
print(' '.join(finder.shortest_words()))
print(' '.join(finder.longest_words()))