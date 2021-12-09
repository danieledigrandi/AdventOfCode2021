from day1 import get_mode
import networkx as nx
import numpy as np


def open_file(path):

    with open(path, 'r') as f:
        lines = f.readlines()

    heightmap = []

    for line in lines:
        line = line.strip()
        row = []
        for number in line:
            row.append(int(number))
        heightmap.append(row)

    return heightmap


def find_low_points(heightmap):

    low_points = []
    points_positions = []

    for index_row in range(len(heightmap)):

        for index_number in range(len(heightmap[index_row])):

            # if first row
            if index_row == 0:

                # if left up corner
                if index_number == 0:

                    if heightmap[index_row][index_number] < heightmap[index_row][index_number + 1] \
                            and heightmap[index_row][index_number] < heightmap[index_row + 1][index_number]:
                        low_points.append(heightmap[index_row][index_number])
                        points_positions.append((index_row, index_number))

                # if right up corner
                elif index_number == (len(heightmap[index_row]) - 1):

                    if heightmap[index_row][index_number] < heightmap[index_row][index_number - 1] \
                            and heightmap[index_row][index_number] < heightmap[index_row + 1][index_number]:
                        low_points.append(heightmap[index_row][index_number])
                        points_positions.append((index_row, index_number))

                # otherwise
                else:
                    if heightmap[index_row][index_number] < heightmap[index_row][index_number - 1] \
                            and heightmap[index_row][index_number] < heightmap[index_row][index_number + 1] \
                            and heightmap[index_row][index_number] < heightmap[index_row + 1][index_number]:
                        low_points.append(heightmap[index_row][index_number])
                        points_positions.append((index_row, index_number))

            # if last row
            elif index_row == (len(heightmap) - 1):

                # if left down corner
                if index_number == 0:

                    if heightmap[index_row][index_number] < heightmap[index_row][index_number + 1] \
                            and heightmap[index_row][index_number] < heightmap[index_row - 1][index_number]:
                        low_points.append(heightmap[index_row][index_number])
                        points_positions.append((index_row, index_number))

                # if right down corner
                elif index_number == (len(heightmap[index_row]) - 1):

                    if heightmap[index_row][index_number] < heightmap[index_row][index_number - 1] \
                            and heightmap[index_row][index_number] < heightmap[index_row - 1][index_number]:
                        low_points.append(heightmap[index_row][index_number])
                        points_positions.append((index_row, index_number))

                # otherwise
                else:
                    if heightmap[index_row][index_number] < heightmap[index_row][index_number - 1] \
                            and heightmap[index_row][index_number] < heightmap[index_row][index_number + 1] \
                            and heightmap[index_row][index_number] < heightmap[index_row - 1][index_number]:
                        low_points.append(heightmap[index_row][index_number])
                        points_positions.append((index_row, index_number))

            # otherwise I'm somewhere in the middle. Though the columns are still to be checked
            else:

                # first column
                if index_number == 0:

                    if heightmap[index_row][index_number] < heightmap[index_row][index_number + 1] \
                            and heightmap[index_row][index_number] < heightmap[index_row - 1][index_number] \
                            and heightmap[index_row][index_number] < heightmap[index_row + 1][index_number]:
                        low_points.append(heightmap[index_row][index_number])
                        points_positions.append((index_row, index_number))

                # last column
                elif index_number == (len(heightmap[index_row]) - 1):

                    if heightmap[index_row][index_number] < heightmap[index_row][index_number - 1] \
                            and heightmap[index_row][index_number] < heightmap[index_row - 1][index_number] \
                            and heightmap[index_row][index_number] < heightmap[index_row + 1][index_number]:
                        low_points.append(heightmap[index_row][index_number])
                        points_positions.append((index_row, index_number))

                # otherwise I'm somewhere in the middle
                else:

                    if heightmap[index_row][index_number] < heightmap[index_row][index_number - 1] \
                            and heightmap[index_row][index_number] < heightmap[index_row][index_number + 1] \
                            and heightmap[index_row][index_number] < heightmap[index_row - 1][index_number] \
                            and heightmap[index_row][index_number] < heightmap[index_row + 1][index_number]:
                        low_points.append(heightmap[index_row][index_number])
                        points_positions.append((index_row, index_number))

    return low_points, points_positions


def main():
    path = "./data/input_day_9.txt"
    heightmap = open_file(path)

    mode = get_mode()

    if mode == 1:

        low_points, points_positions = find_low_points(heightmap)

        risk_levels = [number + 1 for number in low_points]

        print("Sum of the risk levels of all low points:", sum(risk_levels))

    elif mode == 2:

        """
        Treat puzzle input as a graph, where 4-neighbourhoods have edges.
        Basically, each value is a node and start with a fully connected graph.
        Remove edges from nodes with value (called depth in the puzzle) of 9. 
        Sort connected components by size.
        """

        area = nx.Graph()

        for y, line in enumerate(heightmap):

            for x, depth in enumerate(line):
                area.add_node((x, y))
                if x > 0:
                    area.add_edge((x, y), (x - 1, y))
                if y > 0:
                    area.add_edge((x, y), (x, y - 1))
                area.nodes[(x, y)]['depth'] = depth

        for x, y in area.nodes:
            if area.nodes[(x, y)]['depth'] == 9:
                area.remove_edges_from([
                    ((x, y), (x - 1, y)),
                    ((x, y), (x + 1, y)),
                    ((x, y), (x, y - 1)),
                    ((x, y), (x, y + 1))
                ])

        component_sizes = [len(c) for c in sorted(nx.connected_components(area), key=len, reverse=True)]

        value = np.prod(component_sizes[:3])

        print("Sizes of the three largest basins:", component_sizes[:3])
        print("Multiplication of sizes of the three largest basins:", value)


if __name__ == '__main__':
    main()
