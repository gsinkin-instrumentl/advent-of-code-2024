import re
from collections import defaultdict


def run(filepath):
  f = open(filepath, "r")

  # position : collection of directions when visiting the position
  visited_positions = defaultdict(set)
  current_position = None
  current_direction = None
  matrix = []
  for y_pos, line in enumerate(f):
    values = [v for v in line.strip()]
    found = re.search(r"<|>|\^|v", line)
    if found:
      current_position = (line.index(found.group()), y_pos)
      match found.group():
        case "<":
          current_direction = (-1, 0)
        case ">":
          current_direction = (1, 0)
        case "^":
          current_direction = (0, -1)
        case _:
          current_direction = (0, 1)
      visited_positions[current_position].add(current_direction)
    matrix.append(values)

  part_one(matrix, current_position, current_direction, visited_positions)
  part_two(matrix, current_position, current_direction, visited_positions)


def part_two(matrix, initial_position, current_direction, visited_positions):
  positions_to_verify = set([k for k,v in visited_positions.items() if len(v) > 0 and k != initial_position])

  valid_blockers = set()
  import pdb; pdb.set_trace()
  for position_to_verify in positions_to_verify:
    if position_to_verify in valid_blockers:
      continue
    matrix[position_to_verify[1]][position_to_verify[0]] = "#"
    if blocked_matrix(matrix, initial_position, current_direction):
      valid_blockers.add(position_to_verify)
    matrix[position_to_verify[1]][position_to_verify[0]] = "X"
  pretty_print(matrix)
  print(len(valid_blockers))

def blocked_matrix(matrix, current_position, current_direction):
  visited_positions = defaultdict(set)
  visited_positions[current_position].add(current_direction)
  max_width = len(matrix[0])
  max_height = len(matrix)
  infinite_loop = False

  while True:
    next_position = (current_position[0] + current_direction[0], current_position[1] + current_direction[1])
    if (next_position[0] == -1 or next_position[0] == max_width or next_position[1] == -1 or next_position[1] == max_height):
      break
    if current_direction in visited_positions[next_position]:
      infinite_loop = True
      break
    while matrix[next_position[1]][next_position[0]] == "#":
      current_direction = turn_90(current_direction)
      next_position = (current_position[0] + current_direction[0], current_position[1] + current_direction[1])
      if next_position[0] == -1 or next_position[0] == max_width or next_position[1] == -1 or next_position[1] == max_height:
        break
      if current_direction in visited_positions[next_position]:
        infinite_loop = True
        break
    visited_positions[next_position].add(current_direction)
    symbol = matrix[next_position[1]][next_position[0]]
    match current_direction:
      case (-1, 0) | (1, 0):
        if symbol == "|":
          symbol = "+"
        elif symbol == ".":
          symbol = "-"
      case (0, -1) | (0, 1):
        if symbol == "-":
          symbol = "+"
        elif symbol == ".":
          symbol = "|"
    matrix[next_position[1]][next_position[0]] = symbol
    current_position = next_position

  return infinite_loop


def part_one(matrix, current_position, current_direction, visited_positions):
  max_width = len(matrix[0])
  max_height = len(matrix)
  infinite_loop = False

  while True:
    next_position = (current_position[0] + current_direction[0], current_position[1] + current_direction[1])
    if (next_position[0] == -1 or next_position[0] == max_width or next_position[1] == -1 or next_position[1] == max_height):
      break
    if current_direction in visited_positions[next_position]:
      infinite_loop = True
      break
    while matrix[next_position[1]][next_position[0]] == "#":
      current_direction = turn_90(current_direction)
      next_position = (current_position[0] + current_direction[0], current_position[1] + current_direction[1])
      if next_position[0] == -1 or next_position[0] == max_width or next_position[1] == -1 or next_position[1] == max_height:
        break
    visited_positions[next_position].add(current_direction)
    symbol = matrix[next_position[1]][next_position[0]]
    match current_direction:
      case (-1, 0) | (1, 0):
        if symbol == "|":
          symbol = "+"
        elif symbol == ".":
          symbol = "-"
      case (0, -1) | (0, 1):
        if symbol == "-":
          symbol = "+"
        elif symbol == ".":
          symbol = "|"
    matrix[next_position[1]][next_position[0]] = symbol
    current_position = next_position

  pretty_print(matrix)
  print(len([v for v in visited_positions.values() if len(v) > 0]))
  print(f'infinite loop: {infinite_loop}')
  return infinite_loop


def turn_90(current_direction):
  match current_direction:
    case (0, 1):
      return (-1, 0)
    case (0, -1):
      return (1, 0)
    case (1, 0):
      return (0, 1)
    case (-1, 0):
      return (0, -1)


def pretty_print(matrix):
   print("")
   for line in matrix:
      print("".join(line))
   print("")


if __name__ == "__main__":
    run("input.txt")