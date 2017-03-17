#!/usr/bin/env python3

from random import random
from time import time
from math import exp
from traveling_salesman_problem.tsp_problem import TspProblem
from traveling_salesman_problem.simulated_annealing.node import Node


def simulated_annealing(problem, time_to_run):
    current = Node(problem)
    t_not = time()
    out_file = open("cost_vs_time.csv", "w")
    n = 0
    while 1:
        t = time() - t_not
        #print(t)
        if n == 100:
            out_file.write("{}, {}\n".format(t, current.cost))
            n = 0
        else:
            n += 1
        temp = temperature_schedule(time_to_run, t)
        if temp == 0:
            return current
        successor = Node(problem, current.visit_order)
        delta = current.cost - successor.cost
        if delta > 0 or exp(delta/temp) > random():
            current = successor


def calc_average_cost_increase(problem, inner_iterations, outer_iterations):
    """
    adds up every positive cost change for inner_iterations length Markov chain over outer_iteration number of Markov
    chains, then averages them to find the average increase in cost.

    :param problem:
    :param inner_iterations:
    :param outer_iterations:
    :return:
    """
    total_cost_sum = 0
    total_nums_summed = 0
    for i in range(outer_iterations):
        current = Node(problem)
        inner_cost_sum = 0
        inner_nums_summed = 0
        for j in range(inner_iterations):
            successor = Node(problem, current)
            delta = successor.cost - current.cost
            if delta > 0:
                inner_cost_sum += delta
                inner_nums_summed += 1
            current = successor
        print("Markov Chain #{} average cost increase: {}".format(i, round(float(inner_cost_sum) / inner_nums_summed)))
        total_cost_sum += inner_cost_sum
        total_nums_summed += inner_nums_summed
    print("Average cost increase over all Markov chains: {}".format(round(float(total_cost_sum) / total_nums_summed)))


filename = "../tsp_example_1.txt"
problem = TspProblem(filename)
tnot = time()
calc_average_cost_increase(problem, 100, 100)
print(time() - tnot)

