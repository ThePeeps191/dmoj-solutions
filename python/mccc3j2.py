N, K = input().split()
N, K = int(N), int(K)
hike = input()
c = 0
s = K
walking = False
for h in hike:
	if not walking:
		if h == "U":
			s -= 1
		if h == "D":
			s += 1
		if not s:
			walking = True
			c += 1
	else:
		if h == "D":
			s += 1
		elif h == "F" and s == 0:
			s += 1
		elif h == "D":
			c += 1
		if s > 0:
			walking = False
if walking:
	c += 1
print(c)