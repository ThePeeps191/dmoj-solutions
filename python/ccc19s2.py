primes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31}

def is_prime(n):
	if n in primes:
		return True
	else:
		if n == 1:
			return False

		i = 2
		while i*i <= n:
			if n % i == 0:
				return False
			i += 1
		primes.add(n)
		return True


for _ in range(int(input())):
	N = int(input())
	if is_prime(N):
		print(N, N)
	else:
		N *= 2
		for i in range(2, N):
			a, b = i, N - i
			if is_prime(a) and is_prime(b):
				print(a, b)
				break