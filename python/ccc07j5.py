# motels = [0, 990, 1010, 1970, 2030, 2940, 3060, 3930, 4060, 4970, 5030, 5990, 6010, 7000]
# A = int(input())
# B = int(input())
# N = int(input())
# for _ in range(N):
# 	a = int(input())
# 	if a not in motels:
# 		motels.append(a)
# motels.sort()
# L = len(motels)
# dp = [0 for i in range(L)]
# dp[0] = 1
# for i in range(1, L):
# 	cnt = 0
# 	for j in range(i - 1, -1, -1):
# 		dist = motels[i] - motels[j]
# 		if dist >= A and dist <= B: 
# 			cnt += dp[j]
# 	dp[i] = cnt
# print(dp[L-1])


motels = {0, 990, 1010, 1970, 2030, 2940, 3060, 3930, 4060, 4970, 5030, 5990, 6010, 7000}
A, B, N = int(input()), int(input()), int(input())
for _ in range(N):
	m = int(input())
	motels.add(m)

