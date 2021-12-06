import copy
from day1 import get_mode


def open_file(path):

    with open(path, 'r') as f:
        lines = f.readlines()

    fishes_str = lines[0].strip().split(',')

    fishes = list(map(int, fishes_str))

    return fishes


def get_count(fishes):

    fishes_count = {}

    for i in range(9):
        fishes_count[i] = fishes.count(i)

    return fishes_count


def main():
    path = "./data/input_day_6.txt"

    fishes = open_file(path)
    fishes_count = get_count(fishes)
    fishes_count_copy = copy.deepcopy(fishes_count)

    day = 0

    mode = get_mode()

    if mode == 1:
        max_days = 80
    elif mode == 2:
        max_days = 256

    while day < max_days:
        # The idea is to group similar fishes in a dictionary that acts as a counter and has as keys
        # the possible days (0..8) and as values the number of fishes with those days left before reproducing

        # Then, move accordingly the values of the dictionary to simulate that fishes are decreasing their days
        # finally, add the number of fishes with 0 days left to the key 6 and substitute them to the key 8
        # to simulate the new fishes

        for key, value in fishes_count.items():

            if key == 0:
                value_0 = value  # store the value of key 0 before it is subscripted by the value of key 1
            else:
                fishes_count_copy[key - 1] = value

        fishes_count_copy[6] += value_0
        fishes_count_copy[8] = value_0

        fishes_count = copy.deepcopy(fishes_count_copy)

        day += 1

    sum_ = 0
    for key, value in fishes_count.items():
        sum_ += value

    print("Number of fishes after", day, "days:", sum_)


if __name__ == '__main__':
    main()
