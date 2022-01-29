a, b = int(input()), int(input())
if a % b == 0:
	print(int(a / b))
else:
	from math import gcd
	g = gcd(a, b)
	if a // b != 0:
		print(f"{a // b} {int((a % b) / g)}/{int(b / g)}")
	else:
		print(f"{int((a % b) / g)}/{int(b / g)}")