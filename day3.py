from collections import Counter
import copy
from day1 import get_mode


def open_file(path):

    with open(path, 'r') as f:
        lines = f.readlines()

    diagnostic_report = [instr.strip('\n') for instr in lines]

    return diagnostic_report


def arrange(diagnostic_report):

    re_ordered = []

    for i in range(len(diagnostic_report[0])):
        string = ''
        for number in diagnostic_report:
            string += number[i]
        re_ordered.append(string)

    return re_ordered


def extract_rates(re_ordered):

    gamma_rate_bin = ''
    epsilon_rate_bin = ''

    for i in re_ordered:

        k = Counter(i)
        most_common = k.most_common(1)

        num_gamma = most_common[0][0]
        num_epsilon = str(1 - int(num_gamma))

        gamma_rate_bin += num_gamma
        epsilon_rate_bin += num_epsilon

    gamma_rate = int(gamma_rate_bin, 2)
    epsilon_rate = int(epsilon_rate_bin, 2)

    return gamma_rate, epsilon_rate


def extract_single_rate(report_copy, mode):

    # mode can be either 'o2' or 'co2'

    bit_tracker = 0

    while len(report_copy) > 1:

        string = ''
        for number in report_copy:
            string += number[bit_tracker]

        k = Counter(string)
        most_common_list = k.most_common(2)

        if mode == 'o2':
            if most_common_list[0][1] == most_common_list[1][1]:
                target = '1'
            else:
                target = most_common_list[0][0]

        elif mode == 'co2':
            if most_common_list[0][1] == most_common_list[1][1]:
                target = '0'
            else:
                target = most_common_list[1][0]

        to_eliminate = [number for number in report_copy if number[bit_tracker] != target]

        for number in to_eliminate:
            report_copy.remove(number)

        bit_tracker += 1

    rating = int((report_copy[0]), 2)

    return rating


def extract_o2_co2(diagnostic_report):

    report_copy_o2 = copy.deepcopy(diagnostic_report)
    report_copy_co2 = copy.deepcopy(diagnostic_report)

    oxygen_generator_rating = extract_single_rate(report_copy_o2, mode='o2')
    co2_scrubber_rating = extract_single_rate(report_copy_co2, mode='co2')

    return oxygen_generator_rating, co2_scrubber_rating


def main():
    path = './data/input_day_3.txt'
    diagnostic_report = open_file(path)

    mode = get_mode()

    if mode == 1:
        re_ordered = arrange(diagnostic_report)

        gamma_rate, epsilon_rate = extract_rates(re_ordered)
        power_consumption = gamma_rate * epsilon_rate

        print("Gamma rate:", gamma_rate)
        print("Epsilon rate:", epsilon_rate)
        print("Power consumption:", power_consumption)

    elif mode == 2:
        oxygen_generator_rating, co2_scrubber_rating = extract_o2_co2(diagnostic_report)
        life_support_rating = oxygen_generator_rating * co2_scrubber_rating

        print("Oxygen generator rating:", oxygen_generator_rating)
        print("CO2 scrubber rating:", co2_scrubber_rating)
        print("Life support rating:", life_support_rating)


if __name__ == '__main__':
    main()
