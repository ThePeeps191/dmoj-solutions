N = int(input())

vals1 = [int(a) for a in input().split()]
vals2 = [int(a) for a in input().split()]
total = 0

for i in range(N):
	h1, h2 = vals1[i], vals1[i + 1]
	width = vals2[i]
	h_dif = abs(h1 - h2)
	min_h = min(h1, h2)
	total += min_h * width
	total += (h_dif * width) / 2
print(total)