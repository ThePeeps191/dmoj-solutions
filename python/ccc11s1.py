n = ""

for i in range(int(input())):
	n = n + input()

t = n.count("t") + n.count("T")
s = n.count("s") + n.count("S")

if t > s:
	print("English")
else:
	print("French")
