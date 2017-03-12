#!/usr/bin/env python3

from random import shuffle, random, randint
from traveling_salesman_problem.tsp_problem import TspProblem
from time import time
from math import exp


class Node(object):

    def __init__(self, problem, state=None):
        if state:
            self.visit_order = list(state)
            for i in range(len(state)):
                if randint(0, 99) < 10:
                    j = randint(0, len(state) - 1)
                    self.visit_order[i] = state[j]
                    self.visit_order[j] = state[i]
            print(self.visit_order)
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


def temperature_schedule(time_to_run, current_time):
    if time_to_run - current_time < 0:
        return 0
    return (time_to_run - current_time)/time_to_run


def simulated_annealing(problem, time_to_run):
    current = Node(problem)
    t_not = time()
    t = 0
    while 1:
        t += time() - t_not
        temp = temperature_schedule(time_to_run, t)
        if temp == 0:
            return current
        successor = Node(problem, current.visit_order)
        delta = current.cost - successor.cost
        if delta > 0 or exp(delta/temp) > random():
            current = successor


filename = "tsp_example_1.txt"
problem = TspProblem(filename)
solution = simulated_annealing(problem, 120)
print(solution.cost)

