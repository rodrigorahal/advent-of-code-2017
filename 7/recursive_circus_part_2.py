from collections import defaultdict, Counter

from recursive_circus_part_1 import make_reversed_graph, find_root

def add_nodes_edges_weights(row, nodes, edges, weights, graph):
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
            graph[parent].append(child)

def make_graph(towers):
    nodes = set()
    edges = set()
    weights = dict()
    graph = defaultdict(list)

    for row in towers:
        add_nodes_edges_weights(row, nodes, edges, weights, graph)

    return nodes, edges, weights, graph

def supporting_weight(weights, graph, node):
    if node not in graph:
        return weights[node]
    else:
        return weights[node] + sum(supporting_weight(weights, graph, c) for c in graph[node])

def find_imbalance(nodes, edges, weights, graph, node, target=None):
    children = graph[node]
    towers_weights = []

    for child in children:
        sup_weight = supporting_weight(weights, graph, child)
        towers_weights.append(sup_weight)

    if len(set(towers_weights)) != 1:

        counter = Counter(towers_weights)

        for i, w in enumerate(towers_weights):
            if counter[w] == 1:
                target = (set(towers_weights) - set([w])).pop()
                return find_imbalance(nodes, edges, weights, graph, children[i], target)

    else:
        sup_weight = sum(towers_weights) + weights[node]
        return target - sup_weight + weights[node]


def main():
    with open('part_1_test_case.txt', 'r') as towers:
        towers = list(towers)
        root = find_root(*make_reversed_graph(towers))

        nodes, edges, weights, graph = make_graph(towers)
        w = supporting_weight(weights, graph, 'fwft')

        assert find_imbalance(nodes, edges, weights, graph, root) == 60

    with open('input.txt', 'r') as towers:
        towers = list(towers)
        root = find_root(*make_reversed_graph(towers))

        graph = make_graph(towers)

        nodes, edges, weights, graph = make_graph(towers)
        w = supporting_weight(weights, graph, 'dgoocsw')

        print('Answer : ', find_imbalance(nodes, edges, weights, graph, root))

if __name__ == '__main__':
    main()
