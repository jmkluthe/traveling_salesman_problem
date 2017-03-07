#!/usr/bin/env python3

from sys import argv


def read_input_file(filename):
    data = {}
    with open(filename, "r") as f:
        for line in f.readlines():
            if line:
                vals = line.strip("\n").split(" ")
                data[vals[0]] = (int(vals[1]), int(vals[2]))
    return data


def write_output_file(filename, out_data):
    pass


def compute_edge_lists(in_data):
    edges = {}
    for u in in_data.keys():
        edges[u] = {}
        for v in in_data.keys():
            if u != v:
                edges[u][v] = compute_edge_weight(in_data(u), in_data(v))


def compute_edge_weight(u, v):
    delta_x_squared = float((u[0] - v[0])**2)
    delta_y_squared = float((u[1] - v[1])**2)
    return round((delta_x_squared + delta_y_squared)**(0.5))


if len(argv) == 2:
    filename = argv(1)
else:
    filename = "tsp_example_1.txt"
in_data = read_input_file(filename)
print(in_data)


