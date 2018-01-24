from collections import defaultdict

def make_graph(edges):
    graph = defaultdict(set)

    for edge in edges:
        start, end = [int(x) for x in edge.strip().split("/")]
        graph[start].add(end)
        graph[end].add(start)

    return graph

def gen_bridges(bridge, components):
    bridge = bridge or [(0, 0)]
    cur = bridge[-1][1]
    for b in components[cur]:
        if not ((cur, b) in bridge or (b, cur) in bridge):
            new = bridge + [(cur, b)]
            yield new
            yield from gen_bridges(new, components)

def all_bridges(components):
    return [bridge for bridge in gen_bridges(None, components)]

def strength(bridge):
    return sum(s + e for s, e in bridge)

def strongest(bridges):
    return max(bridges, key=strength)

def fittest(bridges):
    return sorted(bridges, key=lambda b : (len(b), strength(b)))[-1]

def main():
    with open('test_case.txt') as edges:
        graph = make_graph(edges)
        bridges = all_bridges(graph)
        assert strength(strongest(bridges)) == 31
        assert strength(fittest(bridges)) == 19

    with open('input.txt') as edges:
        graph = make_graph(edges)
        bridges = all_bridges(graph)
        print('Part 1: ', strength(strongest(bridges)))
        print('Part 2: ', strength(fittest(bridges)))

if __name__ == '__main__':
    main()
