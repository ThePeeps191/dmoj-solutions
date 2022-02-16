from collections import defaultdict, deque

N, M, A, B = input().split()
N, M, A, B = int(N), int(M), int(A), int(B)
n = defaultdict(set)

for _ in range(M):
	a, b = input().split()
	a, b = int(a), int(b)
	n[a].add(b)
	n[b].add(a)
print(n)
def bfs():
	q = deque([A])
	visited = {A}
	while q:
		curr = q.popleft()
		for house in n[curr]:
			if house != curr and house not in visited:
				visited.add(house)
				if house not in visited:
					q.append(house)
				if house == B:
					return True
			#if len(visited) == N - 1:
			#	return False
	print(visited)
	return False

if bfs():
	print("GO SHAHIR!")
else:
	print("NO SHAHIR!")