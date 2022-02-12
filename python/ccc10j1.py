import math
c = 0
s = int(input())

for i in zip(range(s + 1), reversed(range(s + 1))):
	if i[0] <= 5 and i[1] <= 5:
		c += 1

print(math.ceil(c / 2))
