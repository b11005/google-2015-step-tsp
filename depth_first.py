import sys
import math

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

    def dfs(N):
    	def dfs_sub(f, path):
        	global min_length, min_path
        	if N == f:
        		new_len = path_length(path)
        		if new_len < min_length:
        			min_length = new_len
        			min_path = path[:]
        			print(min_length)
        	else:
        		for x in xrange(1, N):
        			if x not in path:
        				if f != 2 or path[0] > x:
        					path.append(x)
        					dfs_sub(f + 1, path)
        					path.pop()
    
    	global min_length, min_path
    	min_length = 1e100
    	min_path = []
    	for x in range(1, N):
    		path=[x,0]
    		dfs_sub(2, path)

    	
    while unvisited_cities:
        next_city = min(unvisited_cities, key=distance_from_current_city)
        unvisited_cities.remove(next_city)
        solution.append(next_city)
        current_city = next_city
    return solution



if __name__ == '__main__':
    assert len(sys.argv) > 1
    solution = solve(read_input(sys.argv[1]))
    print_solution(solution)
