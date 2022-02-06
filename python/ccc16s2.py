type_question = input()
N = input()
dmoj = list(map(int, input().split()))
peg = list(map(int, input().split()))

dmoj.sort()
peg.sort()

if type_question == "2":
	peg.reverse()

print(sum(max(a, b) for a, b in zip(dmoj, peg)))
