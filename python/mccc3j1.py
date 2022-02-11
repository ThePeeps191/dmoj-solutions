N, i, j = int(input()), int(input()), int(input())

dif1, dif2 = abs(N - i ** 2), abs(N - j ** 2)

print(1 if dif1 < dif2 else 2)