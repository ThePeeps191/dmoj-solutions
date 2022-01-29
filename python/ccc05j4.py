a, b = int(input()), int(input())
c, d = int(input()), int(input())

a -= 2 * c
b -= 2 * d

direc = 1
sqs = []
x, y = c + 1, 1

while True:
	if direc == 1:
		c = 1
		for _ in range(a - 1):
			sqs.append([x + c, y])
			c += 1
		x += c