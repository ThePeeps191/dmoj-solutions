N = int(input())
c = 0

for i in range(0, N // 5 + 1):
	for j in range(0, N // 4 + 1):
		five, four = 5 * i, 4 * j
		if five + four == N:
			c += 1
print(c)