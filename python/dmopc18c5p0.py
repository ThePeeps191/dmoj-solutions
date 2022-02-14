# not yet finished

mode = input()

a = [float(a) for a in input().split()]
b = [float(a) for a in input().split()]

if mode == "Multiply":
	print(f"{a[0] * b[0]} {a[1] * b[1]} {a[2] * b[2]}")
elif mode == "Screen":
