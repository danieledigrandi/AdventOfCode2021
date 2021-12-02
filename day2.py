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


def move_pt1(submarine, instructions):

    for instr in instructions:

        # Here, call the method directly with the instance contained in instr[0]
        # For example, if instr[0] == 'forward', is like writing submarine.forward(instr[1])
        # The 2 lines of code below do exactly the same thing, but now is parametrized
        # for any possible value of instr[0]

        class_method = getattr(Submarine_pt1, instr[0])
        class_method(submarine, instr[1])

    return submarine


def move_pt2(submarine, instructions):

    for instr in instructions:

        # Here, call the method directly with the instance contained in instr[0]
        # For example, if instr[0] == 'forward', is like writing submarine.forward(instr[1])
        # The 2 lines of code below do exactly the same thing, but now is parametrized
        # for any possible value of instr[0]

        class_method = getattr(Submarine_pt2, instr[0])
        class_method(submarine, instr[1])

    return submarine


def main(mode=1):

    path = './data/input_day_2_1.txt'
    instructions = open_file(path)

    if mode == 1:
        submarine = Submarine_pt1()

        submarine_moved = move_pt1(submarine, instructions)

        result = submarine_moved.horizontal * submarine_moved.depth

        print("Horizontal:", submarine_moved.horizontal)
        print("Depth:", submarine_moved.depth)
        print("Multiplied:", result)

    elif mode == 2:
        submarine = Submarine_pt2()

        submarine_moved = move_pt2(submarine, instructions)

        result = submarine_moved.horizontal * submarine_moved.depth

        print("Horizontal:", submarine_moved.horizontal)
        print("Depth:", submarine_moved.depth)
        print("Multiplied:", result)


if __name__ == '__main__':
    main(mode=2)