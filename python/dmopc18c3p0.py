r1, g1, b1 = input().split()
r2, g2, b2 = input().split()
r1, g1, b1, r2, g2, b2 = int(r1), int(g1), int(b1), int(r2), int(g2), int(b2)

color1, color2 = [int(r1 ** 0.5), int(g1 ** 0.5), int(b1 ** 0.5)], [int(r2 ** 0.5), int(g2 ** 0.5), int(b2 ** 0.5)]
if color1 == color2:
	print("Dull")
else:
	print("Colourful")