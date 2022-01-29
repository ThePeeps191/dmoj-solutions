N, M = input().split()
N, M = int(N), int(M)
sqs = []
Q = []
for _ in range(M):
	x, y = input().split()
	x, y = int(x), int(y)
	Q.append([x, y])

for q in Q:
	for i in range(N):
		s = [q[0], i + 1]
		if s not in sqs:
			sqs.append(s)
	for i in range(N):
		s = [i + 1, q[1]]
		if s not in sqs:
			sqs.append(s)
	x, y = q[0], q[1]
	while True:
		s = [x - 1, y + 1]
		if (1 <= s[0] <= N) and (1 <= s[1] <= N):
			if s not in sqs:
				sqs.append(s)
			x, y = s[0], s[1]
		else:
			break
	x, y = q[0], q[1]
	while True:
		s = [x + 1, y - 1]
		if (1 <= s[0] <= N) and (1 <= s[1] <= N):
			if s not in sqs:
				sqs.append(s)
			x, y = s[0], s[1]
		else:
			break
	x, y = q[0], q[1]
	while True:
		s = [x + 1, y + 1]
		if (1 <= s[0] <= N) and (1 <= s[1] <= N):
			if s not in sqs:
				sqs.append(s)
			x, y = s[0], s[1]
		else:
			break
	x, y = q[0], q[1]
	while True:
		s = [x - 1, y - 1]
		if (1 <= s[0] <= N) and (1 <= s[1] <= N):
			if s not in sqs:
				sqs.append(s)
			x, y = s[0], s[1]
		else:
			break
print(N ** 2 - len(sqs))