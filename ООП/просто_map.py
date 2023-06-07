def simple_map(transformation, values):
  list_res = []
  for value in values:
    list_res.append(transformation(value))
  return list_res


def main():
  values = [1, 3, 1, 5, 7]
  print(*simple_map(lambda x: x + 5, values))


if __name__ == '__main__':
  main()