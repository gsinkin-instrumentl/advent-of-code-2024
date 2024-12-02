
def run(filepath):
    f = open(filepath, "r")
    safe_levels = 0
    for report in f:
        levels = [int(v) for v in report.split()]
        direction = 1
        if levels[-1] < levels[0]:
            direction = -1

        if validate_level(levels, direction) or any(
           validate_level(levels[:index:] + levels[index + 1:], direction) for index in range(len(levels))
        ):
            safe_levels += 1

    print(safe_levels)


def validate_level(level, direction):
    left_value = None
    level = level[::direction]
    for value in level:
        if left_value == None:
            left_value = value
            continue

        difference = value - left_value

        # print(left_value, value, difference, skipped)

        if abs(difference) > 3 or difference <= 0:
            print(f"{level} is no good")
            return False

        left_value = value
    print(f"{level} is good")
    return True

if __name__ == "__main__":
    run("input.txt")