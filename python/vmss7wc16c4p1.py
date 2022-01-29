A, B = input().split()
A, B = int(A), int(B)
c = 0
for i in range(A, B + 1):
	try:
		if int(i ** 0.5) == i ** 0.5:
			c += 1
	except:
		pass
print(c)