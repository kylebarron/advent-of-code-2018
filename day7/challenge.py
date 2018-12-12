import networkx as nx
import matplotlib.pyplot as plt

def main():
    with open('input.txt') as f:
        lines = f.readlines()

    lines = [x.strip() for x in lines]
    lines = sorted([(x[5], x[36]) for x in lines])

    parents = {x[0] for x in lines}
    children = {x[1] for x in lines}
    parents - children

    G = nx.Graph()
    G.add_node(1)
    G.add_nodes_from([2, 3])
    nx.draw(G)


    nodes = {}
    for line in lines:
        k = line[0]
        v = line[1]
        nodes[k] = nodes.get(k, Node(k))
        nodes[k].add_child(v)
    a = Node('A')
    a.add_child(Node('C'))
    a.add_child('V')
    a
    Node('A')


class Node(object):
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, obj):
        self.children.append(obj)

    def __repr__(self):
        txt = f'Node({self.data})'
        if self.children:
            txt += f'; Children={str(self.children)}'
        return txt

if __name__ == '__main__':
    main()