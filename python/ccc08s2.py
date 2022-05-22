while True:
	r = int(input())
	if r == 0:
		break
	count = 0
	for i in range(1, r + 1):
		for j in range(1, r + 1):
			count += 1
	count *= 4
	count -= r ** 2
	count += 1
	if r % 2 == 0:
		print(count)
	else:
		print(count + 1)
