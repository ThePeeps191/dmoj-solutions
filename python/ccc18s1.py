N = int(input())
vils = sorted([int(input()) for _ in range(N)])

dists = []
for i in range(len(vils) - 1):
	dists.append(vils[i + 1] - vils[i])
print(vils);print(dists)
neighs = [1]
current = 0

for d in range(1, len(dists) - 1):
	left, right = dists[d - 1], dists[d + 1]
	if left < right:
		neighs[current] += 1
	elif right < left:
		neighs.append(0)
		current += 1
		neighs[current] += 1
	else:
		neighs[current] += 1
		neighs.append(0)
		current += 1
		neighs[current] += 1
neighs[-1] += 1
print(neighs)
print(min(neighs), '.0', sep='')