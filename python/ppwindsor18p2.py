# not yet finished

W, H = int(input()), int(input())
# start = False
x = False
s = ""
if H % 2 == 0:
	for _ in range(H):
		for _ in range(W):
			if x:
				s += "1"
			else:
				s += "0"
			x = not x
		x = not x
		s += "\n"
else:
	for _ in range(H):
		for _ in range(W):
			if x:
				s += "1"
			else:
				s += "0"
			x = not x
		s += "\n"


print(s)