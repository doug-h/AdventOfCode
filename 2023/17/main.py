
import timeit
import heapq


def pq_push(h, p, data):
	heapq.heappush(h, (p, pq_push._x, data))
	pq_push._x += 1
pq_push._x = 0


def pq_pop(h):
	p, _, data = heapq.heappop(h)
	return p, data


grid = {
	(a + b * 1j): int(d)
	for b, row in enumerate(open("data.txt").readlines())
	for a, d in enumerate(row.rstrip())
}
start = list(grid.keys())[0]
end = list(grid.keys())[-1]

def get_neighbours(p, d, c, min_step, max_step):
	neighbours = []
	for nd in d * 1j, d * -1j:
		for i in range(min_step, max_step + 1):
			np = p + nd * i
			if 0 <= np.real <= end.real and 0 <= np.imag <= end.imag:
				nc = c + sum([grid[p + nd * (_i+1)] for _i in range(i)])
				neighbours.append((np,nc,nd))
	return neighbours

def dijkstra(min_step, max_step):
	frontier = []
	visited = set()

	pq_push(frontier, 0, (start, 1))
	pq_push(frontier, 0, (start, 1j))

	while frontier:
		c, (p, d) = pq_pop(frontier)

		if p == end:
			return c
		if (p, d) in visited:
			continue
		visited.add((p, d))

		for np,nc,nd in get_neighbours(p,d,c, min_step, max_step):
			pq_push(frontier, nc, (np, nd))

answer1 = dijkstra(1,3)
answer2 = dijkstra(4,10)

print(f"Part one: {answer1}")
print(f"Part two: {answer2}")

assert (answer1 == 1001)
assert (answer2 == 1197)
