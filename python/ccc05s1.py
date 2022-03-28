#error

letters = {
	"ABC" : 2,
	"DEF" : 3,
	"GHI" : 4,
	"JKL" : 5,
	"MNO" : 6,
	"PQRS" : 7,
	"TUV" : 8,
	"WXYZ" : 9
}

for _ in range(int(input())):
	p = input().replace("-", "")
	o = ''
	for char in p:
		if char.isalpha():
			for k in letters.keys():
				if char in k:
					o += str(letters[k])
					break
		else:
			o += char
	print(o[:3], o[3:6], o[6:], sep='-')