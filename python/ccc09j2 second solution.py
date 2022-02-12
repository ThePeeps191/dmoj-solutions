# solution work in progress

a, b, c, score = 1, 2, 3, 2#int(input()), int(input()), int(input()), int(input())
t = 0

for brown in range(a):
	for north in range(b):
		for yellow in range(c):
			print(brown, north, yellow)
			if brown + north + yellow == score:
				t += 1
				print(f"{brown} Brown Trout, {north} Northern Pike, {yellow} Yellow Pickerel")

print(f"Number of ways to catch fish: {t}")