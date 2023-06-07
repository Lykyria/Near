def plus(a, b):
  c = a + b
  return c


def mins(a, b):
  c = a - b
  return c


def ymn(a, b):
  c = a * b
  return c


def delen(a, b):
  c = a / b
  return c


def arithmetic_operation(c):
  if c == '+':
    return plus
  if c == '-':
    return mins
  if c == '*':
    return ymn
  if c == '/':
    return delen


def main():
  c = input()
  operation = arithmetic_operation(c)
  print(operation(1, 4))


if __name__ == '__main__':
  main()
