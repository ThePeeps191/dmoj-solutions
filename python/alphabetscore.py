from string import ascii_lowercase as l
c = 0
s = input()
for char in s:
	c += l.index(char) + 1
print(c)