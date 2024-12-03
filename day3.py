import re

def run(filepath):
    f = open(filepath, "r")
    total = 0
    should = True
    for line in f:
      equations = re.findall(r"mul\(\d+,\d+\)|don't\(\)|do\(\)", line)
      for equation in equations:
        if equation == "don't()":
          should = False
          continue
        elif equation == "do()":
          should = True
          continue
        elif should:
          numbers = [int(v) for v in re.findall(r"\d+", equation)]
          total += numbers[0] * numbers[1]

    print(total)

if __name__ == "__main__":
    run("input.txt")