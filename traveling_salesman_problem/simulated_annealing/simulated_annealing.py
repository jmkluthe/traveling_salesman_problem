#!/usr/bin/env python3

from random import random
from time import time
from math import exp, inf
from traveling_salesman_problem.tsp_problem import TspProblem
from traveling_salesman_problem.simulated_annealing.node import Node
from sys import float_info
#import threading
import _thread


def temperature_schedule(temp):
    if temp < float_info.min:
        return 0
    else:
        return temp*0.95


def simulated_annealing(problem, time_to_run):
    current = Node(problem)
    #t_not = time()
    #out_file = open("cost_vs_time.csv", "w")
    n = 0
    temp = 27695
    while 1:
        #t = time() - t_not
        if temp == 0:
            return current
        #if n % 100 == 0:
        #    out_file.write("{}, {}, {}, {}\n".format(t, current.cost, n, temp))
        #temp = temperature_schedule(time_to_run, t)
        successor = Node(problem, current.visit_order)
        delta = successor.cost - current.cost
        if delta < 0 or exp(- delta/temp) > random():
            current = successor
        n += 1
        temp = temperature_schedule(temp)


filename = "../tsp_example_1.txt"
problem = TspProblem(filename)
best_cost = inf
best_solution = None
tnot = time()
while time() - tnot < 180:
    #solution = _thread.start_new_thread(simulated_annealing, (problem, 180))
    solution = simulated_annealing(problem, 600)
    if solution.cost < best_cost:
        best_cost = solution.cost
        best_solution = solution
print(best_solution.cost)
print(best_cost)

#threading.start_new_thread ( function, args[, kwargs] )