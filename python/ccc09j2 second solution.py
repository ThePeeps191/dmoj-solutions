# solution work in progress

a, b, c, score = 1, 2, 3, 2#int(input()), int(input()), int(input()), int(input())
t = 0

for brown in range(0, score // a + 1):
	for north in range(0, score // b + 1):
		for yellow in range(0, score // c):
			br, no, ye = a * brown, b * north, c * yellow
			print(br, no, ye)
			if br + no + ye == score:
				t += 1
				print(f"{br} Brown Trout, {no} Northern Pike, {ye} Yellow Pickerel")

print(f"Number of ways to catch fish: {t}")