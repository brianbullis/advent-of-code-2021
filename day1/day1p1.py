"""
Advent of Code 2021 - Day 1, Part 1
Brian Bullis - brian [AT] bullis [DOT] me
"""

# Take in a file of depth readings and count how many times the depth increased from the previous line
if __name__ == '__main__':
    with open('input.txt', 'r') as input_file:
        data = input_file.readlines()
        ints = []
        # convert the strings to ints
        for i in data:
            ints.append(int(i.strip('\n')))

        increases = 0

        # count how many times the depth increased compared to the previous reading
        for i in range(1, len(ints)):
            if ints[i] > ints[i-1]:
                increases += 1

        print(increases)
