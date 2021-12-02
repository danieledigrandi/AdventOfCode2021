from day1 import get_mode


class Submarine_pt1:

    def __init__(self, horizontal: int = 0, depth: int = 0):

        self.horizontal = horizontal
        self.depth = depth

    def forward(self, value: int):

        self.horizontal += value

    def up(self, value: int):

        self.depth -= value

    def down(self, value: int):

        self.depth += value


class Submarine_pt2:

    def __init__(self, horizontal: int = 0, depth: int = 0, aim: int = 0):

        self.horizontal = horizontal
        self.depth = depth
        self.aim = aim

    def forward(self, value: int):

        self.horizontal += value
        self.depth += self.aim * value

    def up(self, value: int):

        self.aim -= value

    def down(self, value: int):

        self.aim += value


def open_file(path):

    instructions = []

    with open(path, 'r') as f:
        lines = f.readlines()

    raw_data = [instr.strip('\n') for instr in lines]

    for i in raw_data:
        split = i.split()
        instructions.append((split[0], int(split[1])))

    return instructions


def move(submarine, instructions, class_):

    for instr in instructions:

        # Here, call the method directly with the instance contained in instr[0]
        # For example, if instr[0] == 'forward', is like writing submarine.forward(instr[1])
        # The 2 lines of code below do exactly the same thing, but now is parametrized
        # for any possible value of instr[0]

        class_method = getattr(class_, instr[0])
        class_method(submarine, instr[1])

    return submarine


def main():

    path = './data/input_day_2.txt'
    instructions = open_file(path)

    mode = get_mode()

    if mode == 1:
        submarine = Submarine_pt1()

        submarine_moved = move(submarine, instructions, Submarine_pt1)

        result = submarine_moved.horizontal * submarine_moved.depth

        print("Horizontal:", submarine_moved.horizontal)
        print("Depth:", submarine_moved.depth)
        print("Multiplied:", result)

    elif mode == 2:
        submarine = Submarine_pt2()

        submarine_moved = move(submarine, instructions, Submarine_pt2)

        result = submarine_moved.horizontal * submarine_moved.depth

        print("Horizontal:", submarine_moved.horizontal)
        print("Depth:", submarine_moved.depth)
        print("Multiplied:", result)


if __name__ == '__main__':
    main()
