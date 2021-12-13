"""
if fold on y:

new_position_x = old_position_x
new_position_y = 2 * fold_position - old_position_y

if fold on x:

new_position_y = old_position_y
new_position_x = 2 * fold_position - old_position_x
"""

from day1 import get_mode


class Paper:

    def __init__(self, dots):

        self.dots = dots
        self.max_x = 0
        self.max_y = 0

    def fold_x(self, num):

        for pos in range(len(self.dots)):
            if self.dots[pos][0] > num:
                self.dots[pos][0] = 2 * num - self.dots[pos][0]

        # remove duplicate points:
        new_points = []
        for point in self.dots:
            if point not in new_points:
                new_points.append(point)
        self.dots = new_points

        # update maximum for correctly printing the paper
        self.max_x -= num + 1

    def fold_y(self, num):

        for pos in range(len(self.dots)):
            if self.dots[pos][1] > num:
                self.dots[pos][1] = 2 * num - self.dots[pos][1]

        # remove duplicate points:
        new_points = []
        for point in self.dots:
            if point not in new_points:
                new_points.append(point)
        self.dots = new_points

        # update maximum for correctly printing the paper
        self.max_y -= num + 1

    def get_initial_max(self):

        for elem in self.dots:

            x = elem[0]
            y = elem[1]

            if x > self.max_x:
                self.max_x = x
            if y > self.max_y:
                self.max_y = y

    def print_paper(self):

        for pos_y in range(self.max_y + 1):
            string = ''
            for pos_x in range(self.max_x + 1):
                if [pos_x, pos_y] in self.dots:
                    string += '#'
                else:
                    string += ' '
            print(string)

    def count_dots(self):

        return len(self.dots)


def open_file(path):

    with open(path, 'r') as f:
        lines = f.readlines()

    dots = []
    instructions = []

    for i in lines:
        if ',' in i:
            dots.append(list(map(int, i.strip().split(','))))

        elif 'fold' in i:
            a, num = i.strip().split('=')
            num = int(num)
            instructions.append((a[-1], num))

    return dots, instructions


def main():
    path = "./data/input_day_13.txt"

    dots, instructions = open_file(path)

    paper = Paper(dots=dots)
    paper.get_initial_max()

    mode = get_mode()

    if mode == 1:
        if instructions[0][0] == 'x':
            paper.fold_x(num=instructions[0][1])
        else:
            paper.fold_y(num=instructions[0][1])

        num = paper.count_dots()
        print("Visible dots after completing just the first fold:", num)

    elif mode == 2:
        for instruction in instructions:
            if instruction[0] == 'x':
                paper.fold_x(num=instruction[1])
            else:
                paper.fold_y(num=instruction[1])

        print("Code to activate the infrared camera (read the 8 capital letters here):")
        paper.print_paper()


if __name__ == '__main__':
    main()
