from collections import defaultdict


def run(filepath):
    f = open(filepath, "r")
    left_numbers = []
    right_numbers = defaultdict(int)
    for line in f:
        numbers = line.split()
        left_numbers.append(int(numbers[0]))
        right_number = int(numbers[1])

        right_numbers[right_number] += 1

    total = 0
    for left_number in left_numbers:
        total += left_number * right_numbers[left_number]

    print(total)


if __name__ == "__main__":
    run("input.txt")