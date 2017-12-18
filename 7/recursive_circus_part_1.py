import random

def add_nodes_reverse_edges_weights(row, nodes, edges, weights, graph):
    info = row.split()

    if len(info) == 2:
        name, weight = info
        nodes.add(name)
        weights[name] = int(weight.strip('()'))

    else:
        parent = info[0]
        weight = info[1]
        nodes.add(parent)
        weights[parent] = int(weight.strip('()'))

        children = ["".join(c.split(",")) for c in info[3:]]

        for child in children:
            nodes.add(child)
            edges.add((child, parent))
            graph[child] = parent

def make_reversed_graph(towers):
    nodes = set()
    edges = set()
    weights = dict()
    reversed_graph = dict()

    for row in towers:
        add_nodes_reverse_edges_weights(row, nodes, edges, weights, reversed_graph)

    return nodes, edges, weights, reversed_graph

def find_root(nodes, edges, weights, graph):
    root = random.choice(list(nodes))

    while True:
        try:
            root = graph[root]
        except KeyError:
            return root

def main():
    with open('part_1_test_case.txt', 'r') as towers:
        assert find_root(*make_reversed_graph(towers)) == 'tknk'

    with open('input.txt', 'r') as towers:
        print("Answer: ", find_root(*make_reversed_graph(towers)))

if __name__ == '__main__':
    main()
