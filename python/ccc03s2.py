vowels = ['a', 'e', 'i', 'o', 'u']
for _ in range(int(input())):
	a, b, c, d = list(input().lower()), list(input().lower()), list(input().lower()), list(input().lower())
	a1, b1, c1, d1 = "", "", "", ""
	for char in a[::-1]:
		a1 += char
		if char in vowels or char == " ":
			break
	a1 = a1[::-1]
	for char in b[::-1]:
		b1 += char
		if char in vowels or char == " ":
			break
	b1 = b1[::-1]
	for char in c[::-1]:
		c1 += char
		if char in vowels or char == " ":
			break
	c1 = c1[::-1]
	for char in d[::-1]:
		d1 += char
		if char in vowels or char == " ":
			break
	d1 = d1[::-1]
	if a1 == b1 == c1 == d1:
		print("perfect")
	elif a1 == b1 and c1 == d1:
		print("even")
	elif a1 == c1 and b1 == d1:
		print("cross")
	elif a1 == d1 and b1 == c1:
		print("shell")
	else:
		print("free")