import copy
from day1 import get_mode


class Grid:

    def __init__(self, grid, flashed_this_step, flashes_num=0):

        self.grid = grid
        self.flashed_this_step = flashed_this_step
        self.flashes_num = flashes_num

    def simulate_one_step(self):

        # First, the energy level of each octopus increases by 1
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.grid[i][j] != -1:
                    self.grid[i][j] += 1

        while any(value > 9 for i in self.grid for value in i):  # while there is an octopuses that can flashes in this step
            # Then, any octopus with an energy level greater than 9 flashes
            for i in range(len(self.grid)):
                for j in range(len(self.grid[i])):
                    if self.grid[i][j] > 9:
                        self.grid[i][j] = 0
                        self.flashes_num += 1

            # This increases the energy level of all adjacent octopuses by 1, including diagonals
            # If this causes an octopus to have an energy level greater than 9, it also flashes
            # Though, the counter of already flashed octopus in the same step does not increase
            # This process continues as long as new octopuses keep having their energy level increased beyond 9
            # Finally, any octopus that flashed during this step has its energy level set to 0
            for i in range(1, len(self.grid) - 1):
                for j in range(1, len(self.grid[i]) - 1):

                    if self.grid[i][j] == 0 and not self.flashed_this_step[i][j]:

                        self.flashed_this_step[i][j] = True  # to not increase any further if already increased the adjacent values

                        if self.grid[i + 1][j] != -1 and self.grid[i + 1][j] != 0: self.grid[i + 1][j] += 1
                        if self.grid[i + 1][j + 1] != -1 and self.grid[i + 1][j + 1] != 0: self.grid[i + 1][j + 1] += 1
                        if self.grid[i][j + 1] != -1 and self.grid[i][j + 1] != 0: self.grid[i][j + 1] += 1
                        if self.grid[i - 1][j + 1] != -1 and self.grid[i - 1][j + 1] != 0: self.grid[i - 1][j + 1] += 1
                        if self.grid[i - 1][j] != -1 and self.grid[i - 1][j] != 0: self.grid[i - 1][j] += 1
                        if self.grid[i - 1][j - 1] != -1 and self.grid[i - 1][j - 1] != 0: self.grid[i - 1][j - 1] += 1
                        if self.grid[i][j - 1] != -1 and self.grid[i][j - 1] != 0: self.grid[i][j - 1] += 1
                        if self.grid[i + 1][j - 1] != -1 and self.grid[i + 1][j - 1] != 0: self.grid[i + 1][j - 1] += 1

        self.flashed_this_step = [[False for _ in self.grid[0]] for _ in self.grid]

    def simulate_pt1(self, num_of_steps):

        for step in range(num_of_steps):
            self.simulate_one_step()

    def simulate_pt2(self):

        step = 0

        while any(value != 0 and value != -1 for i in self.grid for value in i):  # while there exists a value in the matrix that is not 0 or -1
            self.simulate_one_step()
            step += 1

        return step


def open_file(path):

    with open(path, 'r') as f:
        file_lines = f.readlines()

    octopuses = []

    for line in file_lines:
        line = line.strip()
        row = [int(number) for number in line]
        octopuses.append(row)

    # frame the input with a bunch of -1 so to not have to deal with corner edge cases
    fictional_row = [-1 for _ in range(len(octopuses[0]))]
    octopuses.append(fictional_row)
    octopuses.insert(0, fictional_row)

    octopuses_final = copy.deepcopy(octopuses)

    for i in range(len(octopuses)):
        octopuses_final[i].insert(0, -1)
        octopuses_final[i].append(-1)

    octopuses_final[0].pop()
    octopuses_final[len(octopuses_final) - 1].pop()

    return octopuses_final


def main():
    path = './data/input_day_11.txt'
    octopuses = open_file(path)

    flashed_this_step = [[False for _ in octopuses[0]] for _ in octopuses]

    cavern = Grid(grid=octopuses, flashed_this_step=flashed_this_step)

    mode = get_mode()

    if mode == 1:
        cavern.simulate_pt1(num_of_steps=100)
        print("Number of total flashes after 100 steps:", cavern.flashes_num)

    elif mode == 2:
        synchro = cavern.simulate_pt2()
        print("First step during which all octopuses flash in synchro:", synchro)


if __name__ == '__main__':
    main()
