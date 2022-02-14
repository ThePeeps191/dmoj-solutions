# not yet finished

S, T = input(), input()

c = 0

for i in range(max(len(S), len(T))):
	try:
		a, b = S[i], T[i]
		if a != b:
			c += 2 * abs(len(S) - len(T))
			break
	except:
		c += abs(len(S) - len(T))
		break

print(c)