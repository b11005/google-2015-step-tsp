#!/usr/bin/env python3

import math
import sys
import csv

from common import print_solution, read_input, format_solution


def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)


def solve(cities):
    N = len(cities)
    total=0
    mini=10000000
    dist = [[0] * N for i in range(N)]
    for i in range(N):
        for j in range(N):
            dist[i][j] = dist[j][i] = distance(cities[i], cities[j])
            total+=dist[i][j]
        if total!=0 and mini>total: mini=total
    print (mini)
    
    current_city = 0
    unvisited_cities = set(range(1, N))
    solution = [current_city]

    """def distance_from_current_city(to):
        return dist[current_city][to]"""

    while unvisited_cities:
        #next_city = min(unvisited_cities, key=distance_from_current_city)
        if total!=0 and mini>total: 
            mini=total
        for i in unvisited_cities:# key=distance_from_current_city
            next_city=i
        unvisited_cities.remove(next_city)
        solution.append(next_city)
        current_city = next_city
    return solution


if __name__ == '__main__':
    assert len(sys.argv) > 1
    solution = solve(read_input(sys.argv[1]))
    print_solution(solution)
    '''f=open(sys.argv[2],"w")
    writer=csv.writer(f,lineterminator='\n')
    for i in range(len(solution)-1):
        writer.writerow(solution)
    writer.writerow(solution(solution))
    
    f.close()'''