from collections import defaultdict
N = int(input())
l = [int(a) for a in input().split()]
num, count = 0, 0
counts = defaultdict(int)
for n in sorted(l):
	counts[n] += 1
	if counts[n] > count:
		count = counts[n]
		num = n
print(num)