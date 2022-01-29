# simple math

ab = input().split()
cd = input().split()
t = int(input())
dist_x = abs(int(ab[0]) - int(cd[0]))
dist_y = abs(int(ab[1]) - int(cd[1]))
dist = dist_x + dist_y
if t >= dist and t % 2 == dist % 2:
	print("Y")
else:
	print("N")