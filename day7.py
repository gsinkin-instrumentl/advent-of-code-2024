import re
from itertools import product


def run(filepath):
  f = open(filepath, "r")
  #part1(f)
  part2(f)


def part2(f):
  valid_sum = 0
  for line in f:
    total = re.search(r"\d+:", line).group()
    values = [int(v) for v in line.replace(total, "").strip().split()]
    total = int(total[:-1])

    for operations in product(range(3), repeat=len(values) - 1):
      interim_total = values[0]

      for index, value in enumerate(values[1:]):
        operation = operations[index]
        if operation == 0:
          interim_total += value
        elif operation == 1:
          interim_total *= value
        else:
          interim_total *= pow(10, len(str(value)))
          interim_total += value

        if interim_total > total:
          break
      if interim_total == total:
        valid_sum += total
        break

  print(valid_sum)


def part1(f):
  valid_sum = 0
  for line in f:
    total = re.search(r"\d+:", line).group()
    values = [int(v) for v in line.replace(total, "").strip().split()]
    total = int(total[:-1])

    for operations in product(range(2), repeat=len(values) - 1):
      interim_total = values[0]

      for index, value in enumerate(values[1:]):
        operation = operations[index]
        if operation == 0:
          interim_total += value
        else:
          interim_total *= value
        if interim_total > total:
          break
      if interim_total == total:
        valid_sum += total
        break

  print(valid_sum)


if __name__ == "__main__":
    run("input.txt")