time = 0
M = int(input())
d = {}
for _ in range(M):
	vals = input().split()
	T = vals[0]
	X = int(vals[1])
	if T == 'R' or T == 'S':
		if X in d:
			d[X].append(time)
		else:
			d[X] = [time]
		time += 1
	else: # 'W'
		time += X-1

for X, times in sorted(d.items()):
	if len(times) % 2 == 1:
		print(X, -1)
	else:
		t = 0
		for i in range(0, len(times), 2):
			t += times[i+1] - times[i]
		print(X, t)