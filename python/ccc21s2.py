M, N, K = int(input()), int(input()), int(input())

# Black is True, Gold Is False
canvas = [[True for _ in range(N)] for _ in range(M)]

for _ in range(K):
	choices = input().split()
	a, b = choices[0], int(choices[1])
	if a == "R":
		row = canvas[b - 1]
		new_row = [not b for b in row]
		canvas[b - 1] = new_row
	else:
		index = b - 1
		for row in canvas:
			row[index] = not row[index]

c = 0
print(canvas)
for r in canvas:
	c += r.count(False)
print(c)