from collections import defaultdict


def run(filepath):
  f = open(filepath, "r")
  #part1(f)
  part2(f)


def part2(f):
  antinodes = set()
  positions = defaultdict(list)
  max_width = 0
  max_height = 0
  for y_pos, line in enumerate(f):
    max_height += 1
    max_width = max_width or len(line.strip())
    for x_pos, value in enumerate(line.strip()):
      if value != ".":
        positions[value].append((x_pos, y_pos))

  for a_positions in positions.values():
    calculate_part2_antinodes(a_positions[0], a_positions[1:], antinodes, max_width, max_height)

  print(len(antinodes))


def calculate_part2_antinodes(position, positions, antinodes, max_width, max_height):
  if len(positions) == 0:
    return
  for right_position in positions:
    x_diff = position[0] - right_position[0]
    y_diff = position[1] - right_position[1]
    print(position, right_position, x_diff, y_diff)
    possible_antinodes = [
      (right_position[0] - x_diff, right_position[1] - y_diff),
      (position[0] + x_diff, position[1] + y_diff)
    ]
    multiple = 0
    keep_going = True
    while keep_going:
      antinode = (right_position[0] - x_diff * multiple, right_position[1] - y_diff * multiple)
      if antinode[0] >= 0 and antinode[1] >= 0 and antinode[0] < max_width and antinode[1] < max_height:
        antinodes.add(antinode)
        multiple += 1
      else:
        keep_going = False

    multiple = 0
    keep_going = True
    while keep_going:
      antinode = (right_position[0] + x_diff * multiple, right_position[1] + y_diff * multiple)
      if antinode[0] >= 0 and antinode[1] >= 0 and antinode[0] < max_width and antinode[1] < max_height:
        antinodes.add(antinode)
        multiple += 1
      else:
        keep_going = False
  calculate_part2_antinodes(positions[0], positions[1:], antinodes, max_width, max_height)


def part1(f):
  antinodes = set()
  positions = defaultdict(list)
  max_width = 0
  max_height = 0
  for y_pos, line in enumerate(f):
    max_height += 1
    max_width = max_width or len(line.strip())
    for x_pos, value in enumerate(line.strip()):
      if value != ".":
        positions[value].append((x_pos, y_pos))

  for a_positions in positions.values():
    calculate_antinodes(a_positions[0], a_positions[1:], antinodes, max_width, max_height)

  print(len(antinodes))

def calculate_antinodes(position, positions, antinodes, max_width, max_height):
  if len(positions) == 0:
    return
  for right_position in positions:
    x_diff = position[0] - right_position[0]
    y_diff = position[1] - right_position[1]
    print(position, right_position, x_diff, y_diff)
    possible_antinodes = [
      (right_position[0] - x_diff, right_position[1] - y_diff),
      (position[0] + x_diff, position[1] + y_diff)
    ]
    for antinode in possible_antinodes:
      if antinode[0] >= 0 and antinode[1] >= 0 and antinode[0] < max_width and antinode[1] < max_height:
        antinodes.add(antinode)
  calculate_antinodes(positions[0], positions[1:], antinodes, max_width, max_height)


if __name__ == "__main__":
    run("input.txt")