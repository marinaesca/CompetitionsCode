import heapq


DIR = [(-1,0), (1,0), (0,-1), (0,1)]


def solve(grid, m, n, start, end, energy, cost):
	queue = [(0, start)]
	dist = {start: 0}

	while len(queue) > 0:
		u_cost, u = heapq.heappop(queue)

		for i in range(4):
			v = (u[0] + DIR[i][0], u[1] + DIR[i][1])
			v_cost = u_cost + cost[i]

			if v[0] < 0 or v[0] >= m :
				continue
			elif v[1] < 0 or v[1] >= n :
				continue
			elif grid[v[0]][v[1]] == "X":
				continue

			if v not in dist:
				dist[v] = v_cost
				heapq.heappush(queue, (v_cost, v))
			elif v_cost < dist[v]:
				dist[v] = v_cost
				heapq.heappush(queue, (v_cost, v))

	return max(-1, energy - dist[end])





m,n = map(int, raw_input().split())

grid = [raw_input() for _ in range(m)]

energy = int(input())
cost = list(map(int, raw_input().split()))

for r in range(m):
	for c in range(n):
		if grid[r][c] == 'C':
			start = (r,c)
		elif grid[r][c] == 'E':
			end = (r,c)


print solve(grid, m, n, start, end, energy, cost)

