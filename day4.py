import re

def run(filepath):
  f = open(filepath, "r")
  total = 0

  matrix = []
  for line in f:
    matrix.append(line.strip())

  for row_index, row in enumerate(matrix):
    if row_index < 2:
      continue
    for letter_index in range(len(row)):
      if letter_index < 2:
        continue
      diag_right = matrix[row_index - 2][letter_index - 2] + matrix[row_index - 1][letter_index - 1] + matrix[row_index][letter_index]
      diag_left = matrix[row_index - 2][letter_index] + matrix[row_index - 1][letter_index - 1] + matrix[row_index][letter_index - 2]
      if diag_right in VALID_MATCHES and diag_left in VALID_MATCHES:
        total += 1

  print(total)

VALID_MATCHES = ["MAS", "SAM"]
FOUND_MATCHES = {}

def check_horizontal(letter_index, row):
  if row[letter_index - 3:letter_index + 1] in VALID_MATCHES:
    return 1

  return 0

def check_vertical(row_index, letter_index, matrix):
  options = []

  if row_index > 2:
    options.append(
      matrix[row_index - 3][letter_index] + matrix[row_index - 2][letter_index] + matrix[row_index - 1][letter_index] + matrix[row_index][letter_index]
    )

  if any(option in VALID_MATCHES for option in options):
    return 1
  return 0

def check_left_diagonal(row_index, letter_index, matrix):
  options = []

  if row_index > 2 and letter_index > 2:
    options.append(
      matrix[row_index - 3][letter_index - 3] + matrix[row_index - 2][letter_index - 2] + matrix[row_index - 1][letter_index - 1] + matrix[row_index][letter_index]
    )
  if any(option in VALID_MATCHES for option in options):
    return 1
  return 0

def check_right_diagonal(row_index, letter_index, matrix):
  options = []
  if row_index > 2 and letter_index < len(matrix[row_index]) - 3:
    options.append(
      matrix[row_index - 3][letter_index + 3] + matrix[row_index - 2][letter_index + 2] + matrix[row_index - 1][letter_index + 1] + matrix[row_index][letter_index]
    )
  if any(option in VALID_MATCHES for option in options):
    return 1
  return 0

if __name__ == "__main__":
    run("input.txt")