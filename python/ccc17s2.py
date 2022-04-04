N = int(input())
m = sorted([int(a) for a in input().split()])
if N % 2 == 0:
	mid = int(N / 2)
	a, b = m[:mid][::-1], m[mid:]
	o = []
	for i, j in zip(a, b):
		o.append(i)
		o.append(j)
	print(*o)
else:
	mid = N // 2 + 1
	a, b = m[:mid][::-1], m[mid:]
	o = []
	for i, j in zip(a, b):
		o.append(i)
		o.append(j)
	print(*o, a[-1])