from day1 import get_mode

"""
num     len         correct

1   ->  len 2   ->  cf
4   ->  len 4   ->  bcdf
7   ->  len 3   ->  acf
8   ->  len 7   ->  abcdefg

0   ->  len 6   ->  abcefg
2   ->  len 5   ->  acdeg
3   ->  len 5   ->  acdfg
5   ->  len 5   ->  abdfg
6   ->  len 6   ->  abdefg
9   ->  len 6   ->  abcdfg

To understand the pattern and decrypt the numbers, let's define some rules

RULES
1) 2 is the only one that doesn't have f -> a letter present in each number but one, is mapped as f
2) knowing f, I can deduce c: a number of len 2 must be a 1 (composed by cf), hence the letter that is not
   a f must be a c
3) knowing c, I can discriminate between 3 and 5: 3 contains c and 5 doesn't. Hence I can map
   the letter in 5 that is not c and is not in 3 as b
4) 4 is composed by bcdf and I can map b, c and f. This means that the last letter in a 4 is mapped as d
5) 0 is the only number of len 6 that has not a d inside
6) if the len is 6 and both c and d are present, it must be a 9
7) if the len is 6 and d is present but not c, it must be a 6

CAN DEDUCE
0, 1, 2, 3, 4, 5, 6, 7, 8, 9

CAN MAP
f, c, b, d

But it is enough to deduce all numbers.
"""


def open_file(path):

    with open(path, 'r') as f:
        lines = f.readlines()

    entries = []

    for entry in lines:
        patterns, output = entry.split(' | ')
        entries.append([patterns.split(), output.split()])

    return entries


def decrypt(entries):

    output_values = []

    for entry in entries:
        letter_mapping = {'a': -1, 'b': -1, 'c': -1, 'd': -1, 'e': -1, 'f': -1, 'g': -1}

        # rule 1
        for key in letter_mapping:
            num_times = sum(key in s for s in entry[0])  # count how many times a letter is present in the list

            if num_times == 9:  # f is present in only 9 numbers
                letter_mapping['f'] = key
                break

        for number in entry[0]:
            if letter_mapping['f'] not in number:
                two = number

            # additional rules from part one to catch a 7 or an 8
            if len(number) == 3:
                seven = number

            if len(number) == 7:
                eight = number

        # rule 2
        for number in entry[0]:
            if len(number) == 2:
                one = number
                letter_mapping['c'] = one.replace(letter_mapping['f'], '')
                break

        # rule 3
        for number in entry[0]:
            if len(number) == 5 and letter_mapping['c'] in number and number != two:
                three = number

            if len(number) == 5 and letter_mapping['c'] not in number and number != two:
                five = number

        for char in five:
            if char not in three:
                letter_mapping['b'] = char
                break

        # rule 4
        for number in entry[0]:
            if len(number) == 4:
                four = number
                bcf = letter_mapping['b'] + letter_mapping['c'] + letter_mapping['f']
                final = four.strip(bcf)
                letter_mapping['d'] = final

        # rule 5
        for number in entry[0]:
            if len(number) == 6 and letter_mapping['d'] not in number:
                zero = number

            # rule 6
            if len(number) == 6 and letter_mapping['d'] in number and letter_mapping['c'] in number:
                nine = number

            #rule 7
            if len(number) == 6 and letter_mapping['d'] in number and letter_mapping['c'] not in number:
                six = number

        # map the output with the found numbers
        value = ''

        for number in entry[1]:

            # sort the string because the output can have a different letters order than the pattern
            number_sorted = ''.join(sorted(number))

            if number_sorted == ''.join(sorted(zero)):
                value += '0'
            if number_sorted == ''.join(sorted(one)):
                value += '1'
            if number_sorted == ''.join(sorted(two)):
                value += '2'
            if number_sorted == ''.join(sorted(three)):
                value += '3'
            if number_sorted == ''.join(sorted(four)):
                value += '4'
            if number_sorted == ''.join(sorted(five)):
                value += '5'
            if number_sorted == ''.join(sorted(six)):
                value += '6'
            if number_sorted == ''.join(sorted(seven)):
                value += '7'
            if number_sorted == ''.join(sorted(eight)):
                value += '8'
            if number_sorted == ''.join(sorted(nine)):
                value += '9'

        output_values.append(int(value))

    return output_values


def main():
    path = "./data/input_day_8.txt"

    entries = open_file(path)

    mode = get_mode()

    if mode == 1:
        sum_ = 0

        for entry in entries:
            for value in entry[1]:
                if len(value) == 2 or len(value) == 3 or len(value) == 4 or len(value) == 7:
                    sum_ += 1

        print(f"1, 4, 7 and 8 appear: {sum_} times")

    elif mode == 2:
        output_values = decrypt(entries)
        sum_ = sum(output_values)

        print(f"The sum of all output values is: {sum_}")


if __name__ == '__main__':
    main()
