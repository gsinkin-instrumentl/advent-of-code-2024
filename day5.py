from collections import defaultdict
from itertools import permutations


def run(filepath):
  f = open(filepath, "r")
  to_total = []

  before_rules = defaultdict(set)
  for line in f:
    line = line.strip()
    if "|" in line:
      page, before = line.split("|")
      before_rules[int(page)].add(int(before))
    elif line:
      values = [int(v) for v in line.split(",")]
      if valid_values(values, before_rules):
        pass
      else:
        reordered_values = reorder_values(values, before_rules)
        print(f"{reordered_values} is valid!")
        to_total.append(reordered_values[int(len(reordered_values) / 2)])

  print(sum(to_total))


def reorder_values(values, before_rules):
  collected_values = []

  for index, value in enumerate(values):
    if index == 0:
      collected_values.append(value)
      continue

    rules = before_rules[value]
    if not rules:
      collected_values.append(value)
      continue

    inserted = False
    for left_index, left_value in enumerate(collected_values[:index]):
      if left_value in rules:
        collected_values.insert(left_index, value)
        inserted = True
        break
    if not inserted:
      collected_values.append(value)
  return collected_values


def valid_values(values, before_rules):
  disallowed_values = set()
  for index, value in enumerate(values):
    if value in before_rules:
      disallowed_values.add(value)
    if index == 0:
      # first value is always valid
      continue
    rules = before_rules[value]
    if disallowed_values & rules:
      return False

  return True


if __name__ == "__main__":
    run("input.txt")