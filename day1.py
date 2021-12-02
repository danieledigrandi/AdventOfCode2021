def open_file(path):

    with open(path, 'r') as f:
        lines = f.readlines()

    measurements = [int(measure.strip('\n')) for measure in lines]
    return measurements


def compute_changing(measurements):

    change = []

    for i in range(1, len(measurements)):
        if measurements[i] < measurements[i - 1]:
            change.append('decreased')

        elif measurements[i] == measurements[i - 1]:
            change.append('no change')

        else:
            change.append('increased')

    return change


def compute_3_window(measurements):

    sliding_3_sum = []

    for i in range(2, len(measurements)):

        sliding_3_sum.append(measurements[i - 2] + measurements[i - 1] + measurements[i])

    return(sliding_3_sum)


def main(mode=1):

    path = './data/input_day_1_1.txt'
    measurements = open_file(path)

    if mode == 1:
        change = compute_changing(measurements)
        print(change.count('increased'))

    elif mode == 2:
        sliding_3_sum = compute_3_window(measurements)
        change = compute_changing(sliding_3_sum)
        print(change.count('increased'))


if __name__ == '__main__':
    main(mode=2)