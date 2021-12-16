import networkx as nx
import matplotlib.pyplot as plt
import copy
from day1 import get_mode


def open_file(path):

    with open(path, 'r') as f:
        lines = f.readlines()

    cavern_raw = [[int(number) for number in line.strip()] for line in lines]

    return cavern_raw


def create_graph(cavern_raw):

    # Due to the nature of the problem, the graph must be a directed multi graph,
    # that is, a directed graph that can have multiple edges (with different weights)
    # between two nodes.

    cavern = nx.MultiDiGraph()

    for i in range(len(cavern_raw)):
        for j in range(len(cavern_raw[i])):
            cavern.add_node((i, j))
            if j > 0:
                cavern.add_edge((i, j), (i, j - 1), weight=cavern_raw[i][j])
                cavern.add_edge((i, j - 1), (i, j), weight=cavern_raw[i][j - 1])
            if i > 0:
                cavern.add_edge((i, j), (i - 1, j), weight=cavern_raw[i][j])
                cavern.add_edge((i - 1, j), (i, j), weight=cavern_raw[i - 1][j])

    return cavern


def solve_part1(cavern, cavern_raw):

    p = nx.shortest_path(cavern, source=(0, 0), target=((len(cavern_raw) - 1), (len(cavern_raw[0]) - 1)), weight="weight")

    risk = 0

    print(p)

    risks = [cavern_raw[i[0]][i[1]] for i in p]

    print(risks)

    for i in p:
        # as said in the puzzle, never count the first position
        if i != (0, 0):
            risk += cavern_raw[i[0]][i[1]]

    return risk


def create_complete_map(cavern_raw):

    true_cavern = copy.deepcopy(cavern_raw)

    # expand the rows
    for _ in range(4):
        for j in range(len(cavern_raw[0])):
            for i in range(len(cavern_raw)):
                if cavern_raw[i][j] < 9:
                    true_cavern[i].append(cavern_raw[i][j] + 1)
                else:
                    true_cavern[i].append(1)

        cavern_raw = copy.deepcopy(true_cavern)

    # expand the columns
    for _ in range(4):
        for i in range(len(cavern_raw)):
            new_line = []
            for j in range(len(cavern_raw[i])):
                if cavern_raw[i][j] < 9:
                    new_line.append(cavern_raw[i][j] + 1)
                else:
                    new_line.append(1)
            true_cavern.append(new_line)

        cavern_raw = copy.deepcopy(true_cavern)

    return true_cavern


def draw_graph(graph, mode):

    # mode can either be plt or graphviz, depending on the desired draw method

    if mode == 'graphviz':
        # produce a .dot file to be opened either via graphviz online or graphviz downloaded on a pc
        nx.drawing.nx_pydot.write_dot(graph, 'graph.dot')

    elif mode == 'plt':
        nx.draw(graph, with_labels=True, font_weight='bold')
        plt.show()


def main():
    path = './data/input_day_15.txt'
    #path = './data/prova.txt'

    cavern_raw = open_file(path)

    mode = get_mode()

    if mode == 1:
        cavern = create_graph(cavern_raw)
        risk = solve_part1(cavern, cavern_raw)

        print("Lowest total risk:", risk)

    elif mode == 2:
        true_cavern = create_complete_map(cavern_raw)
        print("here1")
        true_cavern_graph = create_graph(true_cavern)
        print("here2")
        risk = solve_part1(true_cavern_graph, true_cavern)

        print("Lowest total risk:", risk)



if __name__ == '__main__':
    main()
