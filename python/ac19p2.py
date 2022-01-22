from string import ascii_lowercase as a
a = list(a)
N = int(input())
L = int(input())
S = input()

for char in S:
	print(a[(a.index(char) + L) % 26] if char != " " else " ", end="")
