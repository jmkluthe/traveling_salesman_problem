#!/usr/bin/env python3

from sys import argv
from traveling_salesman_problem.tsp_problem import TspProblem

#
# def read_input_file(filename):
#     data = {}
#     with open(filename, "r") as f:
#         for line in f.readlines():
#             if line:
#                 vals = line.strip("\n").split(" ")
#                 data[vals[0]] = (int(vals[1]), int(vals[2]))
#     return data
#
#
# def write_output_file(filename, out_data):
#     pass
#
#
# def compute_edge_lists(in_data):
#     """
#     Computes the edge lists for a complete graph where the nodes are represented by (x, y) point.
#     The edge list is for each node consists of dictionary entries with the key being the node number of every other
#     point in the graph, and the value being the Euclidean distance between the two nodes.
#
#     :param in_data: dictionary(key: tuple) - key is the node number, tuple is (x, y) position.
#     :return edge_lists: dictionary(key: dictionary) - key is the node number, dictionary is the set of other nodes and
#         their distances from the first node.
#     """
#     edge_lists = {}
#     for u in in_data.keys():
#         edge_lists[u] = {}
#         for v in in_data.keys():
#             if u != v:
#                 edge_lists[u][v] = compute_edge_weight(in_data[u], in_data[v])
#     return edge_lists
#
#
# def compute_edge_weight(u, v):
#     """
#     Calculates and returns Euclidean distance between two points in 2 dimensions.
#
#     :param u: tuple of ints representing (x,y) position of a node
#     :param v: tuple of ints representing (x,y) position of a node
#     :return: int distance between points u and v
#     """
#     delta_x_squared = (u[0] - v[0]) ** 2
#     delta_y_squared = (u[1] - v[1]) ** 2
#     return round((delta_x_squared + delta_y_squared) ** 0.5)

if len(argv) == 2:
    filename = argv(1)
else:
    filename = "tsp_example_1.txt"
problem = TspProblem(filename)
print(problem.adjacency_list)
for node, edge_list in problem.adjacency_list.items():
    print("{}: {}".format(node, edge_list))

