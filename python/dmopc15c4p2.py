H, M = input().split()
H, M = int(H), int(M)
N = int(input())
for _ in range(N):
	M += 1
	if M == 60:
		M = 0
		H += 1
	if H == 24:
		H = 0
print(H, M)