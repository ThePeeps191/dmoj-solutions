import math
for _ in range(10):
	smarties = []

	while True:
		x = input()
		if x != "end of box":
			smarties.append(x)
		else:
			break
	orange = 13 * math.ceil(smarties.count("orange") / 7)
	blue = 13 * math.ceil(smarties.count("blue") / 7)
	green = 13 * math.ceil(smarties.count("green") / 7)
	yellow = 13 * math.ceil(smarties.count("yellow") / 7)
	pink = 13 * math.ceil(smarties.count("pink") / 7)
	violet = 13 * math.ceil(smarties.count("violet") / 7)
	brown = 13 * math.ceil(smarties.count("brown") / 7)
	red = 16 * smarties.count("red")

	time = orange + blue + green + yellow + pink + violet + brown + red

	print(time)