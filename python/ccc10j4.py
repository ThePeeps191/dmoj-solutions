while True:
	vals = [int(val) for val in input().split()]

	n = vals[0]
	if n == 0:
		break
	elif n == 1:
		print(0)		
	else:
		seqs = vals[1:]
		diffs = []
		for i in range(1, n):
			diffs.append(seqs[i]-seqs[i-1])
		for i in range(0, len(diffs)):
			isPattern = True
			pattern = diffs[:i+1]
			size = i+1
			for j in range(size, len(diffs)):
				if (diffs[j] != pattern[j%size]):
					isPattern = False
					break
			if isPattern:
				print(size)
				break