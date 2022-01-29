while True:
	prefix = input()
	if prefix == '0':
		break
	prefix = prefix.replace(' ', '')
	stack = []
	for i in range(len(prefix)-1, -1, -1):
		op = prefix[i]
		if op == '+' or op == '-':
			op1 = stack.pop()
			op2 = stack.pop()
			exp = op1 + ' ' + op2 + ' ' + op
			stack.append(exp)
		else:
			stack.append(op)

	print(*stack)