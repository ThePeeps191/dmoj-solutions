N = int(input())
current = []
x = []
y = []
nums = [int(a) for a in input().split()]
for n in nums:
	if n % 2 != 1:
		x.append(n)
	else:
		current.append(x)
		x = []
current.append(x)
for l in current:
	y.append(sum(l))

print(max(y))