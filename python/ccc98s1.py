for _ in range(int(input())):
	s = input().split()
	o = []
	for x in s:
		if len(x) == 4:
			o.append("****")
		else:
			o.append(x)
	print(*o)