#!/usr/bin/env python3

import sys
import math
import random

from common import print_solution, read_input


def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)


def solve(cities):
    N = len(cities)

    dist = [[0] * N for i in range(N)]
    for i in range(N):
        for j in range(N):
            dist[i][j] = dist[j][i] = distance(cities[i], cities[j])
    
    current_city = 0
    unvisited_cities = set(range(1, N))
    solution = [current_city]

    def distance_from_current_city(to):
        return dist[current_city][to]
    total=0

    while unvisited_cities:
        next_city = min(unvisited_cities, key=distance_from_current_city)
        total+=dist[current_city][next_city]
        unvisited_cities.remove(next_city)
        solution.append(next_city)
        current_city = next_city

    total+=dist[solution[0]][solution[-1]]
    print ("solver_greedy",total)
    print ("greedy",solution)
    
    def rute(solution):
    	total=0
    	for i in range(len(solution)-1):
    		total+=dist[solution[i]][solution[i+1]]
    	return total

    def total_rute(solution):
    	total=0
    	for i in range(len(solution)-1):
    		total+=dist[solution[i]][solution[i+1]]
    	total+=dist[solution[0]][solution[-1]]
    	return total

    def annealing(T, cool=0.99, step=1):
    	T=10000
    	while T>0.0001:
    		i=random.randint(0, len(solution)-1)
    		#parameter=(i-0.5)*step
    		#parameter=int(parameter)
    		if i==len(solution): path=solution[i:0]
    		else: path=solution[i:i+2]
    		new_path=path[::-1]
    		now_dist=rute(solution)
    		new_dist=rute(new_path)
    		

    		p = pow(math.e, -abs(new_dist - now_dist) / T)
    		
    		if new_dist<now_dist or random.random()<p:
    			solution[i:i+2]=path[::-1]

    		T=T*cool
    		
    	return solution

    solution=annealing(solution)
    print (total_rute(solution))
    return solution




if __name__ == '__main__':
    assert len(sys.argv) > 1
    solution = solve(read_input(sys.argv[1]))
    print_solution(solution)
