J = int(input())
A = int(input())
size_values = {"S": 0, "M": 1, "L" : 2}
size = [size_values[input()] for _ in range(J)]
athlete = [input().split() for _ in range(A)]
count = 0
for a in athlete:
	s, num = a
	s = size_values[s]
	num = int(num)
	if size[num - 1] >= s:
		count += 1
		size[num - 1] = -1
print(count)