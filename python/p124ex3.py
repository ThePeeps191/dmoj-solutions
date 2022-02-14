N, M, Y = input().split()
N, M, Y = float(N), float(M), int(Y)

current = N

def two_decimals(num):
	num = float(num)
	a, b = str(num).split(".")
	b += "0" * (2 - len(b))
	return a + "." + b

for year in range(Y + 1):
	current = round(current + year * M, 2)
	print(f"{year} {two_decimals(current)}")