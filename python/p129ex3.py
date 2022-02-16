N = int(input())
start = 1
i = 0
while True:
	if start >= N:
		break
	start *= 2
	i += 1
print(i)