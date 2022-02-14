# not yet finished

P, A, Y, B = input().split()
P, A, Y, B = int(float(P)), int(A), int(Y), int(B)

y = Y
p = A

while True:
	p += P * p
	# print(p)
	print(p)
	p = int(p)
	y += 1
	if B in range(int(p) - 1000, int(p) + 1000):
		print(y)
		break