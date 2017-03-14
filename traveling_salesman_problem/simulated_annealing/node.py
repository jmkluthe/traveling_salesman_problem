#!/usr/bin/env python3

from random import shuffle, randrange

class Node(object):

    def __init__(self, problem, state=None):
        if state:
            self.visit_order = list(state)
            i = j = randrange(0, len(state))
            while j == i:
                j = randrange(0, len(state))
            self.visit_order[i], self.visit_order[j] = self.visit_order[j], self.visit_order[i]
            #print(self.visit_order)
            self.cost = self.compute_cost(problem)
        else:
            self.visit_order = list(problem.adjacency_list.keys())
            shuffle(self.visit_order)
            self.cost = self.compute_cost(problem)

    def compute_cost(self, problem):
        cost = 0
        for i in range(len(self.visit_order) - 1):
            #print(self.visit_order[i])
            #print(self.visit_order[i + 1])
            #print(problem.adjacency_list[self.visit_order[i]])
            #print(problem.adjacency_list[self.visit_order[i]][self.visit_order[i + 1]])
            cost += problem.adjacency_list[self.visit_order[i]][self.visit_order[i + 1]]
        return cost

