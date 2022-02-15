N = int(input())
h = input().split()
c = 0
for hobby in h:
	if len(hobby) <= 10:
		c += 1
print(c)