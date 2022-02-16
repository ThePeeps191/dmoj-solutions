# not yet finished

from math import floor as f
N, K = input().split()
N, K = int(N), int(K)
b = 0
t = 0
while True:
	b += 1
	t += 1
	if b % K == 0:
		b -= 1
	print(b, t)
	if t == N:
		break
print(b)