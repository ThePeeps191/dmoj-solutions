from collections import defaultdict, deque

N = int(input())
portals = defaultdict(set)
def bfs(start, end):
	q = deque()
	visited = set()
	if start == end: 
		return True
	q.append(start)
	visited.add(start)
	while len(q) > 0:
		current = q.popleft()
		if current in portals:
			for next in portals[current]:
				if next == end:
					return True
				if next not in visited:
					visited.add(next)
					q.append(next)
	return False

for _ in range(N):
	prompt, a, b = input().split()
	if prompt == "p":
		portals[a].add(b)
		portals[b].add(a)
	else:
		if bfs(a, b):
			print("connected")
		else:
			print("not connected")
