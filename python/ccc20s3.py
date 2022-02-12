from itertools import permutations as p

N, H = input().lower(), input().lower()
print(N, H)
c = 0
if N in H: c += 1
for perm in list(set(p(N))):
	if ''.join(perm) in H:
		c += 1

print(c)