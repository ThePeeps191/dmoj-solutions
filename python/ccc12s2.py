s = input()
d = ['  ']
for c in s:
	if len(d[-1]) == 2:
		d += c
	else:
		d[-1] += c
del d[0]
# I	V	X	L	C	D	M
# 1	5	10	50	100	500	1000
values = {
	"I" : 1,
	"V" : 5,
	"X" : 10,
	"L" : 50,
	"C" : 100,
	"D" : 500,
	"M" : 1000
}
output = 0
for i in range(len(d)):
	v = d[i]
	a, b = int(v[0]), v[1]
	if i != len(d) - 1:
		next_val = d[i + 1]
		b2 = next_val[1]
		value1, value2 = values[b], values[b2]
		if value2 > value1:
			output -= a * values[b]
		else:
			output += a * values[b]
	else:
		output += a * values[b]
print(output)