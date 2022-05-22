# in progress

sizes = [[int(a) for a in input().split()]]
items = [[int(a) for a in input().split()]]
print(sizes)
print(items)

for item in items:
	for size in sizes:
		if item[0] <= size[0] and item[1] <= size[1] and item[2] <= size[2]:
			print(size[0] * size[1] * size[2])
			break
	else:
		print("Item does not fit.")