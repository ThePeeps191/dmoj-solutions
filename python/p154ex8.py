N = int(input())
d = {1, N}
for num in range(2, N // 2 + 1):
	if N % num == 0:
		d.add(num)
		d.add(int(N / num))
print("\n".join([str(a) for a in d]))