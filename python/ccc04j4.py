import re, itertools

k, s = input(), re.sub(r'[^A-Za-z]', '', input())
s = list(s)
l = len(k)

lcyc = itertools.cycle(range(1, l + 1))

encrypt = ""

for char in s:
	i = next(lcyc)
	shift = k[i - 1]
	shift_off = ord(shift) - 65
	new_char = chr(ord(char) + shift_off)
	if ord(new_char) > 90:
		extra = ord(new_char) - 91
		new_char = chr(65 + extra)
	encrypt += new_char

print(encrypt)