N, M = input().split()
N, M = int(N), int(M)
c = []
for n in range(N, M + 1):
	nums = [int(a) ** 3 for a in str(n)]
	if sum(nums) == n:
		c.append(str(n))

print("\n".join(c))