from collections import defaultdict

def add_connection(graph, row):
    nodes = row.split()
    parent = nodes[0]
    for child in nodes[2:]:
        graph[parent].append(child.strip(','))



def make_graph(connections):
    graph = defaultdict(list)

    for row in connections:
        add_connection(graph, row)

    return graph

def bfs(graph, start='0'):
    visited = set()
    queue = [start]

    while queue:
        vertex = queue.pop(0)

        if vertex not in visited:
            visited.add(vertex)
            queue.extend(set(graph[vertex]) - visited)

    return visited

def main():
    with open('test_case.txt', 'r') as connections:
        graph = make_graph(connections)
        assert len(bfs(graph)) == 6

    with open('input.txt', 'r') as connections:
        graph = make_graph(connections)
        print('Answer: ', len(bfs(graph)))

if __name__ == '__main__':
    main()
