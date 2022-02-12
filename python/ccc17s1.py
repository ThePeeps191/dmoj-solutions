N = int(input())

s1, s2 = 0, 0
a, b = [int(a) for a in input().split()], [int(a) for a in input().split()]
d = 0

for day in range(N):
	score1, score2 = a[day], b[day]
	s1 += score1
	s2 += score2
	if s1 == s2:
		d = day + 1

print(d)