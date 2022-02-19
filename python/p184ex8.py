v = [input() for _ in range(int(input()))]
i = 0
for x in list("ABCDEF"):
	print(v.count(x))
	i += v.count(x)
print(len(v) - i)