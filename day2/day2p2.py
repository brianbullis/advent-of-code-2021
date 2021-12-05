"""
Advent of Code 2021 - Day 2, Part 2
Brian Bullis - brian [AT] bullis [DOT] me
"""

# Take in a file of submarine commands and determine its position at the end - now with another thing to track
if __name__ == '__main__':
    horizontal = 0
    depth = 0
    aim = 0

    with open('input.txt', 'r') as input_file:
        data = input_file.readlines()
        # read the commands, direction and distance separated by a space
        for line in data:
            direction = line.split(' ')[0]
            distance = int(line.split(' ')[1])
            # do the appropriate math based on what direction the sub is going
            if direction == 'forward':
                horizontal += distance
                depth += aim * distance
            elif direction == 'down':
                aim += distance
            elif direction == 'up':
                aim -= distance
        print("horizontal position:", horizontal)
        print("depth:", depth)
        print("answer:", horizontal * depth)
