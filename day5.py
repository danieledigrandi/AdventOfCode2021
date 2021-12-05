from day1 import get_mode


class Grid:

    def __init__(self, max_x, max_y, grid):

        self.max_x = max_x
        self.max_y = max_y
        self.grid = grid

    def create_empty_grid(self):
        # Create a grid with max_x columns and max_y lines, all filled with 0s

        for i in range(self.max_x + 1):
            line = []
            for j in range(self.max_y + 1):
                line.append(0)
            self.grid.append(line)

    def fill_grid(self, hydrothermal_list):
        # The grid acts as a counter: increase the i,j position of the grid based on the corresponding point encountered
        # Hence, the point coordinates are the indices values where the grid has to increase

        for hydrothermal in hydrothermal_list:
            point_list = get_inner_points(hydrothermal[0][0], hydrothermal[0][1], hydrothermal[1][0], hydrothermal[1][1])
            # point list is a list of all integer points between 2 given points

            for point in point_list:
                # Here, increase the corresponding counter in the grid with the encountered point
                self.grid[point[1]][point[0]] += 1

    def get_overlapping(self):
        # The number of overlapping hydrothermals is the total number of values > 1 in the grid, which was a counter

        num_overlapping = 0

        for line in self.grid:
            for value in line:
                if value > 1:
                    num_overlapping += 1

        return num_overlapping


def open_file(path):

    with open(path, 'r') as f:
        lines = f.readlines()

    hydrothermal_list = []

    # convert the input in the format: [[(x1, y1), (x2, y2)], [(x1, y1), (x2, y2)], ..., ]
    # hence, each list inside the big list represents the start and end points of an hydrotermal vent.

    for hydro in lines:

        hydrothermal = []
        hydro = hydro.strip()
        hydrothermal.append((int(hydro[0:hydro.find(',')]), int(hydro[(hydro.find(',') + 1):hydro.find(' ')])))
        hydrothermal.append((int(hydro[(hydro.rfind(' ') + 1):hydro.rfind(',')]), int(hydro[(hydro.rfind(',') + 1):])))

        hydrothermal_list.append(hydrothermal)

    return hydrothermal_list


def eliminate_diagonals(hydrothermal_list):
    # for part 1 of the puzzle, keep only the vertical or horizontal hydrothermal vents
    # hence, keep only those that have x1 = x2 or y1 = y2

    hydrothermal_list_pt1 = []

    for hydrothermal in hydrothermal_list:
        if hydrothermal[0][0] == hydrothermal[1][0] or hydrothermal[0][1] == hydrothermal[1][1]:
            hydrothermal_list_pt1.append(hydrothermal)

    return hydrothermal_list_pt1


def get_max_values(hydrothermal_list):

    max_x = 0
    max_y = 0

    for hydrothermal in hydrothermal_list:

        if hydrothermal[0][0] > max_x:
            max_x = hydrothermal[0][0]

        if hydrothermal[1][0] > max_x:
            max_x = hydrothermal[0][0]

        if hydrothermal[0][1] > max_y:
            max_y = hydrothermal[0][1]

        if hydrothermal[1][1] > max_y:
            max_y = hydrothermal[1][1]

    return max_x, max_y


def get_inner_points(x0, y0, x1, y1):
    # Bresenham's line algorithm
    # This algorithm generates all the integer coordinate points between two given points (x0, y0) and (x1, y1)
    # It returns a list of tuples, where a tuple is a coordinate point (x, y)

    points_in_line = []

    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    x, y = x0, y0
    sx = -1 if x0 > x1 else 1
    sy = -1 if y0 > y1 else 1

    if dx > dy:
        err = dx / 2.0
        while x != x1:
            points_in_line.append((x, y))
            err -= dy
            if err < 0:
                y += sy
                err += dx
            x += sx
    else:
        err = dy / 2.0
        while y != y1:
            points_in_line.append((x, y))
            err -= dx
            if err < 0:
                x += sx
                err += dy
            y += sy

    points_in_line.append((x, y))

    return points_in_line


def main():

    path = "./data/input_day_5.txt"
    hydrothermal_list = open_file(path)

    mode = get_mode()

    if mode == 1:
        hydrothermal_list_pt1 = eliminate_diagonals(hydrothermal_list)

        max_x, max_y = get_max_values(hydrothermal_list_pt1)

        diagram = Grid(max_x=max_x, max_y=max_y, grid=[])
        diagram.create_empty_grid()
        diagram.fill_grid(hydrothermal_list_pt1)
        num_overlapping = diagram.get_overlapping()

        print("Number of overlapping lines:", num_overlapping)

    elif mode == 2:
        # The algorithm is the same of pt1, but now use the full hydrothermal list

        max_x, max_y = get_max_values(hydrothermal_list)

        diagram = Grid(max_x=max_x, max_y=max_y, grid=[])
        diagram.create_empty_grid()
        diagram.fill_grid(hydrothermal_list)
        num_overlapping = diagram.get_overlapping()

        print("Number of overlapping lines:", num_overlapping)


if __name__ == '__main__':
    main()
