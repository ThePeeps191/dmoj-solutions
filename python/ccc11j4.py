convert = lambda s: list(map(tuple, s))

sqs = [[0, -1], [0, -2], [0, -3], [1, -3], [2, -3], [3, -3], [3, -4], [3, -5], [4, -5], [5, -5], [5, -4], [5, -3], [6, -3], [7, -3], [7, -4], [7, -5], [7, -6], [7, -7], [6, -7], [5, -7], [4, -7], [3, -7], [2, -7], [1, -7], [0, -7], [-1, -7], [-1, -6], [-1, -5]]

x, y = -1, -5

while True:
	direc, units = input().split()
	units = int(units)
	if direc == "q":
		break
	if direc == "l":
		c = False
		for _ in range(units):
			x -= 1
			sqs.append([x, y])
		print(f"{x} {y} ", end="")
		if len(convert(sqs)) > len(set(convert(sqs))):
			print("DANGER")
			break
		else:
			print("safe")
	elif direc == "r":
		c = False
		for _ in range(units):
			x += 1
			sqs.append([x, y])
		print(f"{x} {y} ", end="")
		if len(convert(sqs)) > len(set(convert(sqs))):
			print("DANGER")
			break
		else:
			print("safe")
	elif direc == "u":
		c = False
		for _ in range(units):
			y += 1
			sqs.append([x, y])
		print(f"{x} {y} ", end="")
		if len(convert(sqs)) > len(set(convert(sqs))):
			print("DANGER")
			break
		else:
			print("safe")
	elif direc == "d":
		c = False
		for _ in range(units):
			y -= 1
			sqs.append([x, y])
		print(f"{x} {y} ", end="")
		if len(convert(sqs)) > len(set(convert(sqs))):
			print("DANGER")
			break
		else:
			print("safe")