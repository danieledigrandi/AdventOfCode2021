from day1 import get_mode


def open_file(path):

    with open(path, 'r') as f:
        file_lines = f.readlines()

    lines = []

    for line in file_lines:
        line = line.strip()
        lines.append(line)

    return lines


def get_score(parenthesis, mode):

    if parenthesis == ')':
        if mode == 1:
            return 3
        else:
            return 1

    elif parenthesis == ']':
        if mode == 1:
            return 57
        else:
            return 2

    elif parenthesis == '}':
        if mode == 1:
            return 1197
        else:
            return 3

    elif parenthesis == '>':
        if mode == 1:
            return 25137
        else:
            return 4


def parse(lines):

    errors = []
    non_corrupted = []

    for line in lines:

        stack = []
        corrupted = False

        for i, parenthesis in enumerate(line):
            if parenthesis == '(' or parenthesis == '[' or parenthesis == '{' or parenthesis == '<':

                stack.insert(0, parenthesis)

            if parenthesis == ')' or parenthesis == ']' or parenthesis == '}' or parenthesis == '>':

                opening_parenthesis = stack.pop(0)
                expression = opening_parenthesis + parenthesis

                if expression != '()' and expression != '[]' and expression != '{}' and expression != '<>':

                    corrupted = True
                    errors.append(parenthesis)
                    break

        if not corrupted:
            non_corrupted.append(line)

    score = 0

    for parenthesis in errors:

        score += get_score(parenthesis, mode=1)

    return score, errors, non_corrupted


def autocomplete(non_corrupted):

    last_parenthesis = []

    for line in non_corrupted:

        stack = []

        for i, parenthesis in enumerate(line):
            if parenthesis == '(' or parenthesis == '[' or parenthesis == '{' or parenthesis == '<':
                stack.insert(0, parenthesis)

            if parenthesis == ')' or parenthesis == ']' or parenthesis == '}' or parenthesis == '>':
                stack.pop(0)

        string = ''

        for parenthesis in stack:
            if parenthesis == '(':
                string += ')'
            elif parenthesis == '[':
                string += ']'
            elif parenthesis == '{':
                string += '}'
            else:
                string += '>'

        last_parenthesis.append(string)

    return last_parenthesis


def get_score_autocompletion(last_parenthesis):

    scores = []

    for string in last_parenthesis:

        score = 0

        for parenthesis in string:

            score *= 5
            score += get_score(parenthesis, mode=2)

        scores.append(score)

    scores.sort()

    middle = int(len(scores)/2)

    return scores[middle]


def main():
    path = "./data/input_day_10.txt"

    lines = open_file(path)

    mode = get_mode()

    if mode == 1:
        score, errors, non_corrupted = parse(lines)

        print("List of incorrect closing parentheses per line:", errors)
        print("Total syntax error score:", score)

    elif mode == 2:
        score, errors, non_corrupted = parse(lines)

        last_parenthesis = autocomplete(non_corrupted)
        score = get_score_autocompletion(last_parenthesis)

        print("List of parentheses to add in each line to have a complete sequence:", last_parenthesis)
        print("Middle score", score)


if __name__ == '__main__':
    main()
