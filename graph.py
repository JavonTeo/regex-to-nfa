import pylab as plt
import networkx as nx
import pydot
from IPython.display import Image, display

class Graph:
    def __init__(self, parsed) -> None:
        self.parsed = parsed
        self.graph = nx.DiGraph()
        self.node_count = 0
        self.create_dfa(parsed)

    def create_dfa(self, parsed):
        operation = parsed[0]
        if operation == 'split':
            # draw_split_node(self.create_dfa(parsed[1]), self.create_dfa(parsed[2]))
            print(f"NOT YET IMPLEMENTED: {operation}")
        elif operation == 'repeat':
            # draw_repeat_node(self.create_dfa(parsed[1]), min=parsed[2])
            print(f"NOT YET IMPLEMENTED: {operation}")
        elif operation == 'cat':
            '''
            For ('cat', s, t),
            Connect last state of s to first state of t.
            '''
            self.draw_cat_node(Graph(parsed[1]).graph, Graph(parsed[2]).graph)
        else:
            # parsed must be a single character
            self.graph.add_edge(self.node_count, self.node_count + 1, label=parsed)
            self.node_count += 1

    def draw_cat_node(self, graph1: nx.DiGraph, graph2: nx.DiGraph):
        self.graph = nx.union(graph1, graph2, rename=("G", "H"))
        last_node_of_graph1 = list(nx.topological_sort(graph1))[-1]
        first_node_of_graph2 = list(nx.topological_sort(graph2))[0]
        self.graph.add_edge(f"G{last_node_of_graph1}", f"H{first_node_of_graph2}")

    def show_dfa(self):
        # nx.draw(self.graph, with_labels=True)
        pdot_graph: pydot.core.Dot = nx.nx_pydot.to_pydot(self.graph)
        Graph.view_pydot(pdot_graph)
        # plt.show()

    def view_pydot(pdot_graph):
        plt = Image(pdot_graph.write_png("out.png"))
        display(plt)
        # check issue with plotting
