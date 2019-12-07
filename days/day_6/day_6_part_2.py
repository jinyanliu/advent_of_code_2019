"""
Created at 2019-12-06 19:00

@author: jinyanliu
"""


def get_list_of_node_names():
    node_names = []
    with open("day_6_input") as lines:
        for line in lines:
            node_names += (line.rstrip('\n').split(')'))
    return node_names


def get_input_nodes():
    different_node_names = []
    for node_name in get_list_of_node_names():
        if node_name not in different_node_names:
            different_node_names.append(node_name)
    nodes = {}
    for different_node_name in different_node_names:
        nodes[different_node_name] = Node(different_node_name)
    return nodes


def get_list_of_edges_src_des():
    edges_src_des = []
    with open("day_6_input") as lines:
        for line in lines:
            splitted_string = line.rstrip('\n').split(')')
            edges_src_des.append((splitted_string[1], splitted_string[0]))
    return edges_src_des


class Node(object):
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

    def __str__(self):
        return self.name


class Edge(object):
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest

    def getSource(self):
        return self.src

    def getDestination(self):
        return self.dest

    def __str__(self):
        return self.src.getName() + '->' + self.dest.getName()


class Digraph(object):
    def __init__(self):
        self.nodes = []
        self.edges = {}

    def addNode(self, node):
        if node in self.nodes:
            raise ValueError('Duplicate node')
        else:
            self.nodes.append(node)
            self.edges[node] = []

    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if not (src in self.nodes and dest in self.nodes):
            raise ValueError('Node not in graph')
        self.edges[src].append(dest)

    def childrenOf(self, node):
        return self.edges[node]

    def hasNode(self, node):
        return node in self.nodes

    def __str__(self):
        result = ''
        for src in self.nodes:
            for dest in self.edges[src]:
                result = result + src.getName() + '->' + dest.getName + '\n'
        return result[:-1]


class Graph(Digraph):
    def addEdge(self, edge):
        Digraph.addEdge(self, edge)
        rev = Edge(edge.getDestination(), edge.getSource())
        Digraph.addEdge(self, rev)


def printPath(path):
    result = ''
    for i in range(len(path)):
        result = result + str(path[i])
        if i != len(path) - 1:
            result = result + '->'
    return result


def DFS(graph, start, end, path, shortest, toPrint=False):
    path = path + [start]
    if toPrint:
        print('Current DFS path:', printPath(path))
    if start == end:
        return path
    for node in graph.childrenOf(start):
        if node not in path:
            if shortest == None or len(path) < len(shortest):
                newPath = DFS(graph, node, end, path, shortest, toPrint)
                if newPath != None:
                    shortest = newPath
    return shortest


def create_graph(nodes, edges):
    graph = Graph()
    for node in nodes.values():
        graph.addNode(node)
    for edge_src_des in edges:
        src, des = edge_src_des
        graph.addEdge(Edge(nodes[src], nodes[des]))
    return graph


def get_solution_2():
    nodes = get_input_nodes()
    edges = get_list_of_edges_src_des()
    graph = create_graph(nodes, edges)
    path = DFS(graph, nodes['YOU'], nodes['SAN'], [], None, True)
    return len(path) - 3


if __name__ == "__main__":
    print(get_solution_2())
    list_1 = [1, 2, 3]
    list_2 = [3, 4]
    list_3 = list_1 + list_2
    print(list_1)
