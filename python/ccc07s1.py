y, m, d = 1989, 2, 27

for _ in range(int(input())):
	year, month, day = input().split()
	year, month, day = int(year), int(month), int(day)
	if year < y:
		print("Yes")
	elif year > y:
		print("No")
	else:
		if month < m:
			print("Yes")
		elif month > m:
			print("No")
		else:
			if day <= d:
				print("Yes")
			else:
				print("No")