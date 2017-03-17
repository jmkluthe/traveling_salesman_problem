#!/usr/bin/env python3

from random import shuffle, randrange

class Node(object):

    def __init__(self, problem, previous_node=None):
        if previous_node:
            self.visit_order = list(previous_node.visit_order)
            self.cost = previous_node.cost
            self.swap_edges(problem)
        else:
            self.visit_order = list(problem.data.keys())
            shuffle(self.visit_order)
            self.cost = self.compute_cost(problem)

    def compute_cost(self, problem):
        cost = 0
        for i in range(len(self.visit_order) - 1):
            cost += problem.compute_edge_weight(problem.data[self.visit_order[i]], problem.data[self.visit_order[i + 1]])
        cost += problem.compute_edge_weight(problem.data[self.visit_order[len(self.visit_order) - 1]], problem.data[self.visit_order[0]])
        return cost

    def swap_edges(self, problem):
        last_index = len(self.visit_order) - 1
        i = j = randrange(0, last_index + 1)
        while j == i:
            j = randrange(0, last_index + 1)
        # subtract the old edge weights and add the new
        # check case that i = 0
        if i == 0:
            self.cost -= problem.compute_edge_weight(problem.data[self.visit_order[last_index]],
                                                     problem.data[self.visit_order[0]])
            self.cost -= problem.compute_edge_weight(problem.data[self.visit_order[0]],
                                                     problem.data[self.visit_order[1]])
        # check case i is last element
        elif i == last_index:
            self.cost -= problem.compute_edge_weight(problem.data[self.visit_order[last_index - 1]],
                                                     problem.data[self.visit_order[last_index]])
            self.cost -= problem.compute_edge_weight(problem.data[self.visit_order[last_index]],
                                                     problem.data[self.visit_order[0]])
        # else i is in the middle somewhere
        else:
            self.cost -= problem.compute_edge_weight(problem.data[self.visit_order[i - 1]],
                                                     problem.data[self.visit_order[i]])
            self.cost -= problem.compute_edge_weight(problem.data[self.visit_order[i]],
                                                     problem.data[self.visit_order[i + 1]])
        # do the same checks and subs for j
        if j == 0:
            self.cost -= problem.compute_edge_weight(problem.data[self.visit_order[last_index]],
                                                     problem.data[self.visit_order[0]])
            self.cost -= problem.compute_edge_weight(problem.data[self.visit_order[0]],
                                                     problem.data[self.visit_order[1]])
        # check case j is last element
        elif j == last_index:
            self.cost -= problem.compute_edge_weight(problem.data[self.visit_order[last_index - 1]],
                                                     problem.data[self.visit_order[last_index]])
            self.cost -= problem.compute_edge_weight(problem.data[self.visit_order[last_index]],
                                                     problem.data[self.visit_order[0]])
        # else j is in the middle somewhere
        else:
            self.cost -= problem.compute_edge_weight(problem.data[self.visit_order[j - 1]],
                                                     problem.data[self.visit_order[j]])
            self.cost -= problem.compute_edge_weight(problem.data[self.visit_order[j]],
                                                     problem.data[self.visit_order[j + 1]])
        # swap the elements
        self.visit_order[i], self.visit_order[j] = self.visit_order[j], self.visit_order[i]

        # add back the edge weights with new swapped values
        # check case that i = 0
        if i == 0:
            self.cost += problem.compute_edge_weight(problem.data[self.visit_order[last_index]],
                                                     problem.data[self.visit_order[0]])
            self.cost += problem.compute_edge_weight(problem.data[self.visit_order[0]],
                                                     problem.data[self.visit_order[1]])
        # check case i is last element
        elif i == last_index:
            self.cost += problem.compute_edge_weight(problem.data[self.visit_order[last_index - 1]],
                                                     problem.data[self.visit_order[last_index]])
            self.cost += problem.compute_edge_weight(problem.data[self.visit_order[last_index]],
                                                     problem.data[self.visit_order[0]])
        # else i is in the middle somewhere
        else:
            self.cost += problem.compute_edge_weight(problem.data[self.visit_order[i - 1]],
                                                     problem.data[self.visit_order[i]])
            self.cost += problem.compute_edge_weight(problem.data[self.visit_order[i]],
                                                     problem.data[self.visit_order[i + 1]])
        # do the same checks and subs for j
        if j == 0:
            self.cost += problem.compute_edge_weight(problem.data[self.visit_order[last_index]],
                                                     problem.data[self.visit_order[0]])
            self.cost += problem.compute_edge_weight(problem.data[self.visit_order[0]],
                                                     problem.data[self.visit_order[1]])
        # check case j is last element
        elif j == last_index:
            self.cost += problem.compute_edge_weight(problem.data[self.visit_order[last_index - 1]],
                                                     problem.data[self.visit_order[last_index]])
            self.cost += problem.compute_edge_weight(problem.data[self.visit_order[last_index]],
                                                     problem.data[self.visit_order[0]])
        # else j is in the middle somewhere
        else:
            self.cost += problem.compute_edge_weight(problem.data[self.visit_order[j - 1]],
                                                     problem.data[self.visit_order[j]])
            self.cost += problem.compute_edge_weight(problem.data[self.visit_order[j]],
                                                     problem.data[self.visit_order[j + 1]])

