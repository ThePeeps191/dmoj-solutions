# nested loops

a = int(input())
b = int(input())
c = int(input())
total = int(input())

ways = 0
for i in range(0, total // a + 1):
	for j in range(0, total // b + 1):
		for k in range(0, total // c + 1):
			fish = i + j + k
			score = i * a + j * b + k * c
			if fish > 0 and score <= total:
				print(f"{i} Brown Trout, {j} Northern Pike, {k} Yellow Pickerel")
				ways += 1
print(f"Number of ways to catch fish: {ways}")