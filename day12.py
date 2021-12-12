import networkx as nx
import copy
from collections import defaultdict
from day1 import get_mode


def open_file(path):

    with open(path, 'r') as f:
        edges = [tuple(line.strip().split('-')) for line in f.readlines()]

    nodes = []

    for edge in edges:
        if edge[0] not in nodes:
            nodes.append(edge[0])
        if edge[1] not in nodes:
            nodes.append(edge[1])

    for a, b in edges:
        paths[a].append(b)
        paths[b].append(a)

    return nodes, edges


def initialise_graph(nodes, edges):

    cave = nx.Graph()

    cave.add_nodes_from(nodes)
    cave.add_edges_from(edges)

    return cave


def printAllPathsUtil(graph, u, d, visited, path):

    # If lowercase, mark the current node as visited and store in path
    if u.islower():
        visited.append(u)
    path.append(u)

    # If current vertex is same as destination, then update the global path list with current path
    if u == d:
        global all_
        all_.append(copy.deepcopy(path))

    else:
        # If current vertex is not destination, recur for all the vertices adjacent to this vertex
        for i in graph.neighbors(u):
            if i.islower():
                if i not in visited:
                    printAllPathsUtil(graph, i, d, visited, path)
            else:
                printAllPathsUtil(graph, i, d, visited, path)

    # Remove current vertex from path and if lowercase, mark it as unvisited
    path.pop()

    if u.islower():
        visited.remove(u)


def printAllPaths(graph, s, d):

    # Create an array of visited vertices
    visited = []

    # Create an array to store paths
    path = []

    # Call the recursive helper function to print all paths
    printAllPathsUtil(graph, s, d, visited, path)


def dfs(node, visited, one_off):
    # For part 2, the simplest way is to use the DFS algorithm

    if node == "end":
        return 1

    if node.islower():
        visited.add(node)

    total = sum([dfs(i, visited, one_off) for i in paths[node] if i not in visited])
    total += sum([dfs(i, visited, i) for i in paths[node] if i in visited and i != "start"]) if one_off == ' ' else 0

    if node != one_off:
        visited.discard(node)

    return total


def main():
    filepath = "./data/input_day_12.txt"

    nodes, edges = open_file(filepath)
    cave = initialise_graph(nodes, edges)

    mode = get_mode()

    if mode == 1:
        printAllPaths(cave, "start", "end")
        print("Number of paths by visiting small caves at most once:", len(all_))

    elif mode == 2:
        total = dfs("start", set(), ' ')
        print("Number of paths for part 2:", total)


if __name__ == '__main__':
    all_ = []
    paths = defaultdict(list)
    main()
