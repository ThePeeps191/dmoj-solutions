N = int(input())
for _ in range(N):
	x = [input() for _ in range(3)]
	t = False
	for i in range(3):
		for j in range(3):
			if i != j:
				a, b = x[i], x[j]
				if a.startswith(b) or b.endswith(a):
					t = True
					break
	print("No" if t else "Yes")