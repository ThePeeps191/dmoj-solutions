# not yet finished

r = []

def len_repeat(seq):
	max_len = int(len(seq) // 2)
	for x in range(2, max_len):
		if seq[0:x] == seq[x:2*x]:
			return x + 1
	return len(seq)

while True:
	u = input()
	if u == "0":
		break
	nums = [int(a) for a in u.split()[1:]]
	dif = [j-i for i, j in zip(nums[:-1], nums[1:])]
	print(len_repeat(dif))
