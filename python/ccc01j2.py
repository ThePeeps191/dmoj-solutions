import math
x, m = int(input()), int(input())
if math.gcd(x, m) == 1:
	print(pow(x, -1, m))
else:
	print("No such integer exists.")
