"""
Advent of Code 2021 - Day 3, Part 1
Brian Bullis - brian [AT] bullis [DOT] me
"""

# Calculate the power consumption of the submarine from a debug report of lines of binary strings
if __name__ == '__main__':
    gamma = ''
    epsilon = ''
    with open('input.txt', 'r') as input_file:
        data = input_file.readlines()
        for i in data:
            i = i.strip('\n')
        # gamma is the most common bit in that position, epsilon is the least common - loop through each line and find
        for i in range(0, len(data[1]) - 1):
            zeroes = 0
            ones = 0
            for line in data:
                if line[i] == '0':
                    zeroes += 1
                else:
                    ones += 1
            if zeroes > ones:
                gamma += '0'
                epsilon += '1'
            else:
                gamma += '1'
                epsilon += '0'
        gamma_int = int(gamma, 2)
        epsilon_int = int(epsilon, 2)

        print("gamma rate:", gamma_int)
        print("epsilon rate:", epsilon_int)
        print("answer:", gamma_int * epsilon_int)
