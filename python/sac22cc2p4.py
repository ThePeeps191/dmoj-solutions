# not yet finished


from collections import deque

N, M = input().split()
N, M = int(N), int(M)

parents = {}
grid = [list(input()) for _ in range(M)]
paths = []

def get_next(node):
	next_nodes = []
	dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
	#dirs = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
	for dir in dirs:
		row = node[0] + dir[0]
		col = node[1] + dir[1]
		if row >= 0 and row < M and col >= 0 and col < N:
			next_nodes.append((row, col))
	return next_nodes

#q = deque()
#visited = set()
# def bfs(start, target):
# 	if start == target:
# 		return 0


# def bfs(start, target):
# 	q = [start]
# 	parents[start] = None
# 	while q:
# 		curr = q.pop(0)
# 		for next in get_next(curr):
# 			if next == target:
# 				parents[next] = curr
# 				return
# 			elif next not in parents:
# 				q.append(next)
# 				parents[next] = curr
visited = {(0, 0)}
def dfs(visited, graph, node):
	if node not in visited:
		print(node)
		visited.add(node)
		for neighbour in get_next(node):
			dfs(visited, graph, neighbour)

dfs(visited, grid, ())
print(visited)

# bfs((0, 0), (N - 1, M - 1))
# print(parents)