import sys
import math
import csv

from common import print_solution, read_input, format_solution


def distance(city1, city2):
	return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)


def solve(cities):
	N = len(cities)

	dist = [[0] * N for i in range(N)]
	for i in range(N):
		for j in range(N):
			dist[i][j] = dist[j][i] = distance(cities[i], cities[j])

	def path_length(path):
		node = 0
		for i in range(1, len(path)):
			node += dist[path[i - 1]][path[i]]
		node += dist[path[0]][path[-1]]
		return node

	def df(N):
		def df_sub(n, path):
			global min_length, min_path
			if N == n:
				new_len = path_length(path)
				if new_len < min_length:
					min_length = new_len
					min_path = path[:]
			else:
				for x in range(1, N): 
					if x not in path:
						if n != 2 or path[0] > x:
							path.append(x)
							df_sub(n + 1, path)
							path.pop()
		global min_length, min_path
		min_length = 1e100
		min_path =[]
		for x in range(1, N):
			path=[x,0]
			df_sub(2, path)
		print (min_length)
		return min_path
	return df(N)


if __name__ == '__main__':
	assert len(sys.argv) > 1
	solution = solve(read_input(sys.argv[1]))
	print_solution(solution)
	"""f=open(sys.argv[2],"w")
	writer=csv.writer(f,lineterminator='\n')
	writer.writerow(format_solution(solution))
	
	f.close()"""
