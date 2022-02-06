N = int(input())
a, b = input().split(), input().split()
pairs = set(tuple(([tuple(sorted(l)) for l in zip(a, b)])))
print("good" if len(pairs) == N / 2 else "bad")