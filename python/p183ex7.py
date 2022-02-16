def sieve(n):
	prime = [True for i in range(n + 1)]
	p = 2
	while (p * p <= n):
		if (prime[p] == True):
			for i in range(p ** 2, n + 1, p):
				prime[i] = False
		p += 1
	prime[0]= False
	prime[1]= False
	del prime[0]
	for p in range(n):
		print(1 if prime[p] else 0)
sieve(int(input()))