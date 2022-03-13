N = int(input())
obs = [[int(a) for a in input().split()] for _ in range(N)]
fastest = 0

for i in range(len(obs) - 1):
	a, b = obs[i], obs[i + 1]
	time = abs(b[0] - a[0])
	dist = abs(a[1] - b[1])
	speed = dist / time
	if speed > fastest:
		fastest = speed
print(round(fastest, 2))