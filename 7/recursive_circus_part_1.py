
def add_child_parent_relationships(row, child_parent):
    info = row.split()

    # no childs
    if len(info) == 2:
        return

    else:
        parent = info[0]
        children = ["".join(c.split(",")) for c in info[3:]]

        for child in children:
            child_parent[child] = parent

def make_graph(towers):
    child_parent = dict()

    for row in towers:
        add_child_parent_relationships(row, child_parent)

    return child_parent

def find_root(child_parent, init_id=0):
    """
    Choose a random node in the graph and traverse backwards until we
    find the root node
    """
    root = list(child_parent.values())[init_id]

    while True:
        try:
            root = child_parent[root]
        except KeyError:
            return root

def main():
    with open('part_1_test_case.txt', 'r') as towers:
        assert find_root(make_graph(towers)) == 'tknk'

    with open('input.txt', 'r') as towers:
        print("Answer: ", find_root(make_graph(towers)))

if __name__ == '__main__':
    main()
