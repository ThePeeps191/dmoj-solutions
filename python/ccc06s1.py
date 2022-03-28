# error


mother, father = input(), input()
for _ in range(int(input())):
	baby = input()
	mom = True
	for char in baby:
		current = mother if mom else father
		if char not in current:
			print("Not their baby!")
			break
		mom = not mom
	else:
		print("Possible baby.")