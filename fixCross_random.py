#!/usr/bin/env python3

import math
import sys

from common import print_solution, read_input


def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)


def solve(cities):
    # Build a trivial solution.
    # Visit the cities in the order they appear in the input.
    N = len(cities)

    dist = [[0] * N for i in range(N)]
    for i in range(N):
        for j in range(N):
            dist[i][j] = dist[j][i] = distance(cities[i], cities[j])

    path=list(range(len(cities)))

    def fix_cross(N, path):
        total=0
        while True:
            count=0
            for i in range(N-2):
                i1=i+1
                for j in range(i+2,N):
                    if j==N-1: j1=0
                    else: j1=j+1
                    if i!=0 or j1!=0:
                        if dist[path[i]][path[i1]]+dist[path[j]][path[j1]]>dist[path[i]][path[j]]+dist[path[i1]][path[j1]]:
                            new_path=path[i1:j+1]
                            path[i1:j+1]=new_path[::-1]
                            count+=1
            total+=count
            if count==0: break
        return path

    def total_rute(solution):
    	total=0
    	for i in range(len(solution)-1):
    		total+=dist[solution[i]][solution[i+1]]
    	total+=dist[solution[0]][solution[-1]]
    	return total

    solution=fix_cross(N,path)
    print (total_rute(solution))
    return solution


if __name__ == '__main__':
    assert len(sys.argv) > 1
    solution = solve(read_input(sys.argv[1]))
    print_solution(solution)
    

