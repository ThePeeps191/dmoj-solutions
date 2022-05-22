import math
def divisorGenerator(n):
	large_divisors = []
	for i in range(1, int(math.sqrt(n) + 1)):
		if n % i == 0:
			yield i
			if i*i != n:
				large_divisors.append(n / i)
	for divisor in reversed(large_divisors):
		yield divisor

# print list(divisorGenerator(100))

perfectnums = []
for i in range(1000, 10000):
	divs = list(divisorGenerator(i))
	print(divs)
	if sum(divs) - i == i:
		perfectnums.append(i)

print(*perfectnums)