#!/usr/bin/env python3

import math
import sys

from common import print_solution, read_input


def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)


def solve(cities):
    # Build a trivial solution.
    # Visit the cities in the order they appear in the input.
    path=list(range(len(cities)))

    N = len(cities)

    dist = [[0] * N for i in range(N)]
    for i in range(N):
        for j in range(N):
            dist[i][j] = dist[j][i] = distance(cities[i], cities[j])

    def rute(solution):
    	total=0
    	for i in range(len(solution)-1):
    		total+=dist[solution[i]][solution[i+1]]
    	total+=dist[solution[0]][solution[-1]]
    	return total

    print (rute(path))
    return path


if __name__ == '__main__':
    assert len(sys.argv) > 1
    solution = solve(read_input(sys.argv[1]))
    print_solution(solution)
