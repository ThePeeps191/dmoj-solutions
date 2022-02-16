# not yet finished

from collections import deque

R, C = input().split()
R, C = int(R), int(C)
grid = [list(input()) for _ in range(R)]

def get_neigh_m(node, grid):
	n = []
	direc = [[1, 0], [-1, 0], [0, 1], [0, -1]]
	for d in direc:
		if grid[node[0] + d[0]][node[1] + d[1]] == "M" and 0 <= node[0] + d[0] <= C and 0 <= node[1] + d[1] <= R:
			n.append([node[0] + d[0], node[1] + d[1]])
	return n

def bfs():
	q = deque((0, 0))
	visited = {(0, 0)}
	used = []
	c = 0
	while q:
		curr = q.popleft()
		nextm = get_neigh_m(curr, grid)
		for a in nextm:
			if a not in visited:
				q.append(a)
			visited.add(a)
			if len(a) == 0 and grid[curr[0]][grid[1]] == "M":
				c += 1
			elif a not in used and grid[curr[0]][grid[1]] == "M":
				c += 1
			elif grid[curr[0]][grid[1]] == "M":
				used.append(a)
			if grid[curr[0]][grid[1]] != "M":
				used = []
			if a not in used:
				used.append(a)
	return c





print(bfs())