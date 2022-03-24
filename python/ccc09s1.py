# stupid python error with cube roots :(

a, b = int(input()), int(input())
c = 0
for n in range(a, b + 1):
	if (abs(int(n ** (1/2)) - (n ** (1/2))) < 4e-17) and (abs(int(n ** (1/3)) - (n ** (1/3))) < 4e-17):
		c += 1
print(c)