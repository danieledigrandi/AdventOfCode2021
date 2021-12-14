import copy
from day1 import get_mode


def open_file(path):

    with open(path, 'r') as f:
        lines = f.readlines()

    template = lines[0].strip()

    rules = {}

    for i in lines:
        if '->' in i:
            a, b = i.strip().split(' -> ')
            rules[a] = b

    return template, rules


def simulate(template, rules, num_iterations):

    counts = {key: 0 for key, value in rules.items()}

    letters = []

    # get the single letters
    for key, value in rules.items():
        if value not in letters:
            letters.append(value)

    single_letters = {letter: 0 for letter in letters}

    # initialise the dictionaries
    for pos in range(len(template) - 1):
        pair = template[pos] + template[pos + 1]
        counts[pair] += 1
        single_letters[template[pos]] += 1

    single_letters[template[-1]] += 1

    # the approach is like day6, store a count of pairs and iterate over it to generate new pairs
    # also, increment the count of the single letters while they are generated from a pair

    for _ in range(num_iterations):
        counts_iterable = copy.deepcopy(counts)
        for key, value in counts_iterable.items():
            if value != 0:
                counts[key] -= value
                counts[key[0] + rules[key]] += value
                counts[rules[key] + key[1]] += value
                single_letters[rules[key]] += value

    result = max(single_letters.values()) - min(single_letters.values())

    return result


def main():
    path = "./data/input_day_14.txt"
    template, rules = open_file(path)

    mode = get_mode()

    if mode == 1:
        num_iterations = 10
    elif mode == 2:
        num_iterations = 40

    result = simulate(template, rules, num_iterations)

    print("Most common element minus least common element:", result)


if __name__ == '__main__':
    main()
