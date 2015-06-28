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

	def path_length(path):
		n = 0
		i = 1
		for i in range(1, len(path)):
			n += dist[path[i - 1]][path[i]]
		n += dist[path[0]][path[-1]]
		return n

	def df(N):
		def df_sub(f, path):
			global min_length, min_path
			min_length = 1e100
			min_path =[]
			if N == f:
				new_len = path_length(path)
				if new_len < min_length:
					min_length = new_len
					min_path = path[:]
			else:
				for x in range(1, N):
					if x not in path:
						if f != 2 or path[0] > x:
							path.append(x)
							df_sub(f + 1, path)
							path.pop()
		global min_length, min_path
		min_length = 1e100
		min_path = []
		for x in range(1, N):
			path=[x,0]
			df_sub(2, path)
		return min_path
	return df(N)


if __name__ == '__main__':
	assert len(sys.argv) > 1
	solution = solve(read_input(sys.argv[1]))
	print_solution(solution)
