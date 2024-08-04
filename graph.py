import matplotlib.pyplot as plt
import networkx as nx

class Graph:
    def __init__(self, parsed) -> None:
        self.parsed = parsed
        self.graph = nx.Graph()
        self.create_dfa(parsed)

    def create_dfa(self, parsed):
        if type(parsed) != tuple:
            self.graph.add_edge(1, 2)
            return
        operation = parsed[0]
        # if operation == 'split':
        #     draw_split_node(self.create_dfa(parsed[1]), self.create_dfa(parsed[2]))
        # elif operation == 'repeat':
        #     draw_repeat_node(self.create_dfa(parsed[1]), min=parsed[2])
        # elif operation == 'cat':
        #     draw_cat_node(self.create_dfa(parsed[1]), self.create_dfa(parsed[2]))
        # self.graph.add

    def show_dfa(self):
        nx.draw(self.graph, with_labels=True)
        plt.show()

