"""
Advent of Code 2021 - Day 1, Part 2
Brian Bullis - brian [AT] bullis [DOT] me
"""

# Take in a file of depth readings, group them into sums of 3, and count how many times the sum increased over the last
if __name__ == '__main__':
    with open('input.txt', 'r') as input_file:
        data = input_file.readlines()
        grouped = []
        ints = []
        # convert the strings to ints
        for i in data:
            ints.append(int(i.strip('\n')))

        # make a list of the sums of groupings of 3 depth readings
        for i in range(0, len(ints) - 2):
            grouped.append(ints[i] + ints[i + 1] + ints[i + 2])
        increases = 0

        # count how many times the sum increased compared to the previous one
        for i in range(1, len(grouped)):
            if grouped[i] > grouped[i-1]:
                increases += 1

        print(increases)
