n = int(input())
coders = set([int(a) for a in input().split()])
print(n - len(coders) + 1)