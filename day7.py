import numpy as np
from day1 import get_mode


def open_file(path):

    with open(path, 'r') as f:
        lines = f.readlines()

    crabs_str = lines[0].strip().split(',')

    crabs = list(map(int, crabs_str))

    return crabs


def median_(crabs):

    crabs = np.asarray(crabs)
    crabs = np.sort(crabs)
    return int(np.median(crabs))


def get_distances(crabs, mean_value):

    distances = []

    for crab in crabs:
        steps = np.absolute(crab - mean_value)

        sum_ = 0
        for i in range(1, steps + 1):
            sum_ += i

        distances.append(sum_)

    return distances


def main():
    path = "./data/input_day_7.txt"
    crabs = open_file(path)

    mode = get_mode()

    if mode == 1:
        # What the problem is really asking is to find the median of the position array of crabs
        # In fact, the median corresponds to the middle number of the sorted array,
        # which is the value that is closest to all the other values thus minimizes the distances

        median_value = median_(crabs)
        distances = [np.absolute(crab - median_value) for crab in crabs]
        sum_ = sum(distances)

        print("Optimum horizontal position:", median_value)
        print("Minimum total fuel cost is:", sum_)

    elif mode == 2:
        # In the second part, it is possible to find the optimal horizontal by averaging the
        # positions of the crabs. Since the average is a floating point number and we are searching
        # for an integer number, the fuel answer can be found either by rounding down or rounding up.
        # The fastest way for this challenge, is to print both of them and try to input both
        # in the website to see which one is correct.
        # For my puzzle input: the correct one was rounding down.

        mean = sum(crabs) / len(crabs)
        mean_low = int(mean)
        mean_high = int(round(mean))

        distances_low = get_distances(crabs, mean_low)
        distances_high = get_distances(crabs, mean_high)

        sum_low = sum(distances_low)
        sum_high = sum(distances_high)

        print(f"Optimum horizontal position can either be: {mean_low} or {mean_high}")
        print(f"Minimum total fuel cost for {mean_low} is {sum_low}, for {mean_high} is {sum_high}")


if __name__ == '__main__':
    main()
