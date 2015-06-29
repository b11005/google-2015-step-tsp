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
    city_num=N
    next_city=-1
    unvisited_cities = set(range(1, N))
    print (unvisited_cities)
    solution = [current_city]
    

    def distance_from_current_city(to):
        return dist[current_city][to]

    while unvisited_cities:
        min_length=1000000000
        #next_city = min(unvisited_cities, key=distance_from_current_city)
        for i in range(1,city_num):
            next=distance_from_current_city(i)
            if min_length>next:
                min_length=next
                min_path=i
        print ("unvisited_cities", unvisited_cities)
        print ("next_city",next_city)
        next_city=i
        unvisited_cities.remove(next_city)
        city_num=city_num-1
        solution.append(next_city)
        current_city = next_city
        print("solution", solution)
    return solution


if __name__ == '__main__':
    assert len(sys.argv) > 1
    solution = solve(read_input(sys.argv[1]))
    print_solution(solution)
