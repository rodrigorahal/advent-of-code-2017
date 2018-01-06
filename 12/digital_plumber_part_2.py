from collections import defaultdict
from digital_plumber_part_1 import bfs

def add_connection(graph, vertices, row):
    nodes = row.split()
    parent = nodes[0]
    vertices.add(parent)
    for child in nodes[2:]:
        graph[parent].append(child.strip(','))
        vertices.add(child.strip(','))

def make_graph(connections):
    vertices = set()
    graph = defaultdict(list)

    for row in connections:
        add_connection(graph, vertices, row)

    return graph, vertices

def strongly_connected_components(graph, vertices):
    visited = set()
    ngroups = 0

    for v in vertices:
        if v not in visited:
            ngroups += 1
            v_group = bfs(graph, start=v)
            visited.update(v_group)

    return ngroups

def main():
    with open('test_case.txt', 'r') as connections:
        graph, vertices = make_graph(connections)
        assert strongly_connected_components(graph, vertices) == 2

    with open('input.txt', 'r') as connections:
        graph, vertices = make_graph(connections)
        print('Answer: ', strongly_connected_components(graph, vertices))

if __name__ == '__main__':
    main()
