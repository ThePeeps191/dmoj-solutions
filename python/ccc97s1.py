for _ in range(int(input())):
	n_count, v_count, n2_count = int(input()), int(input()), int(input())
	noun1 = [input() for _ in range(n_count)]
	verb = [input() for _ in range(v_count)]
	noun2 = [input() for _ in range(n2_count)]
	for n1 in noun1:
		for v in verb:
			for n2 in noun2:
				print(f"{n1} {v} {n2}.")