# in progress

J = int(input())
A = int(input())
size = [input() for _ in range(J)]
athlete = [input().split() for _ in range(A)]
count = 0
for a in athlete:
	s, num = a
	num = int(num)
	if size[num - 1] == s:
		count += 1
		size[num - 1] = "N"
print(count)