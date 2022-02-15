X = int(input())
spent = [int(input()) for _ in range(int(input()))]
current = X
for s in spent:
	current -= s
	current += X

print(current)