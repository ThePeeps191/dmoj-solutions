for _ in range(int(input())):
	i = int(input())
	half = i // 2
	sums = []
	diffs = []
	for x in range(1, half + 1):
		if i % x == 0:
			sums.append(x + i / x)
			if x + i / x != abs(x - i / x):
					diffs.append(abs(x - i / x))
	for elem in sums:
		if elem in diffs:
			print(i, "is nasty")
			break
	else:
		print(i, "is not nasty")