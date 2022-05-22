N = int(input())

for n in range(N):
	i = int(input())
	orig = i
	print(i)
	while len(str(i)) > 2:
		d = int(str(i)[-1])
		i = int(str(i)[:-1])
		i -= d
		print(i)
	if i % 11 == 0:
		print(f"The number {orig} is divisible by 11.")
	else:
		print(f"The number {orig} is not divisible by 11.")

	if n != N - 1:
		print()