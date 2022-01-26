while True:
	prefix = input()
	if prefix == "0":
		break
	prefix = prefix.replace(' ', '')
	stack = []
	for i in range(len(prefix) - 1, -1, -1):
		op = prefix[i]
		if op == "+" or op == "-":
			op1