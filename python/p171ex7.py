# not yet finished...

while True:
	num = int(input())
	if num == -1:
		break
	else:
		if 0 <= num < 10000:
			print(1)
		elif 10000 <= num < 20000:
			print(2)
		elif 20000 <= num < 30000:
			print(3)
		elif 30000 <= num < 40000:
			print(4)
		elif 40000 <= num < 50000:
			print(5)
		else:
			print(6)