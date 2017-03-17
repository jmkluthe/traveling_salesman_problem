#!/usr/bin/env python3

from random import random
from time import time
from math import exp, inf, log
from traveling_salesman_problem.tsp_problem import TspProblem
from traveling_salesman_problem.simulated_annealing.node import Node


def get_average_time_n_cost(problem, iterations):
    initial_time = time()
    cost_sum = 0
    nums_summed = 0
    current = Node(problem)
    for i in range(iterations):
        successor = Node(problem, current)
        delta = successor.cost - current.cost
        if delta > 0:
            cost_sum += delta
            nums_summed += 1
        current = successor
    time_per_iteration = (time() - initial_time)/iterations
    ave_cost = float(cost_sum)/nums_summed
    return time_per_iteration, ave_cost


class TemperatureSchedule(object):

    def __init__(self, initial_temp, target, iterations):
        self.initial_temp = initial_temp
        self.decrease_factor = target**(1.0/iterations)

    def get_temp(self, temp):
        return temp*self.decrease_factor


def simulated_annealing(problem, time_to_run):
    initial_time = time()
    time_per_iteration, ave_cost = get_average_time_n_cost(problem, 10000)
    #calculate number of iterations to run in given time, w/10s buffer for wrap up
    iterations = round((time_to_run - (time() - initial_time) - 10)/time_per_iteration)
    initial_temp = - ave_cost/log(0.6)
    target = 0.01
    temp_schedule = TemperatureSchedule(initial_temp, target, iterations)
    current = Node(problem)
    temp = initial_temp
    best_cost = inf
    best_solution = None
    for i in range(iterations):
        if current.cost < best_cost:
            best_cost = current.cost
            best_solution = current
        successor = Node(problem, current)
        delta = successor.cost - current.cost
        if delta < 0 or (delta > 0 and exp(- delta / temp) > random()):
            current = successor
        temp = temp_schedule.get_temp(temp)
        # if i % 100000 == 0:
        #     print(temp)
        #     print(current.cost)
    total_time = time() - initial_time
    return best_solution, total_time


def run_annealing(filename):
    problem = TspProblem(filename)
    solution, time = simulated_annealing(problem, 180)
    print(filename)
    print(time)
    print(solution.cost)
    out_file = open("{}.tour".format(filename), "w")
    out_file.write(str(solution.cost) + "\n")
    out_file.writelines((str(el) + "\n") for el in solution.visit_order)


filenames = ["../test-input-1.txt",
             "../test-input-2.txt",
             "../test-input-3.txt",
             "../test-input-4.txt",
             "../test-input-5.txt",
             "../test-input-6.txt",
             "../test-input-7.txt"]
for file in filenames:
    run_annealing(file)

